import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="CIMED - Saúde em Movimento",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS CIMED PRETO E AMARELO - FUNCIONALIDADES INOVADORAS
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=IBM+Plex+Sans:wght@300;400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
        font-family: 'IBM Plex Sans', sans-serif;
        color: #ffffff;
        line-height: 1.8;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ANIMAÇÕES INOVADORAS */
    @keyframes electricPulse {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 200, 0, 0.5); }
        50% { box-shadow: 0 0 60px rgba(255, 200, 0, 0.9); }
    }
    
    @keyframes scanLine {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
    }
    
    @keyframes glitchEffect {
        0% { transform: translateX(0); }
        20% { transform: translateX(-2px); }
        40% { transform: translateX(2px); }
        60% { transform: translateX(-2px); }
        80% { transform: translateX(2px); }
        100% { transform: translateX(0); }
    }
    
    @keyframes dataFlow {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes circleRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes yellowFlash {
        0%, 100% { color: #FFC800; text-shadow: 0 0 10px #FFC800; }
        50% { color: #FFD700; text-shadow: 0 0 30px #FFD700; }
    }
    
    @keyframes borderFlow {
        0% { border-color: #FFC800; }
        50% { border-color: #FFD700; }
        100% { border-color: #FFC800; }
    }
    
    @keyframes slideInLeft {
        0% { transform: translateX(-100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        0% { transform: translateX(100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    /* NAVBAR CIMED */
    .navbar {
        background: linear-gradient(90deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
        border-bottom: 3px solid #FFC800;
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 0 30px rgba(255, 200, 0, 0.3);
    }
    
    .navbar-logo {
        font-size: 32px;
        font-weight: 700;
        color: #FFC800;
        letter-spacing: 4px;
        font-family: 'Space Mono', monospace;
        animation: yellowFlash 2s ease-in-out infinite;
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: #ffffff;
        text-decoration: none;
        font-weight: 600;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 2px;
        background: #FFC800;
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #FFC800;
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, #FFC800, #FFD700);
        color: #0a0a0a;
        padding: 12px 32px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: 2px solid #FFC800;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(255, 200, 0, 0.4);
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(255, 200, 0, 0.7);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
        min-height: 800px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 80px 60px;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        border: 2px solid rgba(255, 200, 0, 0.2);
        border-radius: 50%;
        top: -200px;
        right: -200px;
        animation: circleRotate 20s linear infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 400px;
        height: 400px;
        border: 2px solid rgba(255, 200, 0, 0.15);
        border-radius: 50%;
        bottom: -150px;
        left: -150px;
        animation: circleRotate 30s linear infinite reverse;
    }
    
    .hero-content {
        text-align: center;
        z-index: 2;
        position: relative;
        max-width: 900px;
    }
    
    .hero-title {
        font-size: 80px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #FFC800;
        letter-spacing: -2px;
        line-height: 1.1;
        font-family: 'Space Mono', monospace;
        animation: yellowFlash 2s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 200, 0, 0.6);
    }
    
    .hero-subtitle {
        font-size: 24px;
        font-weight: 400;
        margin-bottom: 50px;
        color: #ffffff;
        letter-spacing: 2px;
        animation: slideInLeft 1s ease-out;
    }
    
    .hero-cta-group {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .hero-cta-primary {
        background: linear-gradient(135deg, #FFC800, #FFD700);
        color: #0a0a0a;
        padding: 18px 50px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid #FFC800;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 30px rgba(255, 200, 0, 0.5);
        font-family: 'IBM Plex Sans', sans-serif;
        animation: slideInLeft 1.2s ease-out;
    }
    
    .hero-cta-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 50px rgba(255, 200, 0, 0.8);
    }
    
    .hero-cta-secondary {
        background: transparent;
        color: #FFC800;
        padding: 18px 50px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid #FFC800;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(255, 200, 0, 0.3);
        font-family: 'IBM Plex Sans', sans-serif;
        animation: slideInRight 1.4s ease-out;
    }
    
    .hero-cta-secondary:hover {
        background: #FFC800;
        color: #0a0a0a;
        box-shadow: 0 0 40px rgba(255, 200, 0, 0.6);
    }
    
    /* STATS SECTION - FUNCIONALIDADE 1 */
    .stats-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
        position: relative;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(255, 200, 0, 0.05), rgba(255, 200, 0, 0.02));
        border: 2px solid #FFC800;
        padding: 50px 40px;
        border-radius: 12px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: dataFlow 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 0 20px rgba(255, 200, 0, 0.15);
    }
    
    .stat-card:nth-child(1) { animation-delay: 0.1s; }
    .stat-card:nth-child(2) { animation-delay: 0.2s; }
    .stat-card:nth-child(3) { animation-delay: 0.3s; }
    .stat-card:nth-child(4) { animation-delay: 0.4s; }
    
    .stat-card:hover {
        transform: translateY(-15px);
        border-color: #FFD700;
        box-shadow: 0 0 50px rgba(255, 200, 0, 0.4);
    }
    
    .stat-number {
        font-size: 56px;
        font-weight: 700;
        color: #FFC800;
        margin-bottom: 15px;
        font-family: 'Space Mono', monospace;
        animation: yellowFlash 2s ease-in-out infinite;
    }
    
    .stat-label {
        font-size: 16px;
        font-weight: 600;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* TIMELINE SECTION - FUNCIONALIDADE 2 */
    .timeline-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 700;
        margin-bottom: 100px;
        text-align: center;
        color: #FFC800;
        letter-spacing: -1px;
        font-family: 'Space Mono', monospace;
        animation: yellowFlash 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 200, 0, 0.5);
    }
    
    .timeline {
        max-width: 1000px;
        margin: 0 auto;
        position: relative;
    }
    
    .timeline::before {
        content: '';
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #FFC800, transparent);
        animation: dataFlow 2s ease-in-out infinite;
    }
    
    .timeline-item {
        margin-bottom: 50px;
        position: relative;
        animation: slideInLeft 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .timeline-item:nth-child(odd) {
        text-align: right;
        padding-right: 52%;
    }
    
    .timeline-item:nth-child(even) {
        text-align: left;
        padding-left: 52%;
        animation: slideInRight 0.8s ease-out;
    }
    
    .timeline-item:nth-child(1) { animation-delay: 0.1s; }
    .timeline-item:nth-child(2) { animation-delay: 0.2s; }
    .timeline-item:nth-child(3) { animation-delay: 0.3s; }
    .timeline-item:nth-child(4) { animation-delay: 0.4s; }
    
    .timeline-dot {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 20px;
        height: 20px;
        background: #FFC800;
        border: 4px solid #0a0a0a;
        border-radius: 50%;
        top: 0;
        box-shadow: 0 0 20px rgba(255, 200, 0, 0.6);
        animation: electricPulse 2s ease-in-out infinite;
    }
    
    .timeline-content {
        background: linear-gradient(135deg, rgba(255, 200, 0, 0.05), rgba(255, 200, 0, 0.02));
        border: 2px solid #FFC800;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(255, 200, 0, 0.15);
    }
    
    .timeline-year {
        font-size: 24px;
        font-weight: 700;
        color: #FFC800;
        margin-bottom: 10px;
        font-family: 'Space Mono', monospace;
    }
    
    .timeline-desc {
        font-size: 14px;
        color: #cccccc;
        line-height: 1.6;
    }
    
    /* FEATURES GRID - FUNCIONALIDADE 3 */
    .features-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 200, 0, 0.05), rgba(255, 200, 0, 0.02));
        border: 2px solid #FFC800;
        padding: 50px 40px;
        border-radius: 12px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: dataFlow 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 0 20px rgba(255, 200, 0, 0.15);
    }
    
    .feature-card:nth-child(1) { animation-delay: 0.1s; }
    .feature-card:nth-child(2) { animation-delay: 0.2s; }
    .feature-card:nth-child(3) { animation-delay: 0.3s; }
    .feature-card:nth-child(4) { animation-delay: 0.4s; }
    .feature-card:nth-child(5) { animation-delay: 0.5s; }
    .feature-card:nth-child(6) { animation-delay: 0.6s; }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 200, 0, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-15px);
        border-color: #FFD700;
        box-shadow: 0 0 50px rgba(255, 200, 0, 0.3);
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 20px;
        animation: electricPulse 2s ease-in-out infinite;
    }
    
    .feature-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #FFC800;
        letter-spacing: 0.5px;
        font-family: 'Space Mono', monospace;
    }
    
    .feature-desc {
        font-size: 15px;
        color: #cccccc;
        line-height: 1.8;
        font-weight: 400;
    }
    
    /* TESTIMONIALS SECTION - FUNCIONALIDADE 4 */
    .testimonials-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    }
    
    .testimonials-title {
        font-size: 56px;
        font-weight: 700;
        margin-bottom: 100px;
        text-align: center;
        color: #FFC800;
        letter-spacing: -1px;
        font-family: 'Space Mono', monospace;
        animation: yellowFlash 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 200, 0, 0.5);
    }
    
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .testimonial-card {
        background: linear-gradient(135deg, rgba(255, 200, 0, 0.08), rgba(255, 200, 0, 0.03));
        border-left: 4px solid #FFC800;
        padding: 50px 40px;
        border-radius: 12px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInLeft 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 0 30px rgba(255, 200, 0, 0.15);
    }
    
    .testimonial-card:nth-child(1) { animation-delay: 0.1s; }
    .testimonial-card:nth-child(2) { animation-delay: 0.2s; }
    .testimonial-card:nth-child(3) { animation-delay: 0.3s; }
    
    .testimonial-card::before {
        content: '"';
        position: absolute;
        top: 10px;
        left: 15px;
        font-size: 80px;
        color: rgba(255, 200, 0, 0.1);
        font-family: 'Space Mono', monospace;
    }
    
    .testimonial-card:hover {
        transform: translateX(10px);
        border-left-color: #FFD700;
        box-shadow: 0 0 50px rgba(255, 200, 0, 0.25);
    }
    
    .testimonial-text {
        font-size: 16px;
        color: #cccccc;
        margin-bottom: 25px;
        line-height: 1.8;
        font-style: italic;
        position: relative;
        z-index: 1;
    }
    
    .testimonial-author {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .testimonial-avatar {
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #FFC800, #FFD700);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        color: #0a0a0a;
        font-size: 20px;
    }
    
    .testimonial-info {
        flex: 1;
    }
    
    .testimonial-name {
        font-size: 16px;
        font-weight: 700;
        color: #FFC800;
        margin-bottom: 3px;
        font-family: 'Space Mono', monospace;
    }
    
    .testimonial-role {
        font-size: 13px;
        color: #888888;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* CTA FINAL */
    .cta-final-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #FFC800 0%, #FFD700 100%);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-final-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(10, 10, 10, 0.2);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-final-title {
        font-size: 56px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #0a0a0a;
        letter-spacing: -1px;
        font-family: 'Space Mono', monospace;
    }
    
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        color: #1a1a1a;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 400;
    }
    
    .cta-final-button {
        background: #0a0a0a;
        color: #FFC800;
        padding: 18px 60px;
        border: 3px solid #0a0a0a;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
    }
    
    /* FOOTER */
    .footer {
        background: #0a0a0a;
        color: #888888;
        padding: 80px;
        text-align: center;
        border-top: 3px solid #FFC800;
        box-shadow: 0 -8px 32px rgba(255, 200, 0, 0.2);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 400;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(255, 200, 0, 0.3);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Space Mono', monospace;
    }
    
    /* RESPONSIVIDADE */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            gap: 20px;
            padding: 15px 20px;
        }
        
        .navbar-links {
            flex-direction: column;
            gap: 15px;
            width: 100%;
        }
        
        .hero-section {
            min-height: 500px;
            padding: 40px 20px;
        }
        
        .hero-title {
            font-size: 42px;
        }
        
        .stats-section,
        .timeline-section,
        .features-section,
        .process-section,
        .cta-final-section {
            padding: 80px 20px;
        }
        
        .section-title,
        .process-title {
            font-size: 36px;
        }
        
        .timeline::before {
            left: 10px;
        }
        
        .timeline-item:nth-child(odd),
        .timeline-item:nth-child(even) {
            text-align: left;
            padding-left: 50px;
            padding-right: 0;
        }
        
        .timeline-dot {
            left: 0;
            transform: translateX(-50%);
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
navbar_html = '<div class="navbar"><div class="navbar-logo">CIMED</div><div class="navbar-links"><a href="#" class="navbar-link">Soluções</a><a href="#" class="navbar-link">Tecnologia</a><a href="#" class="navbar-link">Sobre</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Começar</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">CIMED</div>
        <div class="hero-subtitle">Tecnologia e Inovação em Saúde</div>
        <div class="hero-cta-group">
            <button class="hero-cta-primary">Explorar Agora</button>
            <button class="hero-cta-secondary">Saiba Mais</button>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== STATS SECTION ====================
stats_html = '''<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">50K+</div>
            <div class="stat-label">Pacientes Atendidos</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">200+</div>
            <div class="stat-label">Profissionais</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">99.9%</div>
            <div class="stat-label">Uptime</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Suporte</div>
        </div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# ==================== TIMELINE SECTION ====================
timeline_html = '''<div class="timeline-section">
    <div class="section-title">Nossa Jornada</div>
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-year">2020</div>
                <div class="timeline-desc">Fundação e primeiros passos na inovação em saúde</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-year">2021</div>
                <div class="timeline-desc">Expansão para 5 estados brasileiros</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-year">2022</div>
                <div class="timeline-desc">Lançamento da plataforma digital revolucionária</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-year">2024</div>
                <div class="timeline-desc">Liderança no mercado de saúde digital</div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(timeline_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
features_html = '''<div class="features-section">
    <div class="section-title">Funcionalidades</div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Velocidade</div>
            <div class="feature-desc">Plataforma ultra rápida com resposta em milissegundos</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Segurança</div>
            <div class="feature-desc">Criptografia de ponta com padrões internacionais</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Analytics</div>
            <div class="feature-desc">Dados em tempo real para melhor decisão</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌐</div>
            <div class="feature-title">Integração</div>
            <div class="feature-desc">Conecte com seus sistemas existentes</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">👥</div>
            <div class="feature-title">Colaboração</div>
            <div class="feature-desc">Trabalhe em equipe de forma eficiente</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Escalabilidade</div>
            <div class="feature-desc">Cresce com seu negócio sem limites</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ==================== TESTIMONIALS SECTION ====================
testimonials_html = '''<div class="testimonials-section">
    <div class="testimonials-title">O Que Dizem</div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <div class="testimonial-text">A plataforma CIMED revolucionou completamente nosso atendimento. Eficiência e qualidade em um só lugar.</div>
            <div class="testimonial-author">
                <div class="testimonial-avatar">DR</div>
                <div class="testimonial-info">
                    <div class="testimonial-name">Dr. Roberto Silva</div>
                    <div class="testimonial-role">Clínico Geral</div>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">Implementar CIMED foi a melhor decisão para nosso hospital. Segurança, velocidade e confiabilidade garantidas.</div>
            <div class="testimonial-author">
                <div class="testimonial-avatar">AM</div>
                <div class="testimonial-info">
                    <div class="testimonial-name">Dra. Ana Martins</div>
                    <div class="testimonial-role">Diretora Médica</div>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">Suporte impecável e tecnologia de ponta. CIMED é o futuro da saúde digital no Brasil.</div>
            <div class="testimonial-author">
                <div class="testimonial-avatar">CP</div>
                <div class="testimonial-info">
                    <div class="testimonial-name">Carlos Pereira</div>
                    <div class="testimonial-role">CEO de Clínica</div>
                </div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(testimonials_html, unsafe_allow_html=True)

# ==================== CTA FINAL ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronto para Revolucionar?</div>
        <div class="cta-final-desc">Junte-se aos líderes em inovação de saúde digital</div>
        <button class="cta-final-button">Começar Agora</button>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">Email: contato@cimed.com.br | Telefone: +55 (11) 98765-4321</div><div class="footer-text">Endereço: Av. Tecnologia, 1000 - São Paulo, SP</div><div class="footer-copyright">© 2025 CIMED. Todos os direitos reservados. Inovação em Saúde.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
