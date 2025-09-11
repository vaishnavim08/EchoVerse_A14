# Configuration file for EchoVerse API credentials and settings

# Hugging Face API Token for IBM Granite
import os
HUGGINGFACE_API_TOKEN = os.getenv('HF_TOKEN')

# Gemini configuration
USE_GEMINI = True
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_MODEL_NAME = "gemini-2.5-flash"
# Azure Cognitive Services Speech API
AZURE_SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY')
AZURE_SPEECH_ENDPOINT = "https://centralindia.api.cognitive.microsoft.com/"
AZURE_SPEECH_REGION = "centralindia"

# IBM Granite Model Configuration
# We'll try these identifiers in order until one loads successfully
GRANITE_MODEL_CANDIDATES = [
    "ibm-granite/granite-3.3-8b-instruct"
]
GRANITE_MODEL_NAME = GRANITE_MODEL_CANDIDATES[0]

# Use Hugging Face Inference API instead of local model download
USE_HF_INFERENCE = False
MAX_TOKENS = 2000
TEMPERATURE = 0.7

# No fallback model – use only Granite Inference API
HF_FALLBACK_MODEL = ""

# Voice IDs organized by language (tested and working in Central India region)
VOICE_IDS = {
    "English": {
        # Female Voices
        "Jenny (US Female)": "en-US-JennyNeural",
        "Aria (US Female)": "en-US-AriaNeural",
        "Neerja (IN Female)": "en-IN-NeerjaNeural",
        
        # Male Voices  
        "Tony (US Male)": "en-US-TonyNeural",
        "William (AU Male)": "en-AU-WilliamNeural",
        
        # Child Voices
        "Ana (US Child)": "en-US-AnaNeural",
        "Maisie (UK Child)": "en-GB-MaisieNeural"
    },
    
    "Hindi": {
        "Madhur (Hindi Male)": "hi-IN-MadhurNeural",
        "Swara (Hindi Female)": "hi-IN-SwaraNeural"
    },
    
    "Spanish": {
        "Alvaro (Spanish Male)": "es-ES-AlvaroNeural",
        "Elvira (Spanish Female)": "es-ES-ElviraNeural",
        "Dalia (Mexican Female)": "es-MX-DaliaNeural"
    },
    
    "French": {
        "Denise (French Female)": "fr-FR-DeniseNeural",
        "Henri (French Male)": "fr-FR-HenriNeural"
    },
    
    "German": {
        "Katja (German Female)": "de-DE-KatjaNeural",
        "Conrad (German Male)": "de-DE-ConradNeural"
    },
    
    "Italian": {
        "Elsa (Italian Female)": "it-IT-ElsaNeural",
        "Diego (Italian Male)": "it-IT-DiegoNeural"
    },
    
    "Portuguese": {
        "Francisca (Brazilian Female)": "pt-BR-FranciscaNeural",
        "Antonio (Brazilian Male)": "pt-BR-AntonioNeural"
    },
    
    "Japanese": {
        "Nanami (Japanese Female)": "ja-JP-NanamiNeural",
        "Keita (Japanese Male)": "ja-JP-KeitaNeural"
    },
    
    "Chinese": {
        "Xiaoxiao (Chinese Female)": "zh-CN-XiaoxiaoNeural",
        "Yunxi (Chinese Male)": "zh-CN-YunxiNeural"
    },
    
    "Arabic": {
        "Zariyah (Arabic Female)": "ar-SA-ZariyahNeural",
        "Hamed (Arabic Male)": "ar-SA-HamedNeural"
    },
    
    "Korean": {
        "SunHi (Korean Female)": "ko-KR-SunHiNeural",
        "InJoon (Korean Male)": "ko-KR-InJoonNeural"
    },
    
    "Russian": {
        "Svetlana (Russian Female)": "ru-RU-SvetlanaNeural",
        "Dmitry (Russian Male)": "ru-RU-DmitryNeural"
    },
    
    "Telugu": {
        "Shruti (Telugu Female)": "te-IN-ShrutiNeural",
        "Mohan (Telugu Male)": "te-IN-MohanNeural"
    }
}

