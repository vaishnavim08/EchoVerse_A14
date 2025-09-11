import streamlit as st


def render_theme_and_background():
    # Inject the exact same CSS and animated background used in the current single-page app
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;600;800&family=Righteous:wght@400&family=Fredoka:wght@300;400;500;600;700&family=Exo+2:wght@300;400;500;600;700;800;900&display=swap');
:root { --font-primary:'Poppins','Segoe UI',Tahoma,Geneva,Verdana,sans-serif; --font-display:'Orbitron','Courier New',monospace; --font-fancy:'Righteous',cursive; --font-modern:'Fredoka',sans-serif; --font-tech:'Exo 2',sans-serif; }
.stApp { background: linear-gradient(135deg,#0a0a0a 0%,#1a1a2e 50%,#16213e 100%); color:#ffffff; overflow-x:hidden; }
.stApp::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;background:radial-gradient(circle at 20% 80%, rgba(74,144,226,0.1) 0%, transparent 50%),radial-gradient(circle at 80% 20%, rgba(74,144,226,0.1) 0%, transparent 50%),radial-gradient(circle at 40% 40%, rgba(74,144,226,0.05) 0%, transparent 50%);animation:waveFloat 20s ease-in-out infinite;z-index:-1}
.frequency-wave{position:fixed;bottom:0;left:0;width:100%;height:100px;background:linear-gradient(90deg,transparent 0%,rgba(74,144,226,0.3) 25%,rgba(74,144,226,0.6) 50%,rgba(74,144,226,0.3) 75%,transparent 100%);animation:waveMove 8s linear infinite;z-index:-1}
.frequency-wave:nth-child(2){animation-delay:-2s;opacity:.5;height:60px}
.frequency-wave:nth-child(3){animation-delay:-4s;opacity:.3;height:40px}
@keyframes waveMove{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}
@keyframes waveFloat{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-20px) rotate(1deg)}}
.particle{position:fixed;width:4px;height:4px;background:rgba(74,144,226,.6);border-radius:50%;animation:float 15s linear infinite;z-index:-1}
.particle:nth-child(1){left:10%;animation-delay:0s}.particle:nth-child(2){left:20%;animation-delay:2s}.particle:nth-child(3){left:30%;animation-delay:4s}.particle:nth-child(4){left:40%;animation-delay:6s}.particle:nth-child(5){left:50%;animation-delay:8s}.particle:nth-child(6){left:60%;animation-delay:10s}.particle:nth-child(7){left:70%;animation-delay:12s}.particle:nth-child(8){left:80%;animation-delay:14s}
@keyframes float{0%{transform:translateY(100vh) scale(0);opacity:0}10%{opacity:1}90%{opacity:1}100%{transform:translateY(-100px) scale(1);opacity:0}}
::-webkit-scrollbar{width:8px}::-webkit-scrollbar-track{background:#1a1a2e}::-webkit-scrollbar-thumb{background:#4a90e2;border-radius:4px}::-webkit-scrollbar-thumb:hover{background:#357abd}
.main-header{text-align:center;padding:3rem 0;background:linear-gradient(135deg,rgba(74,144,226,.1) 0%,rgba(26,26,46,.8) 100%);border-radius:20px;margin:1rem 0;backdrop-filter:blur(10px);border:1px solid rgba(74,144,226,.2);transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 20px 40px rgba(0,0,0,.3),0 0 30px rgba(74,144,226,.2)}
.main-header:hover{transform:translateY(-5px) rotateX(5deg);box-shadow:0 25px 50px rgba(0,0,0,.4),0 0 40px rgba(74,144,226,.3)}
.main-header h1{font-size:4rem;margin-bottom:.5rem;background:linear-gradient(135deg,#4a90e2 0%,#ffffff 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-weight:700;text-shadow:0 0 30px rgba(74,144,226,.5);animation:glowPulse 3s ease-in-out infinite}
@keyframes glowPulse{0%,100%{text-shadow:0 0 30px rgba(74,144,226,.5)}50%{text-shadow:0 0 50px rgba(74,144,226,.8)}}
.main-header p{font-size:1.3rem;margin:0;color:#b8c5d6;font-weight:300}
.section-header{color:#4a90e2;margin-top:2rem;margin-bottom:1rem;font-size:1.5rem;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-left:4px solid #4a90e2;padding-left:1rem;transform:perspective(1000px) rotateY(-5deg);transition:all .3s ease}
.section-header:hover{transform:perspective(1000px) rotateY(0) scale(1.05);color:#5ba0f2}
.attractive-label{font-family:var(--font-display)!important;font-weight:700!important;font-size:1.2rem!important;color:#8b5cf6!important;text-transform:uppercase!important;letter-spacing:1.5px!important;margin-bottom:.8rem!important;text-shadow:0 2px 4px rgba(139,92,246,.3)!important;transition:all .3s ease!important;display:block!important}
.attractive-label:hover{color:#a855f7!important;text-shadow:0 3px 6px rgba(139,92,246,.5)!important;transform:translateX(5px)!important}
.attractive-subtext{font-family:var(--font-modern)!important;font-weight:400!important;font-size:1rem!important;color:#b8c5d6!important;font-style:normal!important;margin-bottom:1rem!important;opacity:.9!important;transition:all .3s ease!important;line-height:1.4!important}
.attractive-subtext:hover{color:#fff!important;opacity:1!important}
.option-label{font-family:var(--font-display)!important;font-weight:700!important;font-size:1.1rem!important;color:#06b6d4!important;text-transform:uppercase!important;letter-spacing:1.5px!important;margin-bottom:1rem!important;text-shadow:0 2px 4px rgba(6,182,212,.4)!important;transition:all .3s ease!important;display:block!important;text-align:center!important}
.option-label:hover{color:#0891b2!important;text-shadow:0 3px 6px rgba(6,182,212,.6)!important;transform:scale(1.05)!important}
.card-container{background:rgba(26,26,46,.6);border-radius:15px;padding:1.5rem;margin:1rem 0;border:1px solid rgba(74,144,226,.2);backdrop-filter:blur(10px);transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 10px 20px rgba(0,0,0,.2),0 0 20px rgba(74,144,226,.1)}
.card-container:hover{transform:translateY(-5px) rotateX(2deg);box-shadow:0 15px 30px rgba(0,0,0,.3),0 0 30px rgba(74,144,226,.2);border-color:rgba(74,144,226,.4)}
.stTextArea textarea{background:rgba(10,10,10,.8)!important;border:2px solid rgba(74,144,226,.3)!important;border-radius:10px!important;color:#fff!important;font-size:14px!important;transition:all .3s ease!important}
.stTextArea textarea:focus{border-color:#4a90e2!important;box-shadow:0 0 20px rgba(74,144,226,.4)!important;transform:scale(1.02)!important}
.stFileUploader{background:rgba(26,26,46,.6);border-radius:10px;padding:1rem;border:2px dashed rgba(74,144,226,.4);transition:all .3s ease}
.stFileUploader:hover{border-color:rgba(74,144,226,.6);box-shadow:0 0 20px rgba(74,144,226,.2)}
.stSelectbox select{background:rgba(10,10,10,.8)!important;border:2px solid rgba(74,144,226,.3)!important;border-radius:8px!important;color:#fff!important;transition:all .3s ease!important}
.stSelectbox select:focus{border-color:#4a90e2!important;box-shadow:0 0 20px rgba(74,144,226,.4)!important;transform:scale(1.02)!important}
.stButton>button{background:linear-gradient(135deg,#4a90e2 0%,#357abd 100%)!important;border:none!important;border-radius:25px!important;color:white!important;font-weight:600!important;padding:.75rem 2rem!important;transition:all .3s ease!important;box-shadow:0 8px 25px rgba(74,144,226,.3),0 0 20px rgba(74,144,226,.2)!important;transform-style:preserve-3d!important;position:relative!important;overflow:hidden!important}
.stButton>button[data-testid="baseButton-secondary"]{background:linear-gradient(135deg,#ff6b6b 0%,#4ecdc4 50%,#45b7d1 100%)!important;border:none!important;border-radius:30px!important;color:white!important;font-family:var(--font-display)!important;font-weight:900!important;font-size:20px!important;text-transform:uppercase!important;letter-spacing:3px!important;padding:1.5rem 3rem!important;transition:all .4s cubic-bezier(0.175,0.885,0.32,1.275)!important;box-shadow:0 15px 35px rgba(255,107,107,.4),0 0 40px rgba(78,205,196,.3),inset 0 1px 0 rgba(255,255,255,.2)!important;transform-style:preserve-3d!important;position:relative!important;overflow:hidden!important;text-shadow:0 3px 6px rgba(0,0,0,.4)!important;backdrop-filter:blur(10px)!important}
.stButton>button[data-testid="baseButton-secondary"]:hover{background:linear-gradient(135deg,#ff5252 0%,#26a69a 50%,#42a5f5 100%)!important;transform:translateY(-5px) scale(1.05)!important;box-shadow:0 20px 40px rgba(255,107,107,.5),0 0 40px rgba(78,205,196,.4),inset 0 1px 0 rgba(255,255,255,.3)!important;letter-spacing:3px!important}
.stButton>button[data-testid="baseButton-secondary"]::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.3),transparent);transition:left .6s ease;z-index:1}
.stButton>button[data-testid="baseButton-secondary"]:hover::before{left:100%}
.stButton>button[data-testid="baseButton-secondary"] span{position:relative;z-index:2}
.stButton>button::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent);transition:left .5s ease}
.stButton>button:hover{transform:translateY(-3px) scale(1.05)!important;box-shadow:0 12px 35px rgba(74,144,226,.4),0 0 30px rgba(74,144,226,.3)!important}
.stButton>button:hover::before{left:100%}
.stButton>button:active{transform:translateY(-1px) scale(1.02)!important}
.success-box{background:rgba(139,92,246,.1);border:1px solid rgba(139,92,246,.3);border-radius:10px;padding:1rem;color:#8b5cf6;transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 5px 15px rgba(139,92,246,.1)}
.success-box:hover{transform:translateY(-2px) rotateX(2deg);box-shadow:0 8px 20px rgba(139,92,246,.2)}
.info-box{background:rgba(74,144,226,.1);border:1px solid rgba(74,144,226,.3);border-radius:10px;padding:1rem;color:#4a90e2;transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 5px 15px rgba(74,144,226,.1)}
.info-box:hover{transform:translateY(-2px) rotateX(2deg);box-shadow:0 8px 20px rgba(74,144,226,.2)}
.warning-box{background:rgba(255,193,7,.1);border:1px solid rgba(255,193,7,.3);border-radius:10px;padding:1rem;color:#ffc107;transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 5px 15px rgba(255,193,7,.1)}
.warning-box:hover{transform:translateY(-2px) rotateX(2deg);box-shadow:0 8px 20px rgba(255,193,7,.2)}
/* Column alignment fix */
.stColumn > div {vertical-align: top !important; display: inline-block !important;}
.stColumn {vertical-align: top !important;}
.divider{height:2px;background:linear-gradient(90deg,transparent 0%,#4a90e2 50%,transparent 100%);margin:2rem 0;border-radius:1px;animation:dividerGlow 3s ease-in-out infinite}
@keyframes dividerGlow{0%,100%{box-shadow:0 0 10px rgba(74,144,226,.3)}50%{box-shadow:0 0 20px rgba(74,144,226,.6)}}
.feature-highlight{background:linear-gradient(135deg,rgba(74,144,226,.1) 0%,rgba(26,26,46,.8) 100%);border-radius:15px;padding:1.5rem;margin:1rem 0;border:1px solid rgba(74,144,226,.2);text-align:center;transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 10px 20px rgba(0,0,0,.2)}
.feature-highlight:hover{transform:translateY(-5px) rotateY(5deg);box-shadow:0 15px 30px rgba(0,0,0,.3);border-color:rgba(74,144,226,.4)}
.feature-highlight h3{color:#4a90e2;margin-bottom:.5rem;animation:textGlow 2s ease-in-out infinite}
@keyframes textGlow{0%,100%{text-shadow:0 0 10px rgba(74,144,226,.3)}50%{text-shadow:0 0 20px rgba(74,144,226,.6)}}
.audio-section{background:rgba(26,26,46,.8);border-radius:15px;padding:2rem;text-align:center;border:1px solid rgba(74,144,226,.3);transform-style:preserve-3d;transition:all .3s ease;box-shadow:0 15px 30px rgba(0,0,0,.3)}
.audio-section:hover{transform:translateY(-3px) rotateX(2deg);box-shadow:0 20px 40px rgba(0,0,0,.4)}
.footer{text-align:center;color:#b8c5d6;padding:2rem 0;margin-top:3rem;border-top:1px solid rgba(74,144,226,.2);transform-style:preserve-3d;transition:all .3s ease}
.footer:hover{transform:translateY(-2px)}
.loading-pulse{animation:pulse 1.5s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.rotate-on-scroll{transition:transform .3s ease}
.interactive-element{transition:all .3s ease;cursor:pointer}
.interactive-element:hover{transform:scale(1.05);filter:brightness(1.2)}

/* Top navigation bar */
.top-nav{display:flex;gap:1rem;justify-content:center;align-items:center;margin:0 0 1rem 0;padding:.75rem 1rem;border:1px solid rgba(74,144,226,.2);border-radius:12px;background:rgba(26,26,46,.6);backdrop-filter:blur(10px);box-shadow:0 10px 20px rgba(0,0,0,.2)}
.top-nav a{font-family:var(--font-display);text-decoration:none;color:#b8c5d6;padding:.5rem 1rem;border-radius:8px;transition:all .2s ease}
.top-nav a.active{color:#ffffff;background:rgba(74,144,226,.2);border:1px solid rgba(74,144,226,.4)}
.top-nav a:hover{color:#ffffff;background:rgba(74,144,226,.15)}
</style>
<div class="frequency-wave"></div>
<div class="frequency-wave"></div>
<div class="frequency-wave"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
""",
        unsafe_allow_html=True,
    )


def nav(active: str):
    # Create navigation buttons with clean styling
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", key="nav_home", type="primary" if active == "Home" else "secondary", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()
    
    with col2:
        if st.button("ℹ️ About", key="nav_about", type="primary" if active == "About" else "secondary", use_container_width=True):
            st.session_state.page = "About"
            st.rerun()
    
    with col3:
        if st.button("📚 History", key="nav_history", type="primary" if active == "History" else "secondary", use_container_width=True):
            st.session_state.page = "History"
            st.rerun()
    
    with col4:
        if st.button("📞 Contact", key="nav_contact", type="primary" if active == "Contact" else "secondary", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()


def header():
    st.markdown(
        """
<div class="main-header">
    <h1>🎧 EchoVerse</h1>
    <p>AI-Powered Audiobook Creation Tool</p>
    <p style="font-size: 1rem; margin-top: 1rem; opacity: 0.8;">"Transform your words into healing soundscapes that resonate with the soul"</p>
</div>
""",
        unsafe_allow_html=True,
    )


