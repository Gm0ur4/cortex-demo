import streamlit as st

st.set_page_config(
    page_title="Corporativo Premium - Ambev Style",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);
        font-family: 'Montserrat', sans-serif;
        color: #1a1a1a;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    @keyframes slideInLeft {
        0% { transform: translateX(-100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        0% { transform: translateX(100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeInUp {
        0% { transform: translateY(40px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes scaleIn {
        0% { transform: scale(0.95); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes borderFlow {
        0% { border-left-color: #e0e0e0; }
        50% { border-left-color: #1a1a1a; }
        100% { border-left-color: #e0e0e0; }
    }
    
    /* NAVBAR */
    .navbar {
        background: #ffffff;
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e0e0e0;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 800;
        color: #1a1a1a;
        letter-spacing: 1px;
        font-family: 'Poppins', sans-serif;
    }
    
    .navbar-nav {
        display: flex;
        gap: 60px;
    }
    
    .nav-link {
        color: #666666;
        text-decoration: none;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        position: relative;
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
    
    .nav-link:hover { color: #1a1a1a; }
    .nav-link:hover::after { width: 100%; }
    
    /* HERO */
    .hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 100px 80px;
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.05) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
    }
    
    .hero-content {
        max-width: 650px;
        position: relative;
        z-index: 2;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .hero-label {
        font-size: 12px;
        color: #999999;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
        font-weight: 600;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 30px;
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
        letter-spacing: -1px;
    }
    
    .hero-desc {
        font-size: 16px;
        color: #666666;
        margin-bottom: 50px;
        line-height: 1.8;
        font-weight: 400;
    }
    
    .hero-cta {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }
    
    .btn-primary {
        background: #1a1a1a;
        color: #ffffff;
        padding: 16px 50px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-primary:hover {
        background: #333333;
        transform: translateY(-2px);
    }
    
    .btn-secondary {
        background: transparent;
        color: #1a1a1a;
        padding: 16px 50px;
        border: 2px solid #1a1a1a;
        border-radius: 2px;
        font-weight: 700;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
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
        width: 500px;
        height: 500px;
        background: linear-gradient(135deg, #f0f0f0 0%, #e8e8e8 100%);
        border: 1px solid #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 100px;
        animation: slideInRight 0.8s ease-out;
    }
    
    /* STATS SECTION */
    .stats-section {
        background: #1a1a1a;
        color: #ffffff;
        padding: 100px 80px;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 60px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .stat-item {
        animation: fadeInUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .stat-item:nth-child(1) { animation-delay: 0.1s; }
    .stat-item:nth-child(2) { animation-delay: 0.2s; }
    .stat-item:nth-child(3) { animation-delay: 0.3s; }
    .stat-item:nth-child(4) { animation-delay: 0.4s; }
    
    .stat-number {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }
    
    .stat-label {
        font-size: 13px;
        color: #cccccc;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* SERVICES SECTION */
    .services-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);
        padding: 150px 80px;
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 100px;
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
        letter-spacing: -1px;
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 50px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .service-card {
        padding: 60px 40px;
        background: #ffffff;
        border-left: 4px solid #1a1a1a;
        transition: all 0.4s ease;
        animation: fadeInUp 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .service-card:nth-child(1) { animation-delay: 0.1s; }
    .service-card:nth-child(2) { animation-delay: 0.2s; }
    .service-card:nth-child(3) { animation-delay: 0.3s; }
    
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
        border-left-color: #666666;
    }
    
    .service-icon {
        font-size: 48px;
        margin-bottom: 25px;
    }
    
    .service-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
    }
    
    .service-desc {
        font-size: 14px;
        color: #666666;
        line-height: 1.8;
    }
    
    /* PORTFOLIO SECTION */
    .portfolio-section {
        background: linear-gradient(135deg, #f0f2f5 0%, #f8f9fa 100%);
        padding: 150px 80px;
    }
    
    .portfolio-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 60px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .portfolio-item {
        padding: 80px 60px;
        background: #ffffff;
        border: 1px solid #e0e0e0;
        transition: all 0.4s ease;
        animation: scaleIn 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .portfolio-item:nth-child(1) { animation-delay: 0.1s; }
    .portfolio-item:nth-child(2) { animation-delay: 0.2s; }
    .portfolio-item:nth-child(3) { animation-delay: 0.3s; }
    .portfolio-item:nth-child(4) { animation-delay: 0.4s; }
    
    .portfolio-item:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.1);
        border-color: #1a1a1a;
    }
    
    .portfolio-number {
        font-size: 48px;
        font-weight: 900;
        color: #e0e0e0;
        margin-bottom: 20px;
        font-family: 'Poppins', sans-serif;
    }
    
    .portfolio-title {
        font-size: 24px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }
    
    .portfolio-desc {
        font-size: 14px;
        color: #666666;
        line-height: 1.8;
    }
    
    /* CTA SECTION */
    .cta-section {
        background: #1a1a1a;
        color: #ffffff;
        padding: 120px 80px;
        text-align: center;
    }
    
    .cta-title {
        font-size: 52px;
        font-weight: 800;
        margin-bottom: 30px;
        font-family: 'Poppins', sans-serif;
        letter-spacing: -1px;
    }
    
    .cta-desc {
        font-size: 16px;
        color: #cccccc;
        max-width: 700px;
        margin: 0 auto 50px;
    }
    
    .cta-btn {
        background: #ffffff;
        color: #1a1a1a;
        padding: 16px 60px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .cta-btn:hover {
        background: #e0e0e0;
        transform: translateY(-2px);
    }
    
    /* FOOTER */
    .footer {
        background: #0a0a0a;
        color: #999999;
        padding: 80px 80px;
        border-top: 1px solid #333333;
    }
    
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 60px;
        max-width: 1600px;
        margin: 0 auto 60px;
    }
    
    .footer-col h4 {
        color: #ffffff;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }
    
    .footer-col a {
        display: block;
        color: #999999;
        text-decoration: none;
        font-size: 13px;
        margin-bottom: 12px;
        transition: color 0.3s ease;
    }
    
    .footer-col a:hover { color: #ffffff; }
    
    .footer-bottom {
        text-align: center;
        padding-top: 40px;
        border-top: 1px solid #333333;
        font-size: 12px;
    }
    
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .hero { flex-direction: column; padding: 50px 20px; }
        .hero-title { font-size: 42px; }
        .hero-visual { width: 100%; margin-top: 40px; }
        .stats-grid { grid-template-columns: repeat(2, 1fr); }
        .services-grid { grid-template-columns: 1fr; }
        .portfolio-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: repeat(2, 1fr); }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">CORPORATIVO</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Sobre</a>
        <a href="#" class="nav-link">Serviços</a>
        <a href="#" class="nav-link">Portfólio</a>
        <a href="#" class="nav-link">Contato</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-content">
        <div class="hero-label">Bem-vindo</div>
        <div class="hero-title">Excelência em Cada Detalhe</div>
        <div class="hero-desc">Soluções corporativas que transformam negócios. Expertise, inovação e resultados mensuráveis.</div>
        <div class="hero-cta">
            <button class="btn-primary">Começar</button>
            <button class="btn-secondary">Saiba Mais</button>
        </div>
    </div>
    <div class="hero-visual">📊</div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# STATS
stats_html = '''<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-number">500+</div>
            <div class="stat-label">Projetos Realizados</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">98%</div>
            <div class="stat-label">Satisfação de Clientes</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">25+</div>
            <div class="stat-label">Anos de Experiência</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">150+</div>
            <div class="stat-label">Profissionais Especializados</div>
        </div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# SERVICES
services_html = '''<div class="services-section">
    <div class="section-title">Nossos Serviços</div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-icon">🎯</div>
            <div class="service-title">Consultoria Estratégica</div>
            <div class="service-desc">Análise profunda de mercado e desenvolvimento de estratégias personalizadas para seu negócio.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">💼</div>
            <div class="service-title">Gestão Corporativa</div>
            <div class="service-desc">Otimização de processos e implementação de sistemas para máxima eficiência operacional.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">📈</div>
            <div class="service-title">Transformação Digital</div>
            <div class="service-desc">Modernização tecnológica e adaptação digital para o futuro dos negócios.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# PORTFOLIO
portfolio_html = '''<div class="portfolio-section">
    <div class="section-title">Casos de Sucesso</div>
    <div class="portfolio-grid">
        <div class="portfolio-item">
            <div class="portfolio-number">01</div>
            <div class="portfolio-title">Empresa Tecnológica</div>
            <div class="portfolio-desc">Crescimento de 300% em receita através de estratégia digital integrada e otimização operacional.</div>
        </div>
        <div class="portfolio-item">
            <div class="portfolio-number">02</div>
            <div class="portfolio-title">Indústria de Manufatura</div>
            <div class="portfolio-desc">Redução de custos em 45% com implementação de sistemas de gestão modernos.</div>
        </div>
        <div class="portfolio-item">
            <div class="portfolio-number">03</div>
            <div class="portfolio-title">Setor Financeiro</div>
            <div class="portfolio-desc">Transformação digital completa com aumento de eficiência de 80% nos processos.</div>
        </div>
        <div class="portfolio-item">
            <div class="portfolio-number">04</div>
            <div class="portfolio-title">Varejo Premium</div>
            <div class="portfolio-desc">Experiência de cliente revolucionária gerando aumento de 120% em vendas.</div>
        </div>
    </div>
</div>'''
st.markdown(portfolio_html, unsafe_allow_html=True)

# CTA
cta_html = '''<div class="cta-section">
    <div class="cta-title">Pronto para Transformar seu Negócio?</div>
    <div class="cta-desc">Entre em contato conosco e descubra como podemos impulsionar seu crescimento.</div>
    <button class="cta-btn">Solicitar Consulta</button>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-grid">
        <div class="footer-col">
            <h4>Empresa</h4>
            <a href="#">Sobre Nós</a>
            <a href="#">Carreira</a>
            <a href="#">Imprensa</a>
            <a href="#">Blog</a>
        </div>
        <div class="footer-col">
            <h4>Serviços</h4>
            <a href="#">Consultoria</a>
            <a href="#">Gestão</a>
            <a href="#">Tecnologia</a>
            <a href="#">Treinamento</a>
        </div>
        <div class="footer-col">
            <h4>Recursos</h4>
            <a href="#">Documentação</a>
            <a href="#">Guias</a>
            <a href="#">Webinars</a>
            <a href="#">Suporte</a>
        </div>
        <div class="footer-col">
            <h4>Contato</h4>
            <a href="#">contato@corporativo.com.br</a>
            <a href="#">+55 (11) 98765-4321</a>
            <a href="#">São Paulo, Brasil</a>
            <a href="#">LinkedIn</a>
        </div>
    </div>
    <div class="footer-bottom">
        © 2025 Corporativo Premium. Todos os direitos reservados.
    </div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
