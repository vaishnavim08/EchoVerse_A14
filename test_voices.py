 #!/usr/bin/env python3
"""
Test script to check Azure TTS voices availability in Central India region
"""

import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

def test_voice(voice_id, voice_name, category):
    """Test a specific voice"""
    try:
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_SPEECH_KEY, 
            region=AZURE_SPEECH_REGION
        )
        speech_config.speech_synthesis_voice_name = voice_id
        speech_config.set_speech_synthesis_output_format(
            speechsdk.SpeechSynthesisOutputFormat.Audio16Khz128KBitRateMonoMp3
        )
        
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        
        # Test with short text to avoid timeouts
        test_text = "Hello, this is a voice test."
        result = speech_synthesizer.speak_text_async(test_text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"✅ {category} - {voice_name} ({voice_id}) - WORKS")
            return True
        else:
            print(f"❌ {category} - {voice_name} ({voice_id}) - FAILED: {result.reason}")
            return False
            
    except Exception as e:
        print(f"❌ {category} - {voice_name} ({voice_id}) - ERROR: {str(e)}")
        return False

def test_all_voices():
    """Test various Azure TTS voices for different categories"""
    print(f"🔍 Testing Azure TTS voices in region: {AZURE_SPEECH_REGION}")
    print("=" * 60)
    
    # Voice candidates to test
    voices_to_test = [
        # Female voices
        ("en-US-JennyNeural", "Jenny (US Female)", "Female"),
        ("en-US-AriaNeural", "Aria (US Female)", "Female"),
        ("en-GB-SoniaNeural", "Sonia (UK Female)", "Female"),
        ("en-AU-NatashaNeural", "Natasha (AU Female)", "Female"),
        ("en-IN-NeerjaNeural", "Neerja (IN Female)", "Female"),
        
        # Male voices
        ("en-US-GuyNeural", "Guy (US Male)", "Male"),
        ("en-US-TonyNeural", "Tony (US Male)", "Male"),
        ("en-GB-RyanNeural", "Ryan (UK Male)", "Male"),
        ("en-AU-WilliamNeural", "William (AU Male)", "Male"),
        ("en-IN-PrabhatNeural", "Prabhat (IN Male)", "Male"),
        
        # Kids voices
        ("en-US-AnaNeural", "Ana (US Child)", "Child"),
        ("en-GB-MaisieNeural", "Maisie (UK Child)", "Child"),
        ("en-US-JennyMultilingualNeural", "Jenny Multilingual (Child-like)", "Child"),
    ]
    
    working_voices = {
        "Female": [],
        "Male": [],
        "Child": []
    }
    
    for voice_id, voice_name, category in voices_to_test:
        if test_voice(voice_id, voice_name, category):
            working_voices[category].append((voice_id, voice_name))
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY OF WORKING VOICES:")
    print("=" * 60)
    
    for category, voices in working_voices.items():
        print(f"\n{category} Voices ({len(voices)} working):")
        for voice_id, voice_name in voices:
            print(f"  ✅ {voice_name} - {voice_id}")
    
    return working_voices

if __name__ == "__main__":
    working_voices = test_all_voices()
