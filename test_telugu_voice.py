#!/usr/bin/env python3
"""
Quick test for Telugu voice availability
"""

import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

def test_telugu_voices():
    """Test Telugu voices"""
    print(f"🔍 Testing Telugu voices in region: {AZURE_SPEECH_REGION}")
    
    # Telugu voice candidates
    telugu_voices = [
        ("te-IN-ShrutiNeural", "Shruti (Telugu Female)"),
        ("te-IN-MohanNeural", "Mohan (Telugu Male)"),
    ]
    
    working_voices = []
    
    for voice_id, voice_name in telugu_voices:
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
            
            # Test with Telugu text
            test_text = "నమస్కారం, ఇది వాయిస్ టెస్ట్."
            result = speech_synthesizer.speak_text_async(test_text).get()
            
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print(f"✅ {voice_name} ({voice_id}) - WORKS")
                working_voices.append((voice_id, voice_name))
            else:
                print(f"❌ {voice_name} ({voice_id}) - FAILED")
                
        except Exception as e:
            print(f"❌ {voice_name} ({voice_id}) - ERROR: {str(e)}")
    
    if working_voices:
        print(f"\n🎯 Telugu voices available: {len(working_voices)}")
        for voice_id, voice_name in working_voices:
            print(f"  ✅ {voice_name} - {voice_id}")
    else:
        print("\n❌ No Telugu voices available in this region")
    
    return working_voices

if __name__ == "__main__":
    test_telugu_voices()
