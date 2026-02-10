import streamlit as st

st.set_page_config(
    page_title="Sofisticado & Vivo - Premium Design",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Montserrat:wght@400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        font-family: 'Montserrat', sans-serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes heroGlow {
        0%, 100% { text-shadow: 0 0 30px rgba(59, 130, 246, 0.3), 0 0 60px rgba(139, 92, 246, 0.2); }
        50% { text-shadow: 0 0 50px rgba(59, 130, 246, 0.6), 0 0 100px rgba(139, 92, 246, 0.4); }
    }
    
    @keyframes floatMagic {
        0%, 100% { transform: translateY(0px) rotateZ(-2deg); }
        50% { transform: translateY(-40px) rotateZ(2deg); }
    }
    
    @keyframes pulseRich {
        0%, 100% { box-shadow: 0 0 20px rgba(59, 130, 246, 0.3), inset 0 0 20px rgba(59, 130, 246, 0.1); }
        50% { box-shadow: 0 0 60px rgba(59, 130, 246, 0.6), inset 0 0 40px rgba(59, 130, 246, 0.2); }
    }
    
    @keyframes slideInStagger {
        0% { transform: translateY(60px) rotateX(20deg); opacity: 0; }
        100% { transform: translateY(0) rotateX(0deg); opacity: 1; }
    }
    
    @keyframes borderFlow {
        0% { border-color: rgba(59, 130, 246, 0.2); }
        50% { border-color: rgba(139, 92, 246, 0.8); }
        100% { border-color: rgba(59, 130, 246, 0.2); }
    }
    
    @keyframes shimmerFlow {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    /* NAVBAR */
    .navbar {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
        backdrop-filter: blur(40px);
        padding: 25px 100px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid rgba(59, 130, 246, 0.2);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 8px 40px rgba(59, 130, 246, 0.15);
    }
    
    .navbar-logo {
        font-size: 28px;
        font-weight: 900;
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        letter-spacing: 3px;
    }
    
    .navbar-nav {
        display: flex;
        gap: 80px;
    }
    
    .nav-link {
        color: #a1b4d6;
        text-decoration: none;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after { width: 100%; }
    .nav-link:hover { color: #3b82f6; }
    
    /* HERO SECTION */
    .hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 100px 100px;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        width: 1200px;
        height: 1200px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        top: -400px;
        right: -400px;
        animation: floatMagic 8s ease-in-out infinite;
    }
    
    .hero::after {
        content: '';
        position: absolute;
        width: 1000px;
        height: 1000px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -300px;
        left: -300px;
        animation: floatMagic 10s ease-in-out infinite reverse;
    }
    
    .hero-content {
        max-width: 700px;
        position: relative;
        z-index: 2;
    }
    
    .hero-label {
        font-size: 13px;
        color: #3b82f6;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 25px;
        font-weight: 800;
    }
    
    .hero-title {
        font-size: 90px;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: -2px;
        animation: heroGlow 3s ease-in-out infinite;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #3b82f6);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-desc {
        font-size: 18px;
        color: #a1b4d6;
        margin-bottom: 60px;
        line-height: 1.9;
        font-weight: 400;
    }
    
    .hero-cta {
        display: flex;
        gap: 25px;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        color: #ffffff;
        padding: 18px 55px;
        border: none;
        border-radius: 8px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 40px rgba(59, 130, 246, 0.4), inset 0 0 20px rgba(255, 255, 255, 0.1);
    }
    
    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 80px rgba(59, 130, 246, 0.8), inset 0 0 30px rgba(255, 255, 255, 0.2);
    }
    
    .btn-secondary {
        background: transparent;
        color: #3b82f6;
        padding: 18px 55px;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.2);
    }
    
    .btn-secondary:hover {
        background: rgba(59, 130, 246, 0.1);
        box-shadow: 0 0 50px rgba(59, 130, 246, 0.4);
    }
    
    .hero-visual {
        position: relative;
        z-index: 2;
        width: 500px;
        height: 600px;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.08));
        border: 2px solid rgba(59, 130, 246, 0.3);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 120px;
        animation: floatMagic 6s ease-in-out infinite;
        box-shadow: 0 0 60px rgba(59, 130, 246, 0.2), inset 0 0 40px rgba(59, 130, 246, 0.1);
    }
    
    /* RICH ELEMENTS SECTION */
    .rich-section {
        padding: 150px 100px;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    }
    
    .section-title {
        font-size: 72px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 120px;
        font-family: 'Playfair Display', serif;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .rich-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 60px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .rich-card {
        padding: 70px 50px;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(139, 92, 246, 0.05));
        border: 2px solid rgba(59, 130, 246, 0.2);
        border-radius: 12px;
        transition: all 0.4s ease;
        animation: slideInStagger 0.8s ease-out;
        animation-fill-mode: both;
        position: relative;
        overflow: hidden;
    }
    
    .rich-card:nth-child(1) { animation-delay: 0.1s; }
    .rich-card:nth-child(2) { animation-delay: 0.2s; }
    .rich-card:nth-child(3) { animation-delay: 0.3s; }
    
    .rich-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.2), transparent);
        animation: shimmerFlow 3s ease-in-out infinite;
    }
    
    .rich-card:hover {
        transform: translateY(-20px);
        border-color: #3b82f6;
        box-shadow: 0 0 80px rgba(59, 130, 246, 0.4), inset 0 0 40px rgba(59, 130, 246, 0.1);
    }
    
    .rich-icon {
        font-size: 64px;
        margin-bottom: 30px;
        animation: floatMagic 4s ease-in-out infinite;
    }
    
    .rich-title {
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 20px;
        color: #ffffff;
        font-family: 'Playfair Display', serif;
    }
    
    .rich-desc {
        font-size: 15px;
        color: #a1b4d6;
        line-height: 1.9;
    }
    
    /* SHOWCASE SECTION */
    .showcase-section {
        padding: 150px 100px;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    .showcase-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 80px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .showcase-item {
        padding: 80px 60px;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.06));
        border: 2px solid rgba(59, 130, 246, 0.25);
        border-radius: 12px;
        transition: all 0.4s ease;
        animation: slideInStagger 0.8s ease-out;
        animation-fill-mode: both;
        position: relative;
        overflow: hidden;
    }
    
    .showcase-item:nth-child(1) { animation-delay: 0.1s; }
    .showcase-item:nth-child(2) { animation-delay: 0.2s; }
    .showcase-item:nth-child(3) { animation-delay: 0.3s; }
    .showcase-item:nth-child(4) { animation-delay: 0.4s; }
    
    .showcase-item::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.2) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .showcase-item:hover {
        transform: translateY(-15px);
        border-color: #8b5cf6;
        box-shadow: 0 0 100px rgba(139, 92, 246, 0.3), inset 0 0 50px rgba(59, 130, 246, 0.1);
    }
    
    .showcase-number {
        font-size: 72px;
        font-weight: 900;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
        font-family: 'Playfair Display', serif;
    }
    
    .showcase-title {
        font-size: 32px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 15px;
        font-family: 'Playfair Display', serif;
    }
    
    .showcase-desc {
        font-size: 16px;
        color: #a1b4d6;
        line-height: 1.9;
    }
    
    /* CTA FINAL */
    .cta-final {
        padding: 150px 100px;
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-final::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(15, 23, 42, 0.1);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-final-title {
        font-size: 64px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: -1px;
    }
    
    .cta-final-desc {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.95);
        max-width: 700px;
        margin: 0 auto 60px;
    }
    
    .cta-final-btn {
        background: #0f172a;
        color: #3b82f6;
        padding: 18px 65px;
        border: 2px solid #0f172a;
        border-radius: 8px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 40px rgba(15, 23, 42, 0.4);
    }
    
    .cta-final-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 50px rgba(15, 23, 42, 0.6);
    }
    
    /* FOOTER */
    .footer {
        background: #0f172a;
        color: #a1b4d6;
        padding: 100px 100px;
        text-align: center;
        border-top: 2px solid rgba(59, 130, 246, 0.2);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(59, 130, 246, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .hero { flex-direction: column; padding: 50px 20px; min-height: auto; }
        .hero-title { font-size: 52px; }
        .hero-visual { width: 100%; margin-top: 40px; }
        .rich-grid { grid-template-columns: 1fr; gap: 30px; }
        .showcase-grid { grid-template-columns: 1fr; gap: 40px; }
        .cta-final { padding: 100px 20px; }
        .cta-final-title { font-size: 42px; }
        .section-title { font-size: 42px; }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">VIVO</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Recursos</a>
        <a href="#" class="nav-link">Sobre</a>
        <a href="#" class="nav-link">Showcase</a>
        <a href="#" class="nav-link">Contato</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-content">
        <div class="hero-label">Bem-vindo</div>
        <div class="hero-title">Sofisticação com Vida</div>
        <div class="hero-desc">Design que pulsa de criatividade. Elementos ricos que inspiram, cores vibrantes que envolvem, animações que impressionam.</div>
        <div class="hero-cta">
            <button class="btn-primary">Começar Jornada</button>
            <button class="btn-secondary">Explorar</button>
        </div>
    </div>
    <div class="hero-visual">✨</div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# RICH ELEMENTS
rich_html = '''<div class="rich-section">
    <div class="section-title">Elementos Ricos</div>
    <div class="rich-grid">
        <div class="rich-card">
            <div class="rich-icon">🎨</div>
            <div class="rich-title">Design Vibrante</div>
            <div class="rich-desc">Cores que vivem, elementos que respiram. Cada pixel foi pensado para criar uma experiência extraordinária.</div>
        </div>
        <div class="rich-card">
            <div class="rich-icon">✨</div>
            <div class="rich-title">Animações Absurdas</div>
            <div class="rich-desc">Movimento que hipnotiza. Transições suaves que guiam o olhar e criam conexão emocional.</div>
        </div>
        <div class="rich-card">
            <div class="rich-icon">🚀</div>
            <div class="rich-title">Performance Premium</div>
            <div class="rich-desc">Velocidade extrema sem sacrificar beleza. Otimizado para impressionar em qualquer dispositivo.</div>
        </div>
    </div>
</div>'''
st.markdown(rich_html, unsafe_allow_html=True)

# SHOWCASE
showcase_html = '''<div class="showcase-section">
    <div class="section-title">Resultados Extraordinários</div>
    <div class="showcase-grid">
        <div class="showcase-item">
            <div class="showcase-number">500+</div>
            <div class="showcase-title">Projetos Criados</div>
            <div class="showcase-desc">Cada um uma obra-prima de design e funcionalidade que superou expectativas.</div>
        </div>
        <div class="showcase-item">
            <div class="showcase-number">98%</div>
            <div class="showcase-title">Taxa de Satisfação</div>
            <div class="showcase-desc">Clientes que voltam porque sabem que vão receber excelência em cada projeto.</div>
        </div>
        <div class="showcase-item">
            <div class="showcase-number">20+</div>
            <div class="showcase-title">Anos de Experiência</div>
            <div class="showcase-desc">Duas décadas refinando a arte de criar experiências digitais memoráveis.</div>
        </div>
        <div class="showcase-item">
            <div class="showcase-number">∞</div>
            <div class="showcase-title">Possibilidades</div>
            <div class="showcase-desc">Sem limites para criatividade. Cada projeto é uma oportunidade de inovar.</div>
        </div>
    </div>
</div>'''
st.markdown(showcase_html, unsafe_allow_html=True)

# CTA
cta_html = '''<div class="cta-final">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronto para Transformar?</div>
        <div class="cta-final-desc">Junte-se a centenas de marcas que já experimentaram a magia de design sofisticado com vida.</div>
        <button class="cta-final-btn">Comece Agora</button>
    </div>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-text">Email: contato@vivo.com | Telefone: +55 (11) 98765-4321</div>
    <div class="footer-text">LinkedIn: linkedin.com/company/vivo | Website: vivo.com</div>
    <div class="footer-copyright">© 2025 Vivo Design. Todos os direitos reservados.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
