import streamlit as st

st.set_page_config(
    page_title="Premium Professional Landing",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Lato:wght@300;400;700;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);
        font-family: 'Lato', sans-serif;
        color: #1a1a1a;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    @keyframes slideInLeft {
        0% { transform: translateX(-80px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeInUp {
        0% { transform: translateY(40px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes floatSoft {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes lineGrow {
        0% { width: 0; }
        100% { width: 100%; }
    }
    
    /* NAVBAR */
    .navbar {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        padding: 20px 100px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .navbar-logo {
        font-size: 26px;
        font-weight: 700;
        color: #1a1a1a;
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: 2px;
    }
    
    .navbar-nav {
        display: flex;
        gap: 80px;
    }
    
    .nav-link {
        color: #666;
        text-decoration: none;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        transition: all 0.3s ease;
        position: relative;
        font-family: 'Lato', sans-serif;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 2px;
        background: #1a1a1a;
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after { width: 100%; }
    .nav-link:hover { color: #1a1a1a; }
    
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
        width: 1000px;
        height: 1000px;
        background: radial-gradient(circle, rgba(0, 0, 0, 0.03) 0%, transparent 70%);
        border-radius: 50%;
        top: -400px;
        right: -400px;
    }
    
    .hero::after {
        content: '';
        position: absolute;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(0, 0, 0, 0.02) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -300px;
        left: -300px;
    }
    
    .hero-content {
        max-width: 650px;
        position: relative;
        z-index: 2;
        animation: slideInLeft 1s ease-out;
    }
    
    .hero-label {
        font-size: 12px;
        color: #999;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 25px;
        font-weight: 700;
    }
    
    .hero-title {
        font-size: 80px;
        font-weight: 700;
        line-height: 1;
        margin-bottom: 30px;
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: -2px;
        color: #1a1a1a;
    }
    
    .hero-desc {
        font-size: 18px;
        color: #666;
        margin-bottom: 60px;
        line-height: 1.8;
        font-weight: 300;
    }
    
    .hero-cta {
        display: flex;
        gap: 25px;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: #1a1a1a;
        color: #ffffff;
        padding: 16px 50px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
    }
    
    .btn-secondary {
        background: transparent;
        color: #1a1a1a;
        padding: 16px 50px;
        border: 2px solid #1a1a1a;
        border-radius: 2px;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-secondary:hover {
        background: #1a1a1a;
        color: #ffffff;
    }
    
    .hero-visual {
        position: relative;
        z-index: 2;
        width: 450px;
        height: 550px;
        background: linear-gradient(135deg, #f0f2f5 0%, #e8eaed 100%);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 2px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 120px;
        animation: floatSoft 4s ease-in-out infinite;
    }
    
    /* SECTION DIVIDER - ELEMENTO NOVO */
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 0, 0, 0.1), transparent);
        margin: 120px 100px;
    }
    
    /* STATS SECTION - ELEMENTO NOVO */
    .stats-section {
        padding: 120px 100px;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 80px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .stat-item {
        text-align: left;
        animation: fadeInUp 0.8s ease-out;
        animation-fill-mode: both;
        position: relative;
    }
    
    .stat-item:nth-child(1) { animation-delay: 0.1s; }
    .stat-item:nth-child(2) { animation-delay: 0.2s; }
    .stat-item:nth-child(3) { animation-delay: 0.3s; }
    .stat-item:nth-child(4) { animation-delay: 0.4s; }
    
    .stat-item::before {
        content: '';
        position: absolute;
        bottom: -20px;
        left: 0;
        width: 60px;
        height: 3px;
        background: #1a1a1a;
        transition: width 0.3s ease;
    }
    
    .stat-item:hover::before { width: 100%; }
    
    .stat-number {
        font-size: 56px;
        font-weight: 900;
        color: #1a1a1a;
        margin-bottom: 15px;
        font-family: 'Lato', sans-serif;
    }
    
    .stat-label {
        font-size: 14px;
        color: #999;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
    }
    
    /* SERVICES SECTION - ELEMENTO NOVO */
    .services-section {
        padding: 120px 100px;
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);
    }
    
    .section-title {
        font-size: 64px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 100px;
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: -1px;
        color: #1a1a1a;
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 60px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .service-item {
        padding: 70px 50px;
        background: #ffffff;
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 2px;
        transition: all 0.4s ease;
        animation: fadeInUp 0.8s ease-out;
        animation-fill-mode: both;
        position: relative;
        overflow: hidden;
    }
    
    .service-item:nth-child(1) { animation-delay: 0.1s; }
    .service-item:nth-child(2) { animation-delay: 0.2s; }
    .service-item:nth-child(3) { animation-delay: 0.3s; }
    
    .service-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 4px;
        background: #1a1a1a;
        transition: left 0.6s ease;
    }
    
    .service-item:hover::before { left: 100%; }
    
    .service-item:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
    }
    
    .service-icon {
        font-size: 48px;
        margin-bottom: 30px;
    }
    
    .service-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #1a1a1a;
        font-family: 'Cormorant Garamond', serif;
    }
    
    .service-desc {
        font-size: 15px;
        color: #999;
        line-height: 1.8;
        font-weight: 300;
    }
    
    /* TESTIMONIALS SECTION - ELEMENTO NOVO */
    .testimonials-section {
        padding: 120px 100px;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    }
    
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 50px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .testimonial-card {
        padding: 50px;
        background: #f8f9fa;
        border-left: 4px solid #1a1a1a;
        border-radius: 2px;
        transition: all 0.4s ease;
        animation: fadeInUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .testimonial-card:nth-child(1) { animation-delay: 0.1s; }
    .testimonial-card:nth-child(2) { animation-delay: 0.2s; }
    .testimonial-card:nth-child(3) { animation-delay: 0.3s; }
    
    .testimonial-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
    }
    
    .testimonial-text {
        font-size: 16px;
        color: #1a1a1a;
        margin-bottom: 30px;
        line-height: 1.8;
        font-weight: 300;
        font-style: italic;
    }
    
    .testimonial-author {
        font-size: 13px;
        font-weight: 700;
        color: #1a1a1a;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .testimonial-role {
        font-size: 12px;
        color: #999;
        margin-top: 5px;
    }
    
    /* CTA SECTION */
    .cta-section {
        padding: 150px 100px;
        background: #1a1a1a;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-title {
        font-size: 56px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 30px;
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: -1px;
    }
    
    .cta-desc {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.8);
        max-width: 700px;
        margin: 0 auto 60px;
        font-weight: 300;
    }
    
    .cta-btn {
        background: #ffffff;
        color: #1a1a1a;
        padding: 16px 60px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }
    
    .cta-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
    }
    
    /* FOOTER */
    .footer {
        background: #ffffff;
        color: #999;
        padding: 80px 100px;
        text-align: center;
        border-top: 1px solid rgba(0, 0, 0, 0.08);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(0, 0, 0, 0.08);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .navbar-nav { gap: 20px; }
        .hero { flex-direction: column; padding: 50px 20px; min-height: auto; }
        .hero-title { font-size: 42px; }
        .hero-visual { width: 100%; margin-top: 40px; }
        .stats-section { grid-template-columns: repeat(2, 1fr); padding: 80px 20px; gap: 40px; }
        .services-grid { grid-template-columns: 1fr; gap: 30px; }
        .testimonials-grid { grid-template-columns: 1fr; }
        .cta-section { padding: 100px 20px; }
        .cta-title { font-size: 36px; }
        .section-title { font-size: 36px; }
        .section-divider { margin: 80px 20px; }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">PREMIUM</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Serviços</a>
        <a href="#" class="nav-link">Sobre</a>
        <a href="#" class="nav-link">Depoimentos</a>
        <a href="#" class="nav-link">Contato</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-content">
        <div class="hero-label">Bem-vindo</div>
        <div class="hero-title">Excelência em Design</div>
        <div class="hero-desc">Soluções sofisticadas que elevam sua marca a um novo patamar de profissionalismo e elegância.</div>
        <div class="hero-cta">
            <button class="btn-primary">Começar Agora</button>
            <button class="btn-secondary">Saiba Mais</button>
        </div>
    </div>
    <div class="hero-visual">✨</div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# DIVIDER
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# STATS
stats_html = '''<div class="stats-section">
    <div class="stat-item">
        <div class="stat-number">500+</div>
        <div class="stat-label">Projetos</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">98%</div>
        <div class="stat-label">Satisfação</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">20+</div>
        <div class="stat-label">Anos</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">50M+</div>
        <div class="stat-label">Impacto</div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# DIVIDER
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# SERVICES
services_html = '''<div class="services-section">
    <div class="section-title">Nossos Serviços</div>
    <div class="services-grid">
        <div class="service-item">
            <div class="service-icon">🎨</div>
            <div class="service-title">Design Estratégico</div>
            <div class="service-desc">Criação de identidades visuais que comunicam valor e estabelecem conexão com seu público.</div>
        </div>
        <div class="service-item">
            <div class="service-icon">✨</div>
            <div class="service-title">Experiência Digital</div>
            <div class="service-desc">Interfaces sofisticadas que transformam visitantes em clientes leais.</div>
        </div>
        <div class="service-item">
            <div class="service-icon">🚀</div>
            <div class="service-title">Inovação</div>
            <div class="service-desc">Soluções originais que estabelecem novos padrões no mercado.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# DIVIDER
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# TESTIMONIALS
testimonials_html = '''<div class="testimonials-section">
    <div class="section-title">Depoimentos</div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <div class="testimonial-text">"Transformou completamente nossa marca. Profissionalismo impecável em cada detalhe."</div>
            <div class="testimonial-author">João Silva</div>
            <div class="testimonial-role">CEO, Tech Ventures</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"A melhor decisão que tomamos. Resultados além das expectativas em tempo recorde."</div>
            <div class="testimonial-author">Maria Santos</div>
            <div class="testimonial-role">Diretora, Design Studio</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"Equipe excepcional. Entenderam nossa visão e a executaram com perfeição."</div>
            <div class="testimonial-author">Carlos Oliveira</div>
            <div class="testimonial-role">Fundador, Creative Lab</div>
        </div>
    </div>
</div>'''
st.markdown(testimonials_html, unsafe_allow_html=True)

# CTA
cta_html = '''<div class="cta-section">
    <div class="cta-title">Pronto para Crescer?</div>
    <div class="cta-desc">Transforme sua visão em uma realidade extraordinária que impacta e inspira.</div>
    <button class="cta-btn">Comece Agora</button>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-text">Email: contato@premium.com | Telefone: +55 (11) 98765-4321</div>
    <div class="footer-text">LinkedIn: linkedin.com/company/premium | Website: premium.com</div>
    <div class="footer-copyright">© 2025 Premium Design. Todos os direitos reservados.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
