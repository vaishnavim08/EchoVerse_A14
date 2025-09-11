# 🎧 EchoVerse - AI-Powered Audiobook Creation Tool

EchoVerse is a generative AI-based audiobook creation system that transforms user-provided text into expressive, downloadable audio content. Built with Streamlit, IBM Granite 13B, and Azure Cognitive Services.

## ✨ Features

- **🎭 AI Text Rewriting**: Transform text into Neutral, Inspiring, or Suspenseful tones using IBM Granite 13B
- **🎵 High-Quality TTS**: Generate natural-sounding audio using Azure Cognitive Services
- **📁 Multiple Input Methods**: Upload .txt files or paste text directly
- **💾 Instant Downloads**: Get MP3 audio, rewritten text, and production transcripts
- **🎨 Beautiful 3D UI**: Modern, gamified interface with animations and effects
- **📚 Session History**: Track and replay all generated narrations

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys
Create a `config.py` file with your credentials:
```python
# Hugging Face API Token for IBM Granite 13B
HUGGINGFACE_API_TOKEN = "your_hf_token_here"

# Azure Cognitive Services Speech API
AZURE_SPEECH_KEY = "your_azure_key_here"
AZURE_SPEECH_REGION = "your_azure_region"
AZURE_SPEECH_ENDPOINT = "your_azure_endpoint"
```

### 3. Run the Application
```bash
streamlit run app.py
```

## 🔑 API Setup

### Hugging Face
1. Create account at [huggingface.co](https://huggingface.co)
2. Generate API token in Settings → Access Tokens
3. Use token to access IBM Granite models

### Azure Cognitive Services
1. Create Azure account
2. Set up Speech Service resource
3. Get API key and endpoint from Azure portal

## 🎯 Usage

1. **Input Text**: Upload a .txt file or paste text directly
2. **Select Tone**: Choose Neutral, Inspiring, or Suspenseful
3. **Generate**: Click "Generate Audiobook" to rewrite text and create audio
4. **Download**: Get MP3 audio, rewritten text, and production transcript
5. **History**: View and replay all generated narrations

## 🏗️ Architecture

- **Frontend**: Streamlit with custom 3D CSS animations
- **Text Rewriting**: IBM Granite 13B via Hugging Face Transformers
- **Text-to-Speech**: Azure Cognitive Services Speech API
- **State Management**: Streamlit session state
- **File Handling**: In-memory processing with download capabilities

## 📁 Project Structure

```
EchoVerse/
├── app.py              # Main Streamlit application
├── ai_services.py      # AI services integration
├── config.py           # API credentials and configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎨 UI Features

- **3D Gamified Design**: Hover effects, animations, and depth
- **Responsive Layout**: Works on all screen sizes
- **Dark Theme**: SoulSound-inspired aesthetic with blue accents
- **Interactive Elements**: Hover states, loading animations, and feedback

## 🔧 Technical Details

### IBM Granite 13B
- **Model**: `ibm-granite/granite-13b-base`
- **Capabilities**: Tone-specific text rewriting
- **Optimization**: 16-bit precision, auto device mapping

### Azure TTS
- **Voices**: Jenny (Neutral), Tony (Inspiring), Guy (Suspenseful)
- **Quality**: 16kHz, 128kbps MP3 output
- **Features**: SSML support, multiple languages

## 📊 Performance

- **Text Rewriting**: 5-15 seconds (first time: 30-60 seconds for model loading)
- **Audio Generation**: 3-8 seconds depending on text length
- **Memory Usage**: ~8GB RAM for Granite 13B model
- **Storage**: In-memory processing, no temporary files

## 🚨 Troubleshooting

### Common Issues
1. **Model Loading Fails**: Check Hugging Face token and internet connection
2. **Audio Generation Fails**: Verify Azure credentials and region
3. **Memory Issues**: Ensure sufficient RAM for Granite 13B model

### Solutions
- Restart the application
- Check API key validity
- Verify network connectivity
- Monitor system resources

## 🔮 Future Enhancements

- **Voice Customization**: More voice options and accents
- **Batch Processing**: Handle multiple files simultaneously
- **Advanced Tones**: More emotional and style variations
- **Export Formats**: WAV, FLAC, and other audio formats
- **Cloud Integration**: Save projects to cloud storage

## 📄 License

This project is created for educational and hackathon purposes.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests!

---

**🎧 EchoVerse - Transforming Text into Expressive Audio with AI**
