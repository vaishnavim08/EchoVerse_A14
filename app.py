import streamlit as st
import base64
from ai_services import AIServices
from config import VOICE_IDS
import io
from ui import render_theme_and_background, nav, header

# Page configuration
st.set_page_config(
    page_title="EchoVerse - AI Audiobook Creator",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

render_theme_and_background()

# Initialize page in session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

page = st.session_state.page
nav(page)
header()

if (page == "Home"):
    # Feature highlights with 3D effects
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    with col_feat1:
        st.markdown("""
        <div class="feature-highlight">
            <h3>🎭 Tone Transformation</h3>
            <p>AI-powered text rewriting in multiple emotional tones</p>
        </div>
        """, unsafe_allow_html=True)
    with col_feat2:
        st.markdown("""
        <div class="feature-highlight">
            <h3>🎵 Voice Synthesis</h3>
            <p>Natural-sounding narration with multiple voice options</p>
        </div>
        """, unsafe_allow_html=True)
    with col_feat3:
        st.markdown("""
        <div class="feature-highlight">
            <h3>💾 Instant Download</h3>
            <p>Get your audiobooks in MP3 format immediately</p>
        </div>
        """, unsafe_allow_html=True)

# Initialize AI services
@st.cache_resource
def init_ai_services():
    """Initialize AI services once and cache them"""
    ai_services = AIServices()
    # Note: Model loading will happen on first use to avoid blocking the UI
    return ai_services

# Initialize AI services
ai_services = init_ai_services()

with st.container():
    if page == "About":
        st.markdown('<div class="section-header">🌟 About EchoVerse</div>', unsafe_allow_html=True)
        st.markdown("## 🎧 Welcome to EchoVerse - The Future of Audiobook Creation")
        
        st.write("**EchoVerse** is a revolutionary AI-powered platform that transforms any text into captivating audiobooks with professional-quality narration. Our cutting-edge technology combines advanced artificial intelligence with Azure's world-class text-to-speech capabilities to deliver an unparalleled audiobook creation experience.")
        
        st.markdown("### 🌍 Global Reach, Local Touch")
        st.write("Break language barriers with our comprehensive multilingual support spanning **13 languages** including English, Hindi, Telugu, Spanish, French, German, Italian, Portuguese, Japanese, Chinese, Arabic, Korean, and Russian. Each language features native voice options with authentic pronunciation and cultural nuances.")
        
        st.markdown("### 🎭 Emotional Intelligence")
        st.write("Our AI doesn't just read - it understands context and emotion. Choose from **7 distinct narrative tones**:")
        st.write("• **Storytelling** - Enchanting narratives that captivate listeners")
        st.write("• **Suspenseful** - Edge-of-your-seat thriller delivery")
        st.write("• **Inspiring** - Motivational content that energizes")
        st.write("• **Humorous** - Light-hearted and entertaining")
        st.write("• **Authoritative** - Professional and commanding")
        st.write("• **Blog to Podcast** - Conversational and engaging")
        st.write("• **Neutral** - Clear and balanced narration")
        
        st.markdown("### 🎤 Premium Voice Collection")
        st.write("Select from our curated collection of **25+ premium voices** featuring male, female, and specialized options. Each voice is carefully chosen for clarity, warmth, and professional quality to ensure your audiobooks sound exceptional.")
        
        st.markdown("### 🚀 Powered by Advanced AI")
        st.write("EchoVerse leverages the **IBM Granite 13B** language model for intelligent text rewriting and **Azure Cognitive Services** for crystal-clear speech synthesis. This powerful combination ensures your content is not just converted, but enhanced and optimized for audio consumption.")
        
        st.markdown("### ⚡ Instant Results")
        st.write("From upload to download in minutes. Our streamlined workflow processes your content efficiently while maintaining the highest quality standards. Get your audiobook, rewritten text, and complete transcript ready for immediate use.")
        
        st.markdown("### 🎯 Perfect For")
        st.write("• **Authors & Publishers** - Convert books into audiobooks")
        st.write("• **Content Creators** - Transform blogs into podcasts")
        st.write("• **Educators** - Create engaging learning materials")
        st.write("• **Businesses** - Develop training content and presentations")
        st.write("• **Language Learners** - Practice with native pronunciation")
        
        st.markdown("### 🌟 Why Choose EchoVerse?")
        st.write("**Innovation meets simplicity.** We've eliminated the complexity of traditional audiobook production while maintaining professional standards. No recording studios, no expensive equipment, no lengthy production cycles - just upload, customize, and download.")
        
        st.write("*Experience the future of audiobook creation. Transform your words into voices that resonate across cultures and languages.*")
    elif page == "Contact":
        st.markdown('<div class="section-header">📞 Contact Us</div>', unsafe_allow_html=True)
        
        st.markdown("## 👥 Meet the EchoVerse Team")
        st.write("Get in touch with our development team for support, feedback, or collaboration opportunities.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 👩‍💻 Adithi Garipelly")
            st.write("**Lead Developer**")
            st.write("📧 adithigaripelly@gmail.com")
            st.write("Specializes in AI integration and backend development")
        
        with col2:
            st.markdown("### 👩‍💻 Vaishnavi Motlakunta")
            st.write("**AI Engineer**")
            st.write("📧 motlakuntavaishnavi@gmail.com")
            st.write("Expert in machine learning and speech synthesis")
        
        with col3:
            st.markdown("### 👩‍💻 Harisha Toomu")
            st.write("**Frontend Developer**")
            st.write("📧 toomuharisha@gmail.com")
            st.write("UI/UX design and user experience optimization")
        
        st.markdown("---")
        
        st.markdown("### 🚀 Project Information")
        st.write("**EchoVerse** - AI-Powered Multilingual Audiobook Creator")
        st.write("Built with Streamlit, Azure Cognitive Services, and IBM Granite AI")
        st.write("Supporting 13 languages with 25+ premium voices")
        
        st.markdown("### 💬 Get in Touch")
        st.write("• For technical support or bug reports")
        st.write("• Feature requests and suggestions")
        st.write("• Partnership and collaboration inquiries")
        st.write("• General feedback about EchoVerse")
        
        st.info("We're passionate about making audiobook creation accessible to everyone. Reach out to us - we'd love to hear from you!")
    elif page == "History":
        st.markdown('<div class="section-header">📚 Past Narrations</div>', unsafe_allow_html=True)
        with st.expander("View your session history", expanded=True):
            if 'narrations' not in st.session_state:
                st.session_state.narrations = []
            if not st.session_state.narrations:
                st.markdown('<div class="info-box">No narrations generated yet. Create your first audiobook on Home/Customization.</div>', unsafe_allow_html=True)
            else:
                for i, narration in enumerate(st.session_state.narrations):
                    st.markdown('<div class="card-container">', unsafe_allow_html=True)
                    st.markdown(f"**Narration {i+1}** - {narration['tone']} tone, {narration['voice']} voice")
                    st.text_area(f"Rewritten Text {i+1}", value=narration['rewritten_text'], height=80, disabled=True)
                    
                    # Audio playback if available
                    if 'audio_data' in narration and narration['audio_data']:
                        st.markdown("🎧 **Audio Player**")
                        st.audio(narration['audio_data'], format="audio/mp3")
                    else:
                        st.info("Audio not available for this narration")
                    
                    col9, col10 = st.columns([1, 1])
                    with col10:
                        if 'audio_data' in narration and narration['audio_data']:
                            st.download_button(
                                label=f"📥 Download MP3 {i+1}",
                                data=narration['audio_data'],
                                file_name=f"echoverse_{narration['tone'].lower()}_{narration['voice'].lower()}_{i+1}.mp3",
                                mime="audio/mpeg",
                                key=f"download_{i}"
                            )
                        else:
                            st.write("Download not available")
                    st.markdown('</div>', unsafe_allow_html=True)
    elif page == "Customization":
        # fall through to the same controls and generation UI below
        pass
    else:
        # Home page
        pass
    if page == "Home":
        st.markdown('<div class="section-header">📝 Input Your Text</div>', unsafe_allow_html=True)
        # Create two columns for input methods
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<div style="vertical-align: top;">', unsafe_allow_html=True)
            st.markdown('<span class="attractive-label">📁 Option 1: Upload Text File</span>', unsafe_allow_html=True)
            uploaded_file = st.file_uploader(
                "Choose a .txt file",
                type=['txt'],
                help="Upload a text file (max 200MB)"
            )
            
            if uploaded_file is not None:
                try:
                    content = uploaded_file.read().decode('utf-8')
                    st.markdown(f'<div class="success-box">✅ File uploaded successfully! ({len(content)} characters)</div>', unsafe_allow_html=True)
                    # Store content in session state
                    st.session_state.uploaded_content = content
                except Exception as e:
                    st.error(f"❌ Error reading file: {str(e)}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div style="vertical-align: top;">', unsafe_allow_html=True)
            st.markdown('<span class="attractive-label">✍️ Option 2: Paste Text Directly</span>', unsafe_allow_html=True)
            manual_text = st.text_area(
                "Text Input",
                height=150,
                placeholder="Enter or paste your text here...",
                help="Type or paste your text content directly",
                label_visibility="collapsed"
            )
            
            if manual_text:
                st.session_state.manual_content = manual_text
            st.markdown('</div>', unsafe_allow_html=True)

        # Next button to go to Customization page
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        if st.button("Next", type="primary", use_container_width=True):
            st.session_state.page = "Customization"
            st.rerun()

    # Initialize default values
    selected_tone = "Neutral"
    selected_voice = "Neutral"
    
    if page == "Customization":
        st.markdown('<div class="section-header">🎭 Customize Your Narration</div>', unsafe_allow_html=True)
        col3, col4, col5 = st.columns([1, 1, 1])
        
        with col3:
            st.markdown('<span class="attractive-label">🌍 Select Language</span>', unsafe_allow_html=True)
            st.markdown('<span class="attractive-subtext">Choose your preferred language</span>', unsafe_allow_html=True)
            language_options = list(VOICE_IDS.keys())
            selected_language = st.selectbox(
                "Choose the language:",
                language_options,
                help="Select the language for voice synthesis"
            )
            
        with col4:
            st.markdown('<span class="attractive-label">🎭 Select Tone</span>', unsafe_allow_html=True)
            st.markdown('<span class="attractive-subtext">Choose the emotional style for your narration</span>', unsafe_allow_html=True)
            tone_options = ["Neutral", "Inspiring", "Suspenseful", "Humorous", "Authoritative", "Blog to Podcast", "Storytelling"]
            selected_tone = st.selectbox(
                "Choose the tone for your narration:",
                tone_options,
                help="The tone will affect how your text is rewritten"
            )
            
        with col5:
            st.markdown('<span class="attractive-label">🎵 Select Voice</span>', unsafe_allow_html=True)
            st.markdown('<span class="attractive-subtext">Pick the perfect voice for your story</span>', unsafe_allow_html=True)
            # Get voices for selected language
            voice_options = list(VOICE_IDS[selected_language].keys())
            selected_voice = st.selectbox(
                "🎤 Select Voice:",
                voice_options,
                key="voice_selection"
            )
            
    
    generate_button = False
    if page == "Customization":
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        generate_button = st.button("🎬 Generate Audiobook", type="secondary", use_container_width=True, help="Click to start the AI-powered audiobook generation process")
    
    if page == "Customization" and ('uploaded_content' in st.session_state or 'manual_content' in st.session_state):
        current_content = st.session_state.get('uploaded_content', '') or st.session_state.get('manual_content', '')
        
        if current_content:
            st.markdown('<div class="section-header">📋 Content Preview</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-container">', unsafe_allow_html=True)
            st.text_area("Your input text:", value=current_content, height=100, disabled=True)
            st.markdown(f'<div class="info-box">🎯 **Selected Settings:** Language: {selected_language} | Tone: {selected_tone} | Voice: {selected_voice}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    

    
    if page == "Customization" and generate_button and ('uploaded_content' in st.session_state or 'manual_content' in st.session_state):
        current_content = st.session_state.get('uploaded_content', '') or st.session_state.get('manual_content', '')
        
        # Show section header only when generating
        st.markdown('<div class="section-header">📖 Original vs Rewritten Text</div>', unsafe_allow_html=True)
        
        # AI Text Rewriting
        with st.spinner("🤖 AI is rewriting your text..."):
            try:
                # Load model if not already loaded
                if not ai_services.model:
                    with st.spinner("🔄 Loading AI model (first time only)..."):
                        ai_services.load_granite_model()
                
                # Rewrite text with selected tone and language
                rewritten_text = ai_services.rewrite_text_with_tone(current_content, selected_tone, selected_language)
                
                # Handle tuple return from rewrite function
                if isinstance(rewritten_text, tuple):
                    rewritten_text = rewritten_text[0] if rewritten_text[0] else "Error in text rewriting"
                
                st.markdown('<div class="success-box">✅ Text rewriting completed!</div>', unsafe_allow_html=True)
                
                # Store in session state for later use
                st.session_state.rewritten_text = rewritten_text
                st.session_state.original_text = current_content
                    
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
                rewritten_text = f"[AI would rewrite your text in a {selected_tone.lower()} tone here]"
        
        # Display side by side comparison
        col5, col6 = st.columns([1, 1])
        
        with col5:
            st.markdown('<div class="card-container">', unsafe_allow_html=True)
            st.markdown("**Original Text**")
            st.text_area("Original:", value=current_content, height=200, disabled=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col6:
            st.markdown('<div class="card-container">', unsafe_allow_html=True)
            st.markdown("**AI-Rewritten Text**")
            st.text_area("Rewritten:", value=rewritten_text, height=200, disabled=True)
            st.markdown('</div>', unsafe_allow_html=True)

    

    
    if page == "Customization" and generate_button and ('uploaded_content' in st.session_state or 'manual_content' in st.session_state) and 'rewritten_text' in st.session_state:
        # Show section header only when generating audio
        st.markdown('<div class="section-header">🎵 Audio Playback</div>', unsafe_allow_html=True)
        
        # Generate audio using Azure TTS
        with st.spinner("🎵 Generating audio with Azure TTS..."):
            try:
                # Get the voice ID for the selected voice and language
                voice_id = VOICE_IDS[selected_language][selected_voice]
                audio_data, error = ai_services.generate_speech_azure(st.session_state.rewritten_text, voice_id)
                
                if error:
                    st.error(f"❌ Error in audio generation: {error}")
                    st.markdown('<div class="card-container">', unsafe_allow_html=True)
                    st.markdown("🎧 **Audio generation failed**")
                    st.markdown('<div class="info-box">Please try again or check your Azure credentials</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="success-box">✅ Audio generation completed!</div>', unsafe_allow_html=True)
                    
                    # Store audio data in session state
                    st.session_state.audio_data = audio_data
                    
                    # Audio player section
                    st.markdown('<div class="audio-section">', unsafe_allow_html=True)
                    st.markdown("🎧 **Audio Player**")
                    st.audio(audio_data, format="audio/mp3")
                    st.markdown('<div class="info-box">Audio generated using Azure Cognitive Services TTS</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"❌ Unexpected error in audio generation: {str(e)}")
                st.markdown('<div class="card-container">', unsafe_allow_html=True)
                st.markdown("🎧 **Audio generation failed**")
                st.markdown('<div class="info-box">Please try again later</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

    

    
    if page == "Customization" and generate_button and ('uploaded_content' in st.session_state or 'manual_content' in st.session_state) and 'rewritten_text' in st.session_state:
        # Show section header only when generating downloads
        st.markdown('<div class="section-header">💾 Download Options</div>', unsafe_allow_html=True)
        
        col7, col8, col9 = st.columns([1, 1, 1])
        
        with col7:
            if 'audio_data' in st.session_state and st.session_state.audio_data:
                st.download_button(
                    label="📥 Download MP3",
                    data=st.session_state.audio_data,
                    file_name=f"echoverse_{selected_tone.lower()}_{selected_voice.lower()}.mp3",
                    mime="audio/mpeg",
                    help="Download the generated audio as MP3 file"
                )
        
        with col8:
            if 'rewritten_text' in st.session_state and st.session_state.rewritten_text:
                st.download_button(
                    label="📄 Download Rewritten Text",
                    data=st.session_state.rewritten_text,
                    file_name=f"echoverse_{selected_tone.lower()}_rewritten.txt",
                    mime="text/plain",
                    help="Download the AI-rewritten text"
                )
            
        with col9:
            if 'rewritten_text' in st.session_state and 'original_text' in st.session_state:
                # Create transcript
                transcript = ai_services.create_audiobook_transcript(
                    st.session_state.original_text,
                    st.session_state.rewritten_text,
                    selected_tone,
                    selected_voice
                )
                st.download_button(
                    label="📚 Download Transcript",
                    data=transcript,
                    file_name=f"echoverse_{selected_tone.lower()}_transcript.md",
                    mime="text/markdown",
                    help="Download the complete transcript with production notes"
                )

    
    # Append to history when generated successfully (only if audio was created)
    if page in ("Customization", "Home") and generate_button and ('uploaded_content' in st.session_state or 'manual_content' in st.session_state) and 'rewritten_text' in st.session_state and 'audio_data' in st.session_state and st.session_state.audio_data:
        if 'narrations' not in st.session_state:
            st.session_state.narrations = []
        new_narration = {
            'tone': selected_tone,
            'voice': selected_voice,
            'rewritten_text': st.session_state.rewritten_text,
            'audio_data': st.session_state.get('audio_data', None),
            'timestamp': st.session_state.get('timestamp', 0) + 1
        }
        st.session_state.narrations.append(new_narration)
        st.session_state.timestamp = new_narration['timestamp']

# Footer with SoulSound-inspired design and 3D effects
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <p>🎧 EchoVerse - Transforming Text into Expressive Audio with AI</p>
    <p style="font-size: 0.9rem; opacity: 0.7; margin-top: 0.5rem;">
        "Let the vibrations of words become the music of your soul"
    </p>
</div>
""", unsafe_allow_html=True)
