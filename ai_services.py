import requests
import json
import azure.cognitiveservices.speech as speechsdk
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from config import *
from huggingface_hub import InferenceClient
import google.generativeai as genai

class AIServices:
    def __init__(self):
        """Initialize AI services with API credentials"""
        self.hf_token = HUGGINGFACE_API_TOKEN
        self.azure_key = AZURE_SPEECH_KEY
        self.azure_region = AZURE_SPEECH_REGION
        self.azure_endpoint = AZURE_SPEECH_ENDPOINT
        
        # Initialize Hugging Face model
        self.model_name = GRANITE_MODEL_NAME
        self.tokenizer = None
        self.model = None
        self.hf_client = None
        self.gemini_client_inited = False
        
    def load_granite_model(self):
        """Load IBM Granite model locally unless using Inference API"""
        if USE_GEMINI:
            # Initialize Gemini client once
            try:
                genai.configure(api_key=GEMINI_API_KEY)
                self.gemini_client_inited = True
                print("Using Google Gemini for rewriting.")
            except Exception as e:
                print(f"❌ Failed to init Gemini: {e}")
            return True
        if USE_HF_INFERENCE:
            print("Using Hugging Face Inference API; skipping local model load.")
            try:
                self.hf_client = InferenceClient(model=self.model_name, token=self.hf_token)
            except Exception as e:
                print(f"❌ Failed to init HF InferenceClient: {e}")
            return True
        candidates = [self.model_name] + [c for c in GRANITE_MODEL_CANDIDATES if c != self.model_name]
        last_error = None
        for candidate in candidates:
            try:
                print(f"Loading IBM Granite model: {candidate} ...")
                self.tokenizer = AutoTokenizer.from_pretrained(
                    candidate,
                    token=self.hf_token,
                    trust_remote_code=True
                )
                self.model = AutoModelForCausalLM.from_pretrained(
                    candidate,
                    token=self.hf_token,
                    torch_dtype=torch.float16,
                    device_map="auto",
                    trust_remote_code=True
                )
                self.model_name = candidate
                print(f"✅ IBM Granite model loaded successfully: {candidate}")
                return True
            except Exception as e:
                last_error = str(e)
                print(f"❌ Failed to load {candidate}: {last_error}")
                continue
        print(f"❌ Error loading Granite model after trying candidates: {last_error}")
        return False
    
    def rewrite_text_with_tone(self, original_text, target_tone, target_language="English"):
        """Rewrite text using IBM Granite with specific tone and language"""
        try:
            # Import the function from config
            from config import get_tone_prompt
            
            # Get language-specific prompt
            prompt_template = get_tone_prompt(target_tone, target_language)
            prompt = prompt_template.format(text=original_text)

            # Inference path: Gemini
            if USE_GEMINI:
                try:
                    if not self.gemini_client_inited:
                        genai.configure(api_key=GEMINI_API_KEY)
                        self.gemini_client_inited = True
                    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
                    response = model.generate_content(prompt)
                    rewritten_text = response.text if hasattr(response, 'text') and response.text else ""
                    if not rewritten_text:
                        rewritten_text = "AI rewriting in progress... Please try again."
                    return rewritten_text, None
                except Exception as e:
                    return None, f"Gemini error: {str(e)}"

            # Inference path: call HF Inference API directly
            if USE_HF_INFERENCE:
                try:
                    if not self.hf_client:
                        self.hf_client = InferenceClient(model=self.model_name, token=self.hf_token)
                    rewritten_text = self.hf_client.text_generation(
                        prompt,
                        max_new_tokens=MAX_TOKENS,
                        temperature=TEMPERATURE,
                        top_p=0.9
                    )
                except Exception as e:
                    return None, f"HF Inference error: {str(e)}"
                if not rewritten_text:
                    rewritten_text = "AI rewriting in progress... Please try again."
                return rewritten_text, None

            if not self.model or not self.tokenizer:
                return None, "Model not loaded"
            
            # Tokenize input
            inputs = self.tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
            
            # Generate text
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=MAX_TOKENS,
                    temperature=TEMPERATURE,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            # Decode and clean output
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract only the rewritten part (remove the prompt)
            rewritten_text = generated_text.replace(prompt, "").strip()
            
            if not rewritten_text:
                rewritten_text = "AI rewriting in progress... Please try again."
            
            return rewritten_text
            
        except Exception as e:
            error_msg = f"Error in text rewriting: {str(e)}"
            print(f"❌ {error_msg}")
            return f"Error in text rewriting: {str(e)}"
    
    def generate_speech_azure(self, text, voice_id, output_format="audio-16khz-128kbitrate-mono-mp3", max_retries=2):
        """Generate speech using Azure Cognitive Services with simplified approach"""
        import time
        
        # Validate inputs
        if not self.azure_key or not self.azure_region:
            return None, "Azure Speech credentials not configured"
        
        if not text or not text.strip():
            return None, "No text provided for speech synthesis"
        
        # Remove character limit completely for full audio generation
        # if len(text) > 5000:
        #     text = text[:5000] + "..."
        
        print(f"🎵 Generating speech for {len(text)} characters...")
        print(f"Voice: {voice_id}")
        print(f"🔍 DEBUG - Text length: {len(text)}")
        print(f"🔍 DEBUG - Will chunk: {len(text) > 1000}")
        print(f"🔍 DEBUG - First 200 chars: {text[:200]}...")
        print(f"🔍 DEBUG - Last 200 chars: ...{text[-200:]}")
        
        for attempt in range(max_retries + 1):
            try:
                print(f"Attempt {attempt + 1}/{max_retries + 1}")
                
                # Configure speech
                speech_config = speechsdk.SpeechConfig(
                    subscription=self.azure_key, 
                    region=self.azure_region
                )
                speech_config.speech_synthesis_voice_name = voice_id
                speech_config.set_speech_synthesis_output_format(
                    speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3
                )
                
                # Create synthesizer
                synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
                
                # Use paragraph-based chunking for better natural breaks
                paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
                if not paragraphs:
                    # Fallback to sentence-based chunking if no paragraphs
                    sentences = [s.strip() + '.' for s in text.split('.') if s.strip()]
                    paragraphs = sentences
                
                print(f"📝 Processing {len(paragraphs)} paragraphs/chunks")
                
                # Import pydub for proper audio merging
                try:
                    from pydub import AudioSegment
                    import io
                    use_pydub = True
                    print("🔧 Using pydub for audio merging")
                except ImportError:
                    use_pydub = False
                    print("⚠️ pydub not available, using basic byte concatenation")
                
                audio_segments = []
                audio_chunks = []
                
                for i, paragraph in enumerate(paragraphs):
                    if not paragraph.strip():
                        continue
                        
                    print(f"🔄 Processing paragraph {i+1}/{len(paragraphs)} ({len(paragraph)} chars)")
                    chunk_result = synthesizer.speak_text_async(paragraph).get()
                    
                    if chunk_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                        audio_data = chunk_result.audio_data
                        print(f"✅ Paragraph {i+1} completed: {len(audio_data)} bytes")
                        
                        if use_pydub:
                            # Use pydub for proper audio merging
                            audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
                            audio_segments.append(audio_segment)
                        else:
                            # Fallback to byte concatenation
                            audio_chunks.append(audio_data)
                    else:
                        error_details = chunk_result.error_details if hasattr(chunk_result, 'error_details') else "Unknown error"
                        print(f"❌ Paragraph {i+1} failed: {error_details}")
                        return None, f"Paragraph {i+1} failed: {error_details}"
                
                if use_pydub and audio_segments:
                    # Merge audio segments properly with pydub
                    final_audio = AudioSegment.empty()
                    for segment in audio_segments:
                        final_audio += segment
                    
                    # Export to bytes
                    output_buffer = io.BytesIO()
                    final_audio.export(output_buffer, format="mp3")
                    combined_audio = output_buffer.getvalue()
                    print(f"🎉 Successfully merged {len(audio_segments)} audio segments with pydub! Total size: {len(combined_audio)} bytes")
                    return combined_audio, None
                    
                elif audio_chunks:
                    # Fallback: basic byte concatenation
                    combined_audio = b''.join(audio_chunks)
                    print(f"🎉 Successfully combined {len(audio_chunks)} chunks! Total audio size: {len(combined_audio)} bytes")
                    return combined_audio, None
                else:
                    return None, "No audio chunks were generated"
                
            except Exception as e:
                print(f"❌ Exception on attempt {attempt + 1}: {str(e)}")
                if attempt < max_retries - 1:
                    print("⏱️ Waiting 3 seconds before retry...")
                    time.sleep(3)
                    continue
                else:
                    return None, f"Error in speech generation after {max_retries + 1} attempts: {str(e)}"
        
        return None, f"Failed to generate speech after {max_retries + 1} attempts"
    
    def _apply_emotional_prosody(self, text, intensity, tone):
        """Apply SSML prosody based on emotional intensity and tone"""
        
        # Handle tuple input - extract text if it's a tuple
        if isinstance(text, tuple):
            text = text[0] if text[0] else "No text provided"
        
        # Ensure text is a string
        if not isinstance(text, str):
            text = str(text)
        
        # Debug intensity conversion
        print(f"🔍 DEBUG - intensity before conversion: {intensity}, type: {type(intensity)}")
        
        # Ensure intensity is an integer
        try:
            intensity = int(float(intensity))  # Convert via float first to handle string numbers
        except (ValueError, TypeError):
            print(f"❌ Failed to convert intensity: {intensity}")
            intensity = 5  # Default to medium intensity
        
        print(f"🔍 DEBUG - intensity after conversion: {intensity}, type: {type(intensity)}")
        
        # Map intensity (1-10) to prosody values
        if intensity <= 3:
            rate = "slow"
            pitch = "-5%"
            volume = "soft"
        elif intensity <= 6:
            rate = "medium"
            pitch = "+0%"
            volume = "medium"
        else:
            rate = "fast"
            pitch = "+10%"
            volume = "loud"
        
        # Tone-specific adjustments
        tone_adjustments = {
            "Suspenseful": {
                "rate": "x-slow" if intensity > 7 else "slow",
                "pitch": "+15%" if intensity > 7 else "+5%",
                "emphasis": "strong"
            },
            "Inspiring": {
                "rate": "medium",
                "pitch": "+20%" if intensity > 7 else "+10%",
                "emphasis": "moderate"
            },
            "Humorous": {
                "rate": "fast" if intensity > 6 else "medium",
                "pitch": "+25%" if intensity > 7 else "+15%",
                "emphasis": "strong"
            },
            "Authoritative": {
                "rate": "slow",
                "pitch": "-10%" if intensity > 6 else "-5%",
                "emphasis": "strong"
            },
            "Storytelling": {
                "rate": "medium",
                "pitch": "+10%" if intensity > 6 else "+5%",
                "emphasis": "moderate"
            }
        }
        
        # Apply tone-specific settings if available
        if tone in tone_adjustments:
            adj = tone_adjustments[tone]
            rate = adj.get("rate", rate)
            pitch = adj.get("pitch", pitch)
            emphasis = adj.get("emphasis", "moderate")
        else:
            emphasis = "moderate"
        
        # Create SSML with prosody
        ssml = f'''<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
            <prosody rate="{rate}" pitch="{pitch}" volume="{volume}">
                <emphasis level="{emphasis}">{text}</emphasis>
            </prosody>
        </speak>'''
        
        return ssml
    
    def create_audiobook_transcript(self, original_text, rewritten_text, tone, voice):
        """Create formatted transcript for audiobook"""
        transcript = f"""# EchoVerse Audiobook Transcript

## Content Details
- **Original Tone:** Standard
- **Target Tone:** {tone}
- **Voice:** {voice}
- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Original Text
{original_text}

## AI-Rewritten Text ({tone} Tone)
{rewritten_text}

## Audio Production Notes
- **Pacing:** {'Slow and deliberate' if tone == 'Suspenseful' else 'Natural flow' if tone == 'Neutral' else 'Energetic and engaging'}
- **Emphasis:** {'Key phrases for dramatic effect' if tone == 'Suspenseful' else 'Clear pronunciation' if tone == 'Neutral' else 'Motivational highlights'}
- **Background:** {'Atmospheric music recommended' if tone == 'Suspenseful' else 'Minimal background' if tone == 'Neutral' else 'Uplifting soundtrack'}

---
*Generated by EchoVerse - AI-Powered Audiobook Creation Tool*
"""
        return transcript
    
    def create_podcast_transcript(self, original_text, rewritten_text, tone, voice):
        """Create formatted transcript for podcast"""
        transcript = f"""# EchoVerse Podcast Transcript

## Episode Details
- **Content Type:** {tone} Narrative
- **Voice:** {voice}
- **Duration:** [Audio duration will be calculated]
- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Opening Segment
{rewritten_text[:200]}...

## Main Content
{rewritten_text}

## Production Guidelines
- **Intro Music:** {'Dramatic build-up' if tone == 'Suspenseful' else 'Professional intro' if tone == 'Neutral' else 'Energetic opening'}
- **Pacing:** {'Controlled tension' if tone == 'Suspenseful' else 'Steady rhythm' if tone == 'Neutral' else 'Dynamic flow'}
- **Transitions:** {'Smooth fades' if tone == 'Suspenseful' else 'Clean cuts' if tone == 'Neutral' else 'Energetic bridges'}

## Closing Notes
- **Call to Action:** {'Engage audience with mystery' if tone == 'Suspenseful' else 'Professional sign-off' if tone == 'Neutral' else 'Motivational closing'}
- **Outro Music:** {'Atmospheric fade' if tone == 'Suspenseful' else 'Clean ending' if tone == 'Neutral' else 'Uplifting outro'}

---
*Generated by EchoVerse - AI-Powered Content Transformation*
"""
        return transcript

# Import datetime for transcript generation
from datetime import datetime
