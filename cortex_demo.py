import streamlit as st

st.set_page_config(
    page_title="Portfolio Violeta - Design Premium",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Montserrat:wght@600;700;800;900&family=Poppins:wght@400;500;600;700&family=Cormorant+Garamond:wght@400;500;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0a1a 0%, #1a0f2e 50%, #0f0a1a 100%);
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    @keyframes titleGlow {
        0%, 100% { text-shadow: 0 0 20px rgba(168, 85, 247, 0.3); }
        50% { text-shadow: 0 0 40px rgba(168, 85, 247, 0.6); }
    }
    
    @keyframes floatMagic {
        0%, 100% { transform: translateY(0px) rotateZ(0deg); }
        50% { transform: translateY(-30px) rotateZ(2deg); }
    }
    
    @keyframes shimmerText {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes pulseViolet {
        0%, 100% { box-shadow: 0 0 20px rgba(168, 85, 247, 0.3); }
        50% { box-shadow: 0 0 60px rgba(168, 85, 247, 0.7); }
    }
    
    @keyframes slideInMagic {
        0% { transform: translateY(50px) rotateX(20deg); opacity: 0; }
        100% { transform: translateY(0) rotateX(0deg); opacity: 1; }
    }
    
    @keyframes borderFlow {
        0% { border-color: rgba(168, 85, 247, 0.2); }
        50% { border-color: rgba(168, 85, 247, 0.8); }
        100% { border-color: rgba(168, 85, 247, 0.2); }
    }
    
    /* NAVBAR */
    .navbar {
        background: rgba(15, 10, 26, 0.95);
        backdrop-filter: blur(30px);
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid rgba(168, 85, 247, 0.2);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .navbar-logo {
        font-size: 28px;
        font-weight: 900;
        background: linear-gradient(135deg, #a855f7 0%, #d946ef 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        letter-spacing: 3px;
    }
    
    .navbar-nav {
        display: flex;
        gap: 70px;
    }
    
    .nav-link {
        color: #c4b5fd;
        text-decoration: none;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        position: relative;
        font-family: 'Montserrat', sans-serif;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #a855f7, #d946ef);
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after { width: 100%; }
    .nav-link:hover { color: #a855f7; }
    
    /* HERO SECTION */
    .hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 100px 80px;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        width: 900px;
        height: 900px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        top: -300px;
        right: -300px;
        animation: floatMagic 8s ease-in-out infinite;
    }
    
    .hero::after {
        content: '';
        position: absolute;
        width: 700px;
        height: 700px;
        background: radial-gradient(circle, rgba(217, 70, 239, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -200px;
        left: -200px;
        animation: floatMagic 10s ease-in-out infinite reverse;
    }
    
    .hero-container {
        max-width: 1000px;
        text-align: center;
        position: relative;
        z-index: 2;
    }
    
    .hero-label {
        font-size: 13px;
        color: #a855f7;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 25px;
        font-weight: 800;
        font-family: 'Montserrat', sans-serif;
    }
    
    .hero-title {
        font-size: 100px;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: -3px;
        animation: titleGlow 3s ease-in-out infinite;
    }
    
    .hero-title span {
        background: linear-gradient(135deg, #a855f7 0%, #d946ef 50%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% 200%;
    }
    
    .hero-desc {
        font-size: 18px;
        color: #c4b5fd;
        max-width: 650px;
        margin: 0 auto 70px;
        line-height: 1.9;
        font-weight: 400;
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: 0.5px;
    }
    
    .hero-cta {
        display: flex;
        gap: 25px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #a855f7 0%, #d946ef 100%);
        color: #ffffff;
        padding: 18px 55px;
        border: none;
        border-radius: 6px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 30px rgba(168, 85, 247, 0.4);
        font-family: 'Montserrat', sans-serif;
    }
    
    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 60px rgba(168, 85, 247, 0.7);
    }
    
    .btn-secondary {
        background: transparent;
        color: #a855f7;
        padding: 18px 55px;
        border: 2px solid #a855f7;
        border-radius: 6px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Montserrat', sans-serif;
    }
    
    .btn-secondary:hover {
        background: rgba(168, 85, 247, 0.1);
        box-shadow: 0 0 30px rgba(168, 85, 247, 0.3);
    }
    
    /* STATS SECTION */
    .stats-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a0f2e 0%, #0f0a1a 100%);
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 50px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .stat-box {
        text-align: center;
        padding: 50px;
        border: 2px solid rgba(168, 85, 247, 0.2);
        border-radius: 8px;
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.05), rgba(217, 70, 239, 0.02));
        animation: slideInMagic 0.8s ease-out;
        animation-fill-mode: both;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-box:nth-child(1) { animation-delay: 0.1s; }
    .stat-box:nth-child(2) { animation-delay: 0.2s; }
    .stat-box:nth-child(3) { animation-delay: 0.3s; }
    .stat-box:nth-child(4) { animation-delay: 0.4s; }
    
    .stat-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(168, 85, 247, 0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .stat-box:hover::before { left: 100%; }
    
    .stat-box:hover {
        border-color: #a855f7;
        box-shadow: 0 0 50px rgba(168, 85, 247, 0.3);
        transform: translateY(-10px);
    }
    
    .stat-number {
        font-size: 64px;
        font-weight: 900;
        background: linear-gradient(135deg, #a855f7, #d946ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        font-family: 'Playfair Display', serif;
    }
    
    .stat-label {
        font-size: 13px;
        color: #c4b5fd;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* SERVICES SECTION */
    .services-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0f0a1a 0%, #1a0f2e 100%);
    }
    
    .section-title {
        font-size: 72px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 120px;
        font-family: 'Playfair Display', serif;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #a855f7, #d946ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 50px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .service-card {
        padding: 60px 50px;
        border: 2px solid rgba(168, 85, 247, 0.2);
        border-radius: 8px;
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.05), rgba(217, 70, 239, 0.02));
        transition: all 0.4s ease;
        animation: slideInMagic 0.8s ease-out;
        animation-fill-mode: both;
        position: relative;
        overflow: hidden;
    }
    
    .service-card:nth-child(1) { animation-delay: 0.1s; }
    .service-card:nth-child(2) { animation-delay: 0.2s; }
    .service-card:nth-child(3) { animation-delay: 0.3s; }
    
    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(168, 85, 247, 0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .service-card:hover::before { left: 100%; }
    
    .service-card:hover {
        border-color: #a855f7;
        box-shadow: 0 0 60px rgba(168, 85, 247, 0.4);
        transform: translateY(-15px);
    }
    
    .service-icon {
        font-size: 56px;
        margin-bottom: 30px;
    }
    
    .service-title {
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 20px;
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        letter-spacing: -0.5px;
    }
    
    .service-desc {
        font-size: 15px;
        color: #c4b5fd;
        line-height: 1.9;
        font-family: 'Cormorant Garamond', serif;
    }
    
    /* PORTFOLIO SECTION */
    .portfolio-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a0f2e 0%, #0f0a1a 100%);
    }
    
    .portfolio-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 50px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .portfolio-item {
        position: relative;
        height: 450px;
        border-radius: 8px;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(217, 70, 239, 0.05));
        border: 2px solid rgba(168, 85, 247, 0.2);
        cursor: pointer;
        transition: all 0.4s ease;
        animation: slideInMagic 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .portfolio-item:nth-child(1) { animation-delay: 0.1s; }
    .portfolio-item:nth-child(2) { animation-delay: 0.2s; }
    .portfolio-item:nth-child(3) { animation-delay: 0.3s; }
    .portfolio-item:nth-child(4) { animation-delay: 0.4s; }
    
    .portfolio-item:hover {
        transform: translateY(-20px);
        border-color: #a855f7;
        box-shadow: 0 0 70px rgba(168, 85, 247, 0.4);
    }
    
    .portfolio-image {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 100px;
        position: relative;
    }
    
    .portfolio-content {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 50px;
        background: linear-gradient(180deg, transparent 0%, rgba(15, 10, 26, 0.95) 100%);
        transform: translateY(60px);
        transition: transform 0.4s ease;
    }
    
    .portfolio-item:hover .portfolio-content {
        transform: translateY(0);
    }
    
    .portfolio-title {
        font-size: 24px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
        font-family: 'Montserrat', sans-serif;
    }
    
    .portfolio-desc {
        font-size: 14px;
        color: #c4b5fd;
        font-family: 'Cormorant Garamond', serif;
    }
    
    /* CTA SECTION */
    .cta-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #a855f7 0%, #d946ef 100%);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(15, 10, 26, 0.15);
    }
    
    .cta-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-title {
        font-size: 64px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: -2px;
    }
    
    .cta-desc {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.95);
        max-width: 700px;
        margin: 0 auto 60px;
        font-family: 'Cormorant Garamond', serif;
    }
    
    .cta-btn {
        background: #0f0a1a;
        color: #a855f7;
        padding: 18px 65px;
        border: 2px solid #0f0a1a;
        border-radius: 6px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Montserrat', sans-serif;
    }
    
    .cta-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 40px rgba(15, 10, 26, 0.4);
    }
    
    /* FOOTER */
    .footer {
        background: #0f0a1a;
        color: #c4b5fd;
        padding: 80px;
        text-align: center;
        border-top: 2px solid rgba(168, 85, 247, 0.2);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(168, 85, 247, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Montserrat', sans-serif;
    }
    
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .navbar-nav { gap: 20px; }
        .hero { padding: 50px 20px; min-height: auto; }
        .hero-title { font-size: 52px; }
        .stats-section { grid-template-columns: repeat(2, 1fr); padding: 80px 20px; }
        .services-grid { grid-template-columns: 1fr; gap: 30px; }
        .portfolio-grid { grid-template-columns: 1fr; }
        .cta-section { padding: 100px 20px; }
        .cta-title { font-size: 42px; }
        .section-title { font-size: 42px; }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">VIOLETA</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Sobre</a>
        <a href="#" class="nav-link">Serviços</a>
        <a href="#" class="nav-link">Portfolio</a>
        <a href="#" class="nav-link">Contato</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-container">
        <div class="hero-label">Bem-vindo</div>
        <div class="hero-title">Criatividade <span>Sem Limites</span></div>
        <div class="hero-desc">Transformando ideias em experiências visuais extraordinárias. Design sofisticado que cativa, inspira e converte.</div>
        <div class="hero-cta">
            <button class="btn-primary">Começar Projeto</button>
            <button class="btn-secondary">Explorar Trabalhos</button>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# STATS
stats_html = '''<div class="stats-section">
    <div class="stat-box">
        <div class="stat-number">200+</div>
        <div class="stat-label">Projetos Criados</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">99%</div>
        <div class="stat-label">Satisfação</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">15+</div>
        <div class="stat-label">Anos Experiência</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">100M+</div>
        <div class="stat-label">Impacto Gerado</div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# SERVICES
services_html = '''<div class="services-section">
    <div class="section-title">Serviços Premium</div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-icon">🎨</div>
            <div class="service-title">Design Estratégico</div>
            <div class="service-desc">Criação de identidades visuais que comunicam valor e estabelecem conexão emocional com seu público.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">✨</div>
            <div class="service-title">Experiência Digital</div>
            <div class="service-desc">Interfaces intuitivas e envolventes que transformam usuários em defensores da sua marca.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">🚀</div>
            <div class="service-title">Inovação Criativa</div>
            <div class="service-desc">Soluções originais que desafiam convenções e estabelecem novos padrões no mercado.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# PORTFOLIO
portfolio_html = '''<div class="portfolio-section">
    <div class="section-title">Trabalhos em Destaque</div>
    <div class="portfolio-grid">
        <div class="portfolio-item">
            <div class="portfolio-image">💎</div>
            <div class="portfolio-content">
                <div class="portfolio-title">Luxury Brand</div>
                <div class="portfolio-desc">Rebranding completo para marca premium global.</div>
            </div>
        </div>
        <div class="portfolio-item">
            <div class="portfolio-image">🌟</div>
            <div class="portfolio-content">
                <div class="portfolio-title">Digital Platform</div>
                <div class="portfolio-desc">Plataforma SaaS com 50K+ usuários ativos.</div>
            </div>
        </div>
        <div class="portfolio-item">
            <div class="portfolio-image">🎯</div>
            <div class="portfolio-content">
                <div class="portfolio-title">Marketing Campaign</div>
                <div class="portfolio-desc">Campanha viral com 10M+ impressões.</div>
            </div>
        </div>
        <div class="portfolio-item">
            <div class="portfolio-image">🏆</div>
            <div class="portfolio-content">
                <div class="portfolio-title">Brand Identity</div>
                <div class="portfolio-desc">Sistema visual completo e guidelines.</div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(portfolio_html, unsafe_allow_html=True)

# CTA
cta_html = '''<div class="cta-section">
    <div class="cta-content">
        <div class="cta-title">Vamos Criar Juntos?</div>
        <div class="cta-desc">Transforme sua visão em uma realidade visual extraordinária que impacta e inspira.</div>
        <button class="cta-btn">Iniciar Agora</button>
    </div>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-text">Email: contato@violeta.com | Telefone: +55 (11) 98765-4321</div>
    <div class="footer-text">Instagram: @violeta.design | Portfolio: violeta.com</div>
    <div class="footer-copyright">© 2025 Violeta Design. Todos os direitos reservados.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
