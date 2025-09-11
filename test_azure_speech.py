#!/usr/bin/env python3
"""
Test script to diagnose Azure Speech Services issues
"""

import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION, VOICE_IDS

def test_azure_speech():
    """Test Azure Speech Services with detailed error reporting"""
    
    print("🔍 Testing Azure Speech Services Configuration...")
    print(f"Region: {AZURE_SPEECH_REGION}")
    print(f"Key: {'*' * 20}...{AZURE_SPEECH_KEY[-4:] if AZURE_SPEECH_KEY else 'NOT SET'}")
    
    try:
        # Configure speech config
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_SPEECH_KEY, 
            region=AZURE_SPEECH_REGION
        )
        
        # Test with a simple voice
        voice_id = VOICE_IDS["English"]["Jenny (US Female)"]
        speech_config.speech_synthesis_voice_name = voice_id
        speech_config.set_speech_synthesis_output_format(
            speechsdk.SpeechSynthesisOutputFormat.Audio16Khz128KBitRateMonoMp3
        )
        
        print(f"Voice: {voice_id}")
        
        # Create speech synthesizer
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        
        # Test with simple text
        test_text = "Hello, this is a test of Azure Speech Services."
        print(f"Test text: {test_text}")
        
        # Generate speech
        print("🎵 Generating speech...")
        result = speech_synthesizer.speak_text_async(test_text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("✅ Speech synthesis successful!")
            print(f"Audio data size: {len(result.audio_data)} bytes")
            
            # Save test audio file
            with open("test_audio.mp3", "wb") as audio_file:
                audio_file.write(result.audio_data)
            print("💾 Test audio saved as 'test_audio.mp3'")
            
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"❌ Speech synthesis canceled: {cancellation_details.reason}")
            
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"❌ Error details: {cancellation_details.error_details}")
                
                # Provide specific troubleshooting
                error_details = cancellation_details.error_details.lower()
                if "authentication" in error_details or "unauthorized" in error_details:
                    print("\n🔧 TROUBLESHOOTING:")
                    print("- Check if your Azure Speech API key is correct")
                    print("- Verify the region matches your Azure resource")
                    print("- Ensure the subscription is active")
                    
                elif "quota" in error_details or "limit" in error_details:
                    print("\n🔧 TROUBLESHOOTING:")
                    print("- You may have exceeded your Azure Speech quota")
                    print("- Check your Azure portal for usage limits")
                    
                elif "voice" in error_details:
                    print(f"\n🔧 TROUBLESHOOTING:")
                    print(f"- Voice '{voice_id}' may not be available in region '{AZURE_SPEECH_REGION}'")
                    print("- Try a different voice or region")
                    
        else:
            print(f"❌ Unexpected result: {result.reason}")
            
    except Exception as e:
        print(f"❌ Exception occurred: {str(e)}")
        print("\n🔧 TROUBLESHOOTING:")
        print("- Check if azure-cognitiveservices-speech is installed correctly")
        print("- Verify your internet connection")
        print("- Ensure config.py has the correct credentials")

if __name__ == "__main__":
    test_azure_speech()
