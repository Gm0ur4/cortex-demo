import streamlit as st

st.set_page_config(
    page_title="GetResponse Style - Email Marketing",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #ffffff;
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
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    /* NAVBAR */
    .navbar {
        background: #ffffff;
        padding: 20px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e0e0e0;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .navbar-logo {
        font-size: 20px;
        font-weight: 800;
        color: #0066FF;
        letter-spacing: 1px;
        font-family: 'Poppins', sans-serif;
    }
    
    .navbar-nav {
        display: flex;
        gap: 50px;
    }
    
    .nav-link {
        color: #1a1a1a;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        text-transform: capitalize;
        transition: all 0.3s ease;
    }
    
    .nav-link:hover { color: #0066FF; }
    
    .navbar-cta {
        display: flex;
        gap: 20px;
        align-items: center;
    }
    
    .nav-login {
        color: #1a1a1a;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
    }
    
    .nav-btn {
        background: #0066FF;
        color: #ffffff;
        padding: 12px 30px;
        border: none;
        border-radius: 4px;
        font-weight: 700;
        font-size: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .nav-btn:hover {
        background: #0052CC;
    }
    
    /* HERO */
    .hero {
        background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);
        color: #ffffff;
        padding: 120px 80px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
    }
    
    .hero-content {
        max-width: 700px;
        position: relative;
        z-index: 2;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .hero-label {
        font-size: 13px;
        color: rgba(255, 255, 255, 0.9);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
        font-weight: 600;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 30px;
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
        letter-spacing: -1px;
    }
    
    .hero-desc {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.95);
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
        background: #FFD60A;
        color: #1a1a1a;
        padding: 16px 50px;
        border: none;
        border-radius: 4px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-primary:hover {
        background: #FFC700;
        transform: translateY(-2px);
    }
    
    .btn-secondary {
        background: transparent;
        color: #ffffff;
        padding: 16px 50px;
        border: 2px solid #ffffff;
        border-radius: 4px;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-secondary:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    .hero-visual {
        position: relative;
        z-index: 2;
        width: 500px;
        height: 500px;
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 100px;
        animation: slideInRight 0.8s ease-out;
        backdrop-filter: blur(10px);
    }
    
    /* STATS SECTION */
    .stats-section {
        background: #0066FF;
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
        text-align: center;
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
        font-size: 14px;
        color: rgba(255, 255, 255, 0.9);
        font-weight: 600;
        line-height: 1.6;
    }
    
    /* FEATURES SECTION */
    .features-section {
        background: #ffffff;
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
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 50px;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    .feature-card {
        padding: 60px 40px;
        background: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        transition: all 0.4s ease;
        animation: fadeInUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .feature-card:nth-child(1) { animation-delay: 0.1s; }
    .feature-card:nth-child(2) { animation-delay: 0.2s; }
    .feature-card:nth-child(3) { animation-delay: 0.3s; }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0, 102, 255, 0.1);
        border-color: #0066FF;
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 25px;
    }
    
    .feature-title {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
    }
    
    .feature-desc {
        font-size: 14px;
        color: #666666;
        line-height: 1.8;
    }
    
    /* TESTIMONIAL SECTION */
    .testimonial-section {
        background: #f8f9fa;
        padding: 100px 80px;
        text-align: center;
    }
    
    .testimonial-card {
        background: #ffffff;
        padding: 60px;
        border-radius: 8px;
        max-width: 800px;
        margin: 0 auto;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        animation: fadeInUp 0.8s ease-out;
    }
    
    .testimonial-text {
        font-size: 18px;
        color: #1a1a1a;
        margin-bottom: 30px;
        line-height: 1.8;
        font-weight: 500;
    }
    
    .testimonial-author {
        font-size: 14px;
        color: #666666;
        font-weight: 600;
    }
    
    /* CTA SECTION */
    .cta-section {
        background: #ffffff;
        padding: 100px 80px;
        text-align: center;
    }
    
    .cta-title {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 30px;
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
    }
    
    .cta-form {
        max-width: 600px;
        margin: 0 auto;
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    .cta-input {
        flex: 1;
        padding: 16px 20px;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        font-size: 14px;
        font-family: 'Montserrat', sans-serif;
    }
    
    .cta-btn {
        background: #0066FF;
        color: #ffffff;
        padding: 16px 40px;
        border: none;
        border-radius: 4px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .cta-btn:hover {
        background: #0052CC;
    }
    
    .cta-note {
        font-size: 12px;
        color: #999999;
        margin-top: 15px;
    }
    
    /* FOOTER */
    .footer {
        background: #0a0a0a;
        color: #999999;
        padding: 80px 80px;
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
    
    .footer-col a:hover { color: #0066FF; }
    
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
        .features-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: repeat(2, 1fr); }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">GetResponse</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Produto</a>
        <a href="#" class="nav-link">Recursos</a>
        <a href="#" class="nav-link">Preços</a>
        <a href="#" class="nav-link">Sobre</a>
    </div>
    <div class="navbar-cta">
        <a href="#" class="nav-login">Fazer login</a>
        <button class="nav-btn">Inscreva-se grátis</button>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-content">
        <div class="hero-label">Email Marketing & Automação</div>
        <div class="hero-title">Não é você, é o algoritmo</div>
        <div class="hero-desc">Plataforma de email marketing, automação e landing pages com IA integrada. Crie, teste e venda mais rápido.</div>
        <div class="hero-cta">
            <button class="btn-primary">Comece Grátis</button>
            <button class="btn-secondary">Saiba Mais</button>
        </div>
    </div>
    <div class="hero-visual">📧</div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# STATS
stats_html = '''<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-number">99%</div>
            <div class="stat-label">Taxa de Entregabilidade para 160+ países</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">+150</div>
            <div class="stat-label">Integrações Disponíveis</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">350K+</div>
            <div class="stat-label">Clientes ao Redor do Mundo</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Suporte de Sucesso do Cliente</div>
        </div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# FEATURES
features_html = '''<div class="features-section">
    <div class="section-title">Ferramentas Poderosas para Seu Negócio</div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">📧</div>
            <div class="feature-title">Email Marketing</div>
            <div class="feature-desc">Envie newsletters ilimitadas com IA que cria linhas de assunto e personaliza conteúdo para seu público.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">Automação com IA</div>
            <div class="feature-desc">Crie jornadas automáticas que identificam o melhor momento para contatar seus clientes.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌐</div>
            <div class="feature-title">Landing Pages</div>
            <div class="feature-desc">Publique landing pages ilimitadas com IA que escreve o texto e escolhe o layout ideal.</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# TESTIMONIAL
testimonial_html = '''<div class="testimonial-section">
    <div class="testimonial-card">
        <div class="testimonial-text">"Geramos US$ 43.000 em vendas com apenas 10 e-mails usando a GetResponse. A automação e a IA mudaram nosso negócio."</div>
        <div class="testimonial-author">João Silva - CEO da Tech Company</div>
    </div>
</div>'''
st.markdown(testimonial_html, unsafe_allow_html=True)

# CTA
cta_html = '''<div class="cta-section">
    <div class="cta-title">Junte-se a 350.000+ Empresas</div>
    <div class="cta-form">
        <input type="email" class="cta-input" placeholder="Seu endereço de e-mail">
        <button class="cta-btn">Começar Grátis</button>
    </div>
    <div class="cta-note">Teste gratuito de 14 dias | Não precisa de cartão | Cancele a qualquer momento</div>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-grid">
        <div class="footer-col">
            <h4>Produto</h4>
            <a href="#">Email Marketing</a>
            <a href="#">Automação</a>
            <a href="#">Landing Pages</a>
            <a href="#">Formulários</a>
        </div>
        <div class="footer-col">
            <h4>Recursos</h4>
            <a href="#">Blog</a>
            <a href="#">Webinars</a>
            <a href="#">Templates</a>
            <a href="#">Integrações</a>
        </div>
        <div class="footer-col">
            <h4>Empresa</h4>
            <a href="#">Sobre Nós</a>
            <a href="#">Carreiras</a>
            <a href="#">Imprensa</a>
            <a href="#">Contato</a>
        </div>
        <div class="footer-col">
            <h4>Legal</h4>
            <a href="#">Privacidade</a>
            <a href="#">Termos</a>
            <a href="#">Cookies</a>
            <a href="#">Suporte</a>
        </div>
    </div>
    <div class="footer-bottom">
        © 2025 GetResponse. Todos os direitos reservados.
    </div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
