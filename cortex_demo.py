import streamlit as st

st.set_page_config(
    page_title="Portfolio Premium - Profissional de Elite",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    /* ANIMAÇÕES */
    @keyframes textReveal {
        0% { clip-path: inset(0 100% 0 0); }
        100% { clip-path: inset(0 0 0 0); }
    }
    
    @keyframes numberCounter {
        0% { transform: translateY(30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes floatSoft {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes borderGlowCycle {
        0%, 100% { border-color: rgba(100, 200, 255, 0.3); }
        50% { border-color: rgba(100, 200, 255, 0.8); }
    }
    
    @keyframes slideFromLeft {
        0% { transform: translateX(-100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideFromRight {
        0% { transform: translateX(100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes scaleInCenter {
        0% { transform: scale(0.8); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* NAVBAR */
    .navbar {
        background: rgba(10, 14, 39, 0.95);
        backdrop-filter: blur(30px);
        padding: 20px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(100, 200, 255, 0.15);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(90deg, #64c8ff 0%, #0099ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Syne', sans-serif;
        letter-spacing: 2px;
    }
    
    .navbar-nav {
        display: flex;
        gap: 60px;
    }
    
    .nav-link {
        color: #a0b0d0;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #64c8ff, #0099ff);
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after { width: 100%; }
    .nav-link:hover { color: #64c8ff; }
    
    /* HERO SECTION - NOVO DESIGN */
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
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(100, 200, 255, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        top: -300px;
        right: -300px;
        animation: floatSoft 8s ease-in-out infinite;
    }
    
    .hero::after {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(0, 153, 255, 0.05) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -200px;
        left: -200px;
        animation: floatSoft 10s ease-in-out infinite reverse;
    }
    
    .hero-container {
        max-width: 1000px;
        text-align: center;
        position: relative;
        z-index: 2;
    }
    
    .hero-label {
        font-size: 14px;
        color: #64c8ff;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
        font-weight: 700;
    }
    
    .hero-title {
        font-size: 92px;
        font-weight: 800;
        line-height: 1;
        margin-bottom: 30px;
        font-family: 'Syne', sans-serif;
        letter-spacing: -2px;
        animation: textReveal 1.2s ease-out;
    }
    
    .hero-title span {
        background: linear-gradient(135deg, #64c8ff 0%, #0099ff 50%, #64c8ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% 200%;
        animation: gradientFlow 4s ease infinite;
    }
    
    .hero-desc {
        font-size: 18px;
        color: #a0b0d0;
        max-width: 600px;
        margin: 0 auto 60px;
        line-height: 1.8;
        font-weight: 400;
    }
    
    .hero-cta {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #64c8ff 0%, #0099ff 100%);
        color: #0a0e27;
        padding: 16px 50px;
        border: none;
        border-radius: 4px;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 30px rgba(100, 200, 255, 0.3);
    }
    
    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 50px rgba(100, 200, 255, 0.6);
    }
    
    .btn-secondary {
        background: transparent;
        color: #64c8ff;
        padding: 16px 50px;
        border: 2px solid #64c8ff;
        border-radius: 4px;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-secondary:hover {
        background: rgba(100, 200, 255, 0.1);
        box-shadow: 0 0 30px rgba(100, 200, 255, 0.3);
    }
    
    /* STATS SECTION - ELEMENTO NOVO */
    .stats-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1f3a 0%, #0a0e27 100%);
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .stat-box {
        text-align: center;
        padding: 40px;
        border-left: 4px solid #64c8ff;
        animation: slideFromLeft 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .stat-box:nth-child(1) { animation-delay: 0.1s; }
    .stat-box:nth-child(2) { animation-delay: 0.2s; }
    .stat-box:nth-child(3) { animation-delay: 0.3s; }
    .stat-box:nth-child(4) { animation-delay: 0.4s; }
    
    .stat-number {
        font-size: 56px;
        font-weight: 800;
        background: linear-gradient(135deg, #64c8ff, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
        font-family: 'Syne', sans-serif;
    }
    
    .stat-label {
        font-size: 14px;
        color: #a0b0d0;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* EXPERTISE SECTION - ELEMENTO NOVO */
    .expertise-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 100px;
        font-family: 'Syne', sans-serif;
        letter-spacing: -1px;
    }
    
    .expertise-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 50px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .expertise-item {
        padding: 50px;
        border: 1px solid rgba(100, 200, 255, 0.2);
        border-radius: 8px;
        background: linear-gradient(135deg, rgba(100, 200, 255, 0.05), rgba(0, 153, 255, 0.02));
        transition: all 0.4s ease;
        animation: scaleInCenter 0.8s ease-out;
        animation-fill-mode: both;
        position: relative;
        overflow: hidden;
    }
    
    .expertise-item:nth-child(1) { animation-delay: 0.1s; }
    .expertise-item:nth-child(2) { animation-delay: 0.2s; }
    .expertise-item:nth-child(3) { animation-delay: 0.3s; }
    .expertise-item:nth-child(4) { animation-delay: 0.4s; }
    
    .expertise-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(100, 200, 255, 0.1), transparent);
        transition: left 0.6s ease;
    }
    
    .expertise-item:hover::before { left: 100%; }
    
    .expertise-item:hover {
        transform: translateY(-10px);
        border-color: #64c8ff;
        box-shadow: 0 0 40px rgba(100, 200, 255, 0.2);
    }
    
    .expertise-number {
        font-size: 48px;
        font-weight: 800;
        color: #64c8ff;
        margin-bottom: 20px;
        font-family: 'Syne', sans-serif;
    }
    
    .expertise-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #ffffff;
    }
    
    .expertise-desc {
        font-size: 15px;
        color: #a0b0d0;
        line-height: 1.8;
    }
    
    /* WORK SHOWCASE - ELEMENTO NOVO */
    .work-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1f3a 0%, #0a0e27 100%);
    }
    
    .work-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .work-item {
        position: relative;
        height: 400px;
        border-radius: 8px;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(100, 200, 255, 0.1), rgba(0, 153, 255, 0.05));
        border: 1px solid rgba(100, 200, 255, 0.2);
        cursor: pointer;
        transition: all 0.4s ease;
        animation: slideFromRight 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .work-item:nth-child(1) { animation-delay: 0.1s; }
    .work-item:nth-child(2) { animation-delay: 0.2s; }
    .work-item:nth-child(3) { animation-delay: 0.3s; }
    
    .work-item:hover {
        transform: translateY(-15px);
        border-color: #64c8ff;
        box-shadow: 0 0 50px rgba(100, 200, 255, 0.3);
    }
    
    .work-content {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 40px;
        background: linear-gradient(180deg, transparent 0%, rgba(10, 14, 39, 0.95) 100%);
        transform: translateY(50px);
        transition: transform 0.4s ease;
    }
    
    .work-item:hover .work-content {
        transform: translateY(0);
    }
    
    .work-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .work-desc {
        font-size: 14px;
        color: #a0b0d0;
    }
    
    /* CTA SECTION */
    .cta-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #64c8ff 0%, #0099ff 100%);
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
        background: rgba(10, 14, 39, 0.1);
    }
    
    .cta-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-title {
        font-size: 56px;
        font-weight: 800;
        color: #0a0e27;
        margin-bottom: 30px;
        font-family: 'Syne', sans-serif;
        letter-spacing: -1px;
    }
    
    .cta-desc {
        font-size: 18px;
        color: rgba(10, 14, 39, 0.9);
        max-width: 600px;
        margin: 0 auto 50px;
    }
    
    .cta-btn {
        background: #0a0e27;
        color: #64c8ff;
        padding: 18px 60px;
        border: 2px solid #0a0e27;
        border-radius: 4px;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .cta-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(10, 14, 39, 0.3);
    }
    
    /* FOOTER */
    .footer {
        background: #0a0e27;
        color: #a0b0d0;
        padding: 80px;
        text-align: center;
        border-top: 1px solid rgba(100, 200, 255, 0.15);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(100, 200, 255, 0.15);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .navbar-nav { gap: 20px; }
        .hero { padding: 50px 20px; min-height: auto; }
        .hero-title { font-size: 48px; }
        .stats-section { grid-template-columns: repeat(2, 1fr); padding: 80px 20px; }
        .expertise-grid { grid-template-columns: 1fr; gap: 30px; }
        .work-grid { grid-template-columns: 1fr; }
        .cta-section { padding: 100px 20px; }
        .cta-title { font-size: 36px; }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">ELITE</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Sobre</a>
        <a href="#" class="nav-link">Expertise</a>
        <a href="#" class="nav-link">Trabalhos</a>
        <a href="#" class="nav-link">Contato</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-container">
        <div class="hero-label">Bem-vindo</div>
        <div class="hero-title">Transformando <span>Visões</span> em Realidade</div>
        <div class="hero-desc">Especialista em criar soluções de impacto com design sofisticado e estratégia de negócio.</div>
        <div class="hero-cta">
            <button class="btn-primary">Iniciar Projeto</button>
            <button class="btn-secondary">Explorar Trabalhos</button>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# STATS
stats_html = '''<div class="stats-section">
    <div class="stat-box">
        <div class="stat-number">150+</div>
        <div class="stat-label">Projetos Entregues</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">98%</div>
        <div class="stat-label">Satisfação Clientes</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">12+</div>
        <div class="stat-label">Anos Experiência</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">50M+</div>
        <div class="stat-label">Impacto Gerado</div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# EXPERTISE
expertise_html = '''<div class="expertise-section">
    <div class="section-title">Expertise</div>
    <div class="expertise-grid">
        <div class="expertise-item">
            <div class="expertise-number">01</div>
            <div class="expertise-title">Estratégia Digital</div>
            <div class="expertise-desc">Desenvolvimento de estratégias robustas que transformam objetivos em resultados mensuráveis e crescimento sustentável.</div>
        </div>
        <div class="expertise-item">
            <div class="expertise-number">02</div>
            <div class="expertise-title">Design Premium</div>
            <div class="expertise-desc">Criação de interfaces sofisticadas que combinam estética com funcionalidade, elevando a experiência do usuário.</div>
        </div>
        <div class="expertise-item">
            <div class="expertise-number">03</div>
            <div class="expertise-title">Desenvolvimento</div>
            <div class="expertise-desc">Implementação de soluções técnicas escaláveis e performáticas usando tecnologias de ponta do mercado.</div>
        </div>
        <div class="expertise-item">
            <div class="expertise-number">04</div>
            <div class="expertise-title">Consultoria</div>
            <div class="expertise-desc">Orientação estratégica para empresas que buscam inovação, transformação digital e posicionamento de mercado.</div>
        </div>
    </div>
</div>'''
st.markdown(expertise_html, unsafe_allow_html=True)

# WORK
work_html = '''<div class="work-section">
    <div class="section-title">Trabalhos em Destaque</div>
    <div class="work-grid">
        <div class="work-item">
            <div style="font-size: 120px; display: flex; align-items: center; justify-content: center; height: 100%;">🚀</div>
            <div class="work-content">
                <div class="work-title">Plataforma SaaS</div>
                <div class="work-desc">Solução completa de gestão empresarial com impacto em 10K+ usuários.</div>
            </div>
        </div>
        <div class="work-item">
            <div style="font-size: 120px; display: flex; align-items: center; justify-content: center; height: 100%;">💎</div>
            <div class="work-content">
                <div class="work-title">Marca Luxury</div>
                <div class="work-desc">Rebranding completo para marca premium com presença global.</div>
            </div>
        </div>
        <div class="work-item">
            <div style="font-size: 120px; display: flex; align-items: center; justify-content: center; height: 100%;">📊</div>
            <div class="work-content">
                <div class="work-title">Analytics Platform</div>
                <div class="work-desc">Dashboard inteligente para análise de dados em tempo real.</div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(work_html, unsafe_allow_html=True)

# CTA
cta_html = '''<div class="cta-section">
    <div class="cta-content">
        <div class="cta-title">Pronto para Crescer?</div>
        <div class="cta-desc">Vamos transformar sua visão em uma solução que gera resultados reais e impacto mensurável.</div>
        <button class="cta-btn">Conversar Agora</button>
    </div>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-text">Email: contato@elite.com | Telefone: +55 (11) 98765-4321</div>
    <div class="footer-text">LinkedIn: linkedin.com/in/seu-perfil | Portfólio: seu-site.com</div>
    <div class="footer-copyright">© 2025 Elite Portfolio. Todos os direitos reservados.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