# Language-specific tone prompt templates
def get_tone_prompt(tone, language):
    """Get tone prompt in the specified language"""
    
    # Base prompts in different languages
    language_prompts = {
        "English": {
            "Neutral": "Rewrite the following text in a neutral, professional tone while preserving all factual information and maintaining clarity:\n\n{text}\n\nRequirements:\n- Use clear, straightforward language\n- Maintain professional tone\n- Keep all key information intact\n- Ensure readability for general audience",
            
            "Inspiring": "Transform the following text into an inspiring, motivational narrative that uplifts and energizes the reader:\n\n{text}\n\nRequirements:\n- Add motivational language and positive framing\n- Include inspiring metaphors or analogies\n- Maintain the core message while making it uplifting\n- Use language that creates emotional connection\n- Add calls to action or empowering statements",
            
            "Suspenseful": "Rewrite the following text in a suspenseful, dramatic tone that builds tension and keeps the audience engaged:\n\n{text}\n\nRequirements:\n- Add dramatic pacing and tension-building elements\n- Use cliffhangers and suspenseful language\n- Include descriptive details that create atmosphere\n- Maintain the core narrative while adding dramatic flair\n- Create anticipation and curiosity",

            "Humorous": "Transform the following text into a humorous, entertaining version that makes the content engaging and fun to read:\n\n{text}\n\nRequirements:\n- Add witty observations and light humor\n- Include funny analogies or comparisons\n- Use playful language while keeping the core message\n- Add amusing anecdotes or examples\n- Maintain respect for the subject matter while making it entertaining",

            "Authoritative": "Rewrite the following text in an authoritative, expert tone that establishes credibility and commands respect:\n\n{text}\n\nRequirements:\n- Use confident, decisive language\n- Include expert terminology and insights\n- Present information with authority and conviction\n- Add supporting evidence or expert perspectives\n- Maintain professional credibility throughout",

            "Blog to Podcast": "Transform the following blog text into a conversational podcast script that feels natural when spoken aloud:\n\n{text}\n\nRequirements:\n- Convert written language to spoken, conversational style\n- Add natural transitions and verbal cues\n- Include direct audience address ('you', 'listeners')\n- Add pauses, emphasis, and speaking rhythm\n- Make it sound like a natural conversation with the audience",

            "Storytelling": "Transform the following text into an engaging, captivating story that draws listeners in with vivid imagery and narrative flow:\n\n{text}\n\nRequirements:\n- Use descriptive, imaginative language that paints pictures\n- Add narrative elements like 'Once upon a time' or 'Let me tell you about'\n- Include emotional expressions and character voices\n- Create a sense of wonder and engagement\n- Use pacing that builds excitement and maintains attention\n- Make it feel like a bedtime story or campfire tale"
        },
        
        "Hindi": {
            "Neutral": "निम्नलिखित पाठ को तटस्थ, व्यावसायिक स्वर में फिर से लिखें और सभी तथ्यात्मक जानकारी को संरक्षित करते हुए स्पष्टता बनाए रखें। आउटपुट हिंदी में होना चाहिए:\n\n{text}\n\nआवश्यकताएं:\n- स्पष्ट, सीधी भाषा का उपयोग करें\n- व्यावसायिक स्वर बनाए रखें\n- सभी मुख्य जानकारी को बरकरार रखें\n- सामान्य दर्शकों के लिए पठनीयता सुनिश्चित करें",
            
            "Inspiring": "निम्नलिखित पाठ को एक प्रेरणादायक, प्रेरक कथा में बदलें जो पाठक को उत्साहित करे। आउटपुट हिंदी में होना चाहिए:\n\n{text}\n\nआवश्यकताएं:\n- प्रेरणादायक भाषा और सकारात्मक दृष्टिकोण जोड़ें\n- प्रेरणादायक रूपक या उपमाएं शामिल करें\n- मुख्य संदेश को बनाए रखते हुए इसे उत्साहजनक बनाएं\n- भावनात्मक संबंध बनाने वाली भाषा का उपयोग करें",
            
            "Storytelling": "निम्नलिखित पाठ को एक आकर्षक, मनमोहक कहानी में बदलें जो श्रोताओं को जीवंत कल्पना के साथ आकर्षित करे। आउटपुट हिंदी में होना चाहिए:\n\n{text}\n\nआवश्यकताएं:\n- वर्णनात्मक, कल्पनाशील भाषा का उपयोग करें\n- 'एक बार की बात है' जैसे कथा तत्व जोड़ें\n- भावनात्मक अभिव्यक्ति और चरित्र आवाजें शामिल करें\n- आश्चर्य और जुड़ाव की भावना पैदा करें"
        },
        
        "Spanish": {
            "Neutral": "Reescribe el siguiente texto en un tono neutral y profesional, preservando toda la información factual y manteniendo la claridad. La salida debe estar en español:\n\n{text}\n\nRequisitos:\n- Usar lenguaje claro y directo\n- Mantener tono profesional\n- Conservar toda la información clave\n- Asegurar legibilidad para audiencia general",
            
            "Inspiring": "Transforma el siguiente texto en una narrativa inspiradora y motivacional que eleve y energice al lector. La salida debe estar en español:\n\n{text}\n\nRequisitos:\n- Añadir lenguaje motivacional y enfoque positivo\n- Incluir metáforas o analogías inspiradoras\n- Mantener el mensaje central mientras lo haces edificante\n- Usar lenguaje que cree conexión emocional",
            
            "Storytelling": "Transforma el siguiente texto en una historia cautivadora que atraiga a los oyentes con imágenes vívidas y flujo narrativo. La salida debe estar en español:\n\n{text}\n\nRequisitos:\n- Usar lenguaje descriptivo e imaginativo\n- Añadir elementos narrativos como 'Érase una vez'\n- Incluir expresiones emocionales y voces de personajes\n- Crear sensación de asombro y compromiso"
        },
        
        "French": {
            "Neutral": "Réécrivez le texte suivant dans un ton neutre et professionnel en préservant toutes les informations factuelles et en maintenant la clarté. La sortie doit être en français:\n\n{text}\n\nExigences:\n- Utiliser un langage clair et direct\n- Maintenir un ton professionnel\n- Conserver toutes les informations clés\n- Assurer la lisibilité pour le grand public",
            
            "Storytelling": "Transformez le texte suivant en une histoire captivante qui attire les auditeurs avec des images vives et un flux narratif. La sortie doit être en français:\n\n{text}\n\nExigences:\n- Utiliser un langage descriptif et imaginatif\n- Ajouter des éléments narratifs comme 'Il était une fois'\n- Inclure des expressions émotionnelles et des voix de personnages\n- Créer un sentiment d'émerveillement et d'engagement"
        },
        
        "Telugu": {
            "Neutral": "కింది వచనాన్ని తటస్థ, వృత్తిపరమైన స్వరంలో తిరిగి వ్రాయండి మరియు అన్ని వాస్తవిక సమాచారాన్ని భద్రపరచుతూ స్పష్టతను కొనసాగించండి. అవుట్‌పుట్ తెలుగులో ఉండాలి:\n\n{text}\n\nఅవసరాలు:\n- స్పష్టమైన, సరళమైన భాషను ఉపయోగించండి\n- వృత్తిపరమైన స్వరాన్ని కొనసాగించండి\n- అన్ని ముఖ్య సమాచారాన్ని భద్రపరచండి\n- సాధారణ ప్రేక్షకులకు చదవగలిగేలా చేయండి",
            
            "Inspiring": "కింది వచనాన్ని ప్రేరణాదాయకమైన, ప్రేరేపిత కథనంగా మార్చండి, ఇది పాఠకులను ఉత్తేజపరుస్తుంది మరియు శక్తిని ఇస్తుంది. అవుట్‌పుట్ తెలుగులో ఉండాలి:\n\n{text}\n\nఅవసరాలు:\n- ప్రేరణాదాయక భాష మరియు సానుకూల దృక్పథాన్ని జోడించండి\n- ప్రేరణాదాయక రూపకాలు లేదా సారూప్యతలను చేర్చండి\n- ప్రధాన సందేశాన్ని కొనసాగిస్తూ దానిని ఉత్తేజకరంగా చేయండి\n- భావోద్వేగ సంబంధాన్ని సృష్టించే భాషను ఉపయోగించండి",
            
            "Storytelling": "కింది వచనాన్ని ఆకర్షణీయమైన, మనోహరమైన కథగా మార్చండి, ఇది వినేవారిని స్పష్టమైన చిత్రణ మరియు కథా ప్రవాహంతో ఆకర్షిస్తుంది. అవుట్‌పుట్ తెలుగులో ఉండాలి:\n\n{text}\n\nఅవసరాలు:\n- వర్ణనాత్మక, ఊహాత్మక భాషను ఉపయోగించండి\n- 'ఒకప్పుడు' వంటి కథా అంశాలను జోడించండి\n- భావోద్వేగ వ్యక్తీకరణలు మరియు పాత్రల స్వరాలను చేర్చండి\n- ఆశ్చర్యం మరియు నిమగ్నత యొక్క భావనను సృష్టించండి"
        }
    }
    
    # For languages not fully implemented, use English with language instruction
    if language not in language_prompts:
        base_prompt = language_prompts["English"].get(tone, language_prompts["English"]["Neutral"])
        return f"Translate and rewrite the following text to {language} language with a {tone.lower()} tone:\n\n{{text}}\n\nIMPORTANT: The output must be entirely in {language}, not English."
    
    return language_prompts[language].get(tone, language_prompts[language].get("Neutral", language_prompts["English"]["Neutral"]))

# Backward compatibility - keep original TONE_PROMPTS for English
TONE_PROMPTS = {
    "Neutral": get_tone_prompt("Neutral", "English"),
    "Inspiring": get_tone_prompt("Inspiring", "English"),
    "Suspenseful": get_tone_prompt("Suspenseful", "English"),
    "Humorous": get_tone_prompt("Humorous", "English"),
    "Authoritative": get_tone_prompt("Authoritative", "English"),
    "Blog to Podcast": get_tone_prompt("Blog to Podcast", "English"),
    "Storytelling": get_tone_prompt("Storytelling", "English")
}
