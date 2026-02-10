import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Premium Card - Gestão Completa de Benefícios",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS PREMIUM COM DESIGN MEGAVALE
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #0a0a0a;
        font-family: 'Montserrat', sans-serif;
        color: #ffffff;
        line-height: 1.6;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ANIMAÇÕES PREMIUM */
    @keyframes slideInDown {
        from { transform: translateY(-50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes slideInUp {
        from { transform: translateY(50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes scaleIn {
        from { transform: scale(0.95); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    @keyframes dashAnimation {
        0% { stroke-dashoffset: 1000; }
        100% { stroke-dashoffset: 0; }
    }
    
    @keyframes borderPulse {
        0%, 100% { border-color: rgba(0, 208, 132, 0.3); box-shadow: 0 0 15px rgba(0, 208, 132, 0.1); }
        50% { border-color: rgba(0, 208, 132, 0.8); box-shadow: 0 0 30px rgba(0, 208, 132, 0.3); }
    }
    
    @keyframes colorShift {
        0% { border-color: rgba(0, 180, 216, 0.5); }
        25% { border-color: rgba(255, 213, 10, 0.5); }
        50% { border-color: rgba(0, 208, 132, 0.5); }
        75% { border-color: rgba(255, 107, 74, 0.5); }
        100% { border-color: rgba(0, 180, 216, 0.5); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* NAVBAR PREMIUM */
    .navbar {
        background: rgba(10, 10, 10, 0.98);
        backdrop-filter: blur(20px);
        padding: 20px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px dashed rgba(0, 208, 132, 0.3);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        animation: slideInDown 0.6s ease-out;
    }
    
    .navbar-logo {
        font-size: 28px;
        font-weight: 900;
        background: linear-gradient(135deg, #00D084, #FF6B4A, #FFD60A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px;
        animation: float 3s ease-in-out infinite;
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
        letter-spacing: 1px;
        position: relative;
        animation: slideInDown 0.8s ease-out;
    }
    
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #00D084, #FF6B4A);
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #00D084;
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, #FF6B4A, #FF8C73);
        color: white;
        padding: 12px 32px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: 2px solid #FF6B4A;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 107, 74, 0.3);
        animation: slideInRight 1s ease-out;
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 74, 0.5);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0a0a0a 100%);
        min-height: 700px;
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
        background: radial-gradient(circle, rgba(0, 208, 132, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        top: -100px;
        right: -100px;
        animation: float 4s ease-in-out infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(255, 107, 74, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -100px;
        left: -100px;
        animation: float 5s ease-in-out infinite;
    }
    
    .hero-content {
        text-align: center;
        z-index: 2;
        position: relative;
        max-width: 900px;
        animation: fadeIn 1s ease-out;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        margin-bottom: 20px;
        background: linear-gradient(135deg, #00D084, #00B4D8, #FFD60A, #FF6B4A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        line-height: 1.1;
        animation: slideInUp 0.8s ease-out;
    }
    
    .hero-subtitle {
        font-size: 24px;
        font-weight: 300;
        margin-bottom: 50px;
        color: #00D084;
        letter-spacing: 1px;
        animation: slideInUp 1s ease-out;
    }
    
    .hero-cta {
        background: linear-gradient(135deg, #00D084, #00B4D8);
        color: white;
        padding: 18px 50px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid #00D084;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 25px rgba(0, 208, 132, 0.3);
        animation: slideInUp 1.2s ease-out;
    }
    
    .hero-cta:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 208, 132, 0.5);
    }
    
    /* CATEGORIES SECTION */
    .categories-section {
        padding: 120px 80px;
        background: #0a0a0a;
        position: relative;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 100px;
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 20px;
        background: linear-gradient(135deg, #00D084, #FFD60A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        animation: slideInUp 0.8s ease-out;
    }
    
    .section-subtitle {
        font-size: 18px;
        color: #aaaaaa;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
        animation: slideInUp 1s ease-out;
    }
    
    .categories-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .category-card {
        background: rgba(10, 10, 10, 0.8);
        border: 3px dashed;
        padding: 50px 40px;
        border-radius: 12px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .category-card:nth-child(1) {
        border-color: rgba(0, 180, 216, 0.5);
        animation-delay: 0.1s;
    }
    
    .category-card:nth-child(2) {
        border-color: rgba(255, 213, 10, 0.5);
        animation-delay: 0.2s;
    }
    
    .category-card:nth-child(3) {
        border-color: rgba(0, 208, 132, 0.5);
        animation-delay: 0.3s;
    }
    
    .category-card:nth-child(4) {
        border-color: rgba(255, 107, 74, 0.5);
        animation-delay: 0.4s;
    }
    
    .category-card:nth-child(5) {
        border-color: rgba(0, 180, 216, 0.5);
        animation-delay: 0.5s;
    }
    
    .category-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .category-card:hover::before {
        left: 100%;
    }
    
    .category-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 20px 50px rgba(0, 208, 132, 0.2);
    }
    
    .category-card:nth-child(1):hover {
        border-color: rgba(0, 180, 216, 1);
        box-shadow: 0 20px 50px rgba(0, 180, 216, 0.2);
    }
    
    .category-card:nth-child(2):hover {
        border-color: rgba(255, 213, 10, 1);
        box-shadow: 0 20px 50px rgba(255, 213, 10, 0.2);
    }
    
    .category-card:nth-child(3):hover {
        border-color: rgba(0, 208, 132, 1);
        box-shadow: 0 20px 50px rgba(0, 208, 132, 0.2);
    }
    
    .category-card:nth-child(4):hover {
        border-color: rgba(255, 107, 74, 1);
        box-shadow: 0 20px 50px rgba(255, 107, 74, 0.2);
    }
    
    .category-card:nth-child(5):hover {
        border-color: rgba(0, 180, 216, 1);
        box-shadow: 0 20px 50px rgba(0, 180, 216, 0.2);
    }
    
    .category-icon {
        font-size: 48px;
        margin-bottom: 20px;
        animation: float 3s ease-in-out infinite;
    }
    
    .category-title {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #ffffff;
        letter-spacing: 0.5px;
    }
    
    .category-desc {
        font-size: 15px;
        color: #aaaaaa;
        line-height: 1.8;
        font-weight: 300;
        margin-bottom: 20px;
    }
    
    .category-link {
        color: #00D084;
        text-decoration: none;
        font-weight: 600;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
    }
    
    .category-link:hover {
        color: #FFD60A;
    }
    
    /* STATS SECTION */
    .stats-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1a2e 0%, #0a0a0a 100%);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .stat-card {
        background: rgba(10, 10, 10, 0.8);
        border: 3px solid;
        border-radius: 12px;
        padding: 50px 40px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .stat-card:nth-child(1) {
        border-color: rgba(0, 180, 216, 0.5);
        animation-delay: 0.1s;
    }
    
    .stat-card:nth-child(2) {
        border-color: rgba(255, 213, 10, 0.5);
        animation-delay: 0.2s;
    }
    
    .stat-card:nth-child(3) {
        border-color: rgba(0, 208, 132, 0.5);
        animation-delay: 0.3s;
    }
    
    .stat-card:nth-child(4) {
        border-color: rgba(255, 107, 74, 0.5);
        animation-delay: 0.4s;
    }
    
    .stat-card:hover {
        transform: translateY(-15px);
    }
    
    .stat-card:nth-child(1):hover {
        border-color: rgba(0, 180, 216, 1);
        box-shadow: 0 20px 50px rgba(0, 180, 216, 0.2);
    }
    
    .stat-card:nth-child(2):hover {
        border-color: rgba(255, 213, 10, 1);
        box-shadow: 0 20px 50px rgba(255, 213, 10, 0.2);
    }
    
    .stat-card:nth-child(3):hover {
        border-color: rgba(0, 208, 132, 1);
        box-shadow: 0 20px 50px rgba(0, 208, 132, 0.2);
    }
    
    .stat-card:nth-child(4):hover {
        border-color: rgba(255, 107, 74, 1);
        box-shadow: 0 20px 50px rgba(255, 107, 74, 0.2);
    }
    
    .stat-number {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #00D084, #FFD60A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* CTA FINAL */
    .cta-final-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #00D084 0%, #00B4D8 25%, #FFD60A 50%, #FF6B4A 75%, #00D084 100%);
        background-size: 400% 400%;
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
        background: rgba(0, 0, 0, 0.2);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-final-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 20px;
        color: white;
        letter-spacing: -1px;
        animation: slideInUp 0.8s ease-out;
    }
    
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        color: rgba(255, 255, 255, 0.95);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;
        animation: slideInUp 1s ease-out;
    }
    
    .cta-final-button {
        background: #0a0a0a;
        color: #00D084;
        padding: 18px 60px;
        border: 3px solid #00D084;
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
        animation: slideInUp 1.2s ease-out;
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
        background: #00D084;
        color: #0a0a0a;
    }
    
    /* FOOTER */
    .footer {
        background: #0a0a0a;
        color: #888888;
        padding: 80px;
        text-align: center;
        border-top: 2px dashed rgba(0, 208, 132, 0.3);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 300;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(0, 208, 132, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
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
        
        .categories-section,
        .stats-section,
        .cta-final-section {
            padding: 80px 20px;
        }
        
        .section-title {
            font-size: 36px;
        }
        
        .cta-final-title {
            font-size: 36px;
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
navbar_html = '<div class="navbar"><div class="navbar-logo">PREMIUM</div><div class="navbar-links"><a href="#" class="navbar-link">Produtos</a><a href="#" class="navbar-link">Sobre</a><a href="#" class="navbar-link">Blog</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Acessar Conta</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">Gestão Completa de Benefícios</div>
        <div class="hero-subtitle">Tudo que você precisa em um único cartão</div>
        <button class="hero-cta">Começar Agora</button>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== CATEGORIES SECTION ====================
categories_html = '''<div class="categories-section">
    <div class="section-header">
        <div class="section-title">Nossas Categorias</div>
        <div class="section-subtitle">Soluções completas para todas as suas necessidades</div>
    </div>
    <div class="categories-grid">
        <div class="category-card">
            <div class="category-icon">🍽️</div>
            <div class="category-title">Alimentação</div>
            <div class="category-desc">Acesso a milhares de estabelecimentos parceiros com praticidade e segurança.</div>
            <a href="#" class="category-link">Saiba Mais →</a>
        </div>
        <div class="category-card">
            <div class="category-icon">🚗</div>
            <div class="category-title">Combustível</div>
            <div class="category-desc">Rede de postos de gasolina em todo o país para sua comodidade.</div>
            <a href="#" class="category-link">Saiba Mais →</a>
        </div>
        <div class="category-card">
            <div class="category-icon">💰</div>
            <div class="category-title">Refeição</div>
            <div class="category-desc">Flexibilidade para refeições em diversos locais e restaurantes.</div>
            <a href="#" class="category-link">Saiba Mais →</a>
        </div>
        <div class="category-card">
            <div class="category-icon">🎁</div>
            <div class="category-title">Multibenefícios</div>
            <div class="category-desc">Centralização de todos os seus benefícios em um único cartão.</div>
            <a href="#" class="category-link">Saiba Mais →</a>
        </div>
        <div class="category-card">
            <div class="category-icon">🚙</div>
            <div class="category-title">Frota</div>
            <div class="category-desc">Gestão eficiente de veículos corporativos com controle total.</div>
            <a href="#" class="category-link">Saiba Mais →</a>
        </div>
    </div>
</div>'''
st.markdown(categories_html, unsafe_allow_html=True)

# ==================== STATS SECTION ====================
stats_html = '''<div class="stats-section">
    <div class="section-header">
        <div class="section-title">Por Números</div>
        <div class="section-subtitle">Confiança e qualidade em cada transação</div>
    </div>
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">250K+</div>
            <div class="stat-label">Estabelecimentos</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">500K+</div>
            <div class="stat-label">Cartões Ativos</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">98%</div>
            <div class="stat-label">Satisfação</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Atendimento</div>
        </div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# ==================== CTA FINAL ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronto para Transformar?</div>
        <div class="cta-final-desc">Junte-se a centenas de milhares de usuários que já confiam em nós para gerenciar seus benefícios.</div>
        <button class="cta-final-button">Solicitar Cartão Agora</button>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">Telefone: +55 (11) 98765-4321 | Email: contato@premiumcard.com.br</div><div class="footer-text">Endereço: Av. Paulista, 1000 - São Paulo, SP</div><div class="footer-copyright">© 2025 Premium Card. Todos os direitos reservados. Gestão de benefícios de forma simples e segura.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
