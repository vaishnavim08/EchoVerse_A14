#!/usr/bin/env python3
"""
Test script to check Azure TTS multi-language voices availability in Central India region
"""

import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

def test_multilang_voice(voice_id, voice_name, language, test_text):
    """Test a specific multi-language voice"""
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
        
        result = speech_synthesizer.speak_text_async(test_text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"✅ {language} - {voice_name} ({voice_id}) - WORKS")
            return True
        else:
            print(f"❌ {language} - {voice_name} ({voice_id}) - FAILED: {result.reason}")
            return False
            
    except Exception as e:
        print(f"❌ {language} - {voice_name} ({voice_id}) - ERROR: {str(e)}")
        return False

def test_multilanguage_voices():
    """Test various multi-language Azure TTS voices"""
    print(f"🌍 Testing Multi-Language Azure TTS voices in region: {AZURE_SPEECH_REGION}")
    print("=" * 80)
    
    # Multi-language voice candidates to test
    multilang_voices = [
        # Hindi voices
        ("hi-IN-MadhurNeural", "Madhur (Hindi Male)", "Hindi", "नमस्ते, यह एक आवाज परीक्षण है।"),
        ("hi-IN-SwaraNeural", "Swara (Hindi Female)", "Hindi", "नमस्ते, यह एक आवाज परीक्षण है।"),
        
        # Spanish voices
        ("es-ES-AlvaroNeural", "Alvaro (Spanish Male)", "Spanish", "Hola, esta es una prueba de voz."),
        ("es-ES-ElviraNeural", "Elvira (Spanish Female)", "Spanish", "Hola, esta es una prueba de voz."),
        ("es-MX-DaliaNeural", "Dalia (Mexican Female)", "Spanish", "Hola, esta es una prueba de voz."),
        
        # French voices
        ("fr-FR-DeniseNeural", "Denise (French Female)", "French", "Bonjour, ceci est un test vocal."),
        ("fr-FR-HenriNeural", "Henri (French Male)", "French", "Bonjour, ceci est un test vocal."),
        
        # German voices
        ("de-DE-KatjaNeural", "Katja (German Female)", "German", "Hallo, das ist ein Sprachtest."),
        ("de-DE-ConradNeural", "Conrad (German Male)", "German", "Hallo, das ist ein Sprachtest."),
        
        # Italian voices
        ("it-IT-ElsaNeural", "Elsa (Italian Female)", "Italian", "Ciao, questo è un test vocale."),
        ("it-IT-DiegoNeural", "Diego (Italian Male)", "Italian", "Ciao, questo è un test vocale."),
        
        # Portuguese voices
        ("pt-BR-FranciscaNeural", "Francisca (Brazilian Female)", "Portuguese", "Olá, este é um teste de voz."),
        ("pt-BR-AntonioNeural", "Antonio (Brazilian Male)", "Portuguese", "Olá, este é um teste de voz."),
        
        # Japanese voices
        ("ja-JP-NanamiNeural", "Nanami (Japanese Female)", "Japanese", "こんにちは、これは音声テストです。"),
        ("ja-JP-KeitaNeural", "Keita (Japanese Male)", "Japanese", "こんにちは、これは音声テストです。"),
        
        # Chinese voices
        ("zh-CN-XiaoxiaoNeural", "Xiaoxiao (Chinese Female)", "Chinese", "你好，这是语音测试。"),
        ("zh-CN-YunxiNeural", "Yunxi (Chinese Male)", "Chinese", "你好，这是语音测试。"),
        
        # Arabic voices
        ("ar-SA-ZariyahNeural", "Zariyah (Arabic Female)", "Arabic", "مرحبا، هذا اختبار صوتي."),
        ("ar-SA-HamedNeural", "Hamed (Arabic Male)", "Arabic", "مرحبا، هذا اختبار صوتي."),
        
        # Korean voices
        ("ko-KR-SunHiNeural", "SunHi (Korean Female)", "Korean", "안녕하세요, 이것은 음성 테스트입니다."),
        ("ko-KR-InJoonNeural", "InJoon (Korean Male)", "Korean", "안녕하세요, 이것은 음성 테스트입니다."),
        
        # Russian voices
        ("ru-RU-SvetlanaNeural", "Svetlana (Russian Female)", "Russian", "Привет, это голосовой тест."),
        ("ru-RU-DmitryNeural", "Dmitry (Russian Male)", "Russian", "Привет, это голосовой тест."),
    ]
    
    working_voices = {}
    
    for voice_id, voice_name, language, test_text in multilang_voices:
        if language not in working_voices:
            working_voices[language] = []
            
        if test_multilang_voice(voice_id, voice_name, language, test_text):
            working_voices[language].append((voice_id, voice_name))
    
    print("\n" + "=" * 80)
    print("🌍 SUMMARY OF WORKING MULTI-LANGUAGE VOICES:")
    print("=" * 80)
    
    total_working = 0
    for language, voices in working_voices.items():
        if voices:  # Only show languages with working voices
            print(f"\n{language} ({len(voices)} working):")
            for voice_id, voice_name in voices:
                print(f"  ✅ {voice_name} - {voice_id}")
            total_working += len(voices)
    
    print(f"\n🎯 Total working multi-language voices: {total_working}")
    return working_voices

if __name__ == "__main__":
    working_multilang_voices = test_multilanguage_voices()
