import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="TechStore - Celulares Premium",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ULTRA PROFISSIONAL - INSPIRADO EM TELEPATI
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 50%, #0f0f0f 100%);
        background-attachment: fixed;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        color: #ffffff;
        line-height: 1.6;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* NAVBAR */
    .navbar {
        background: rgba(15, 15, 15, 0.95);
        backdrop-filter: blur(10px);
        padding: 16px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #00BFA5;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 10px rgba(0, 191, 165, 0.15);
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 900;
        color: #00BFA5;
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: #ffffff;
        text-decoration: none;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.3s ease;
    }
    
    .navbar-link:hover {
        color: #00BFA5;
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, #00BFA5, #00A89C);
        color: #000000;
        padding: 10px 28px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 700;
        font-size: 14px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 191, 165, 0.3);
    }
    
    .navbar-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 191, 165, 0.4);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(180deg, rgba(15, 15, 15, 0.9) 0%, rgba(0, 191, 165, 0.05) 100%);
        padding: 100px 60px;
        position: relative;
        overflow: hidden;
        border-bottom: 2px dashed #FF4444;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(0, 191, 165, 0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        align-items: center;
        position: relative;
        z-index: 2;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .hero-text h1 {
        font-size: 64px;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 20px;
        color: #ffffff;
        letter-spacing: -1px;
    }
    
    .hero-text h1 .highlight {
        color: #00BFA5;
    }
    
    .hero-text p {
        font-size: 18px;
        line-height: 1.7;
        margin-bottom: 40px;
        color: #cccccc;
        font-weight: 400;
    }
    
    .hero-image {
        text-align: center;
        font-size: 120px;
    }
    
    .hero-cta {
        display: inline-block;
        background: linear-gradient(135deg, #00BFA5, #00A89C);
        color: #000000;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 191, 165, 0.3);
    }
    
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 191, 165, 0.4);
    }
    
    /* FEATURES SECTION */
    .features-section {
        padding: 100px 60px;
        background: rgba(26, 26, 26, 0.8);
    }
    
    .feature-item {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        align-items: center;
        margin-bottom: 100px;
        padding: 60px;
        background: rgba(0, 191, 165, 0.05);
        border-radius: 12px;
        border: 2px dashed #FF4444;
    }
    
    .feature-item:nth-child(even) {
        direction: rtl;
    }
    
    .feature-item:nth-child(even) > * {
        direction: ltr;
    }
    
    .feature-number {
        font-size: 64px;
        font-weight: 900;
        color: #00BFA5;
        margin-bottom: 20px;
    }
    
    .feature-title {
        font-size: 40px;
        font-weight: 900;
        margin-bottom: 20px;
        color: #ffffff;
    }
    
    .feature-title .highlight {
        color: #00BFA5;
    }
    
    .feature-desc {
        font-size: 16px;
        color: #cccccc;
        line-height: 1.8;
        margin-bottom: 30px;
    }
    
    .feature-icon {
        font-size: 100px;
        text-align: center;
    }
    
    /* PRODUCTS SECTION */
    .products-section {
        padding: 100px 60px;
        background: linear-gradient(180deg, rgba(15, 15, 15, 0.9) 0%, rgba(0, 191, 165, 0.05) 100%);
    }
    
    .section-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 60px;
        color: #ffffff;
        text-align: center;
        letter-spacing: -0.5px;
    }
    
    .section-title .highlight {
        color: #00BFA5;
    }
    
    .products-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .product-card {
        background: rgba(26, 26, 26, 0.8);
        border: 2px solid #00BFA5;
        border-radius: 12px;
        padding: 40px;
        text-align: center;
        transition: all 0.4s ease;
        cursor: pointer;
    }
    
    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0, 191, 165, 0.25);
        border-color: #FF4444;
    }
    
    .product-icon {
        font-size: 80px;
        margin-bottom: 20px;
    }
    
    .product-title {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 12px;
        color: #ffffff;
    }
    
    .product-desc {
        font-size: 15px;
        color: #cccccc;
        line-height: 1.7;
        margin-bottom: 20px;
    }
    
    .product-price {
        font-size: 28px;
        font-weight: 900;
        color: #00BFA5;
    }
    
    /* STATS SECTION */
    .stats-section {
        padding: 100px 60px;
        background: rgba(0, 191, 165, 0.1);
        border-top: 2px dashed #FF4444;
        border-bottom: 2px dashed #FF4444;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 60px;
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
    }
    
    .stat-item {
        padding: 40px;
    }
    
    .stat-number {
        font-size: 56px;
        font-weight: 900;
        color: #00BFA5;
        margin-bottom: 12px;
    }
    
    .stat-label {
        font-size: 16px;
        color: #cccccc;
        font-weight: 600;
    }
    
    /* TESTIMONIALS SECTION */
    .testimonials-section {
        padding: 100px 60px;
        background: rgba(26, 26, 26, 0.8);
    }
    
    .testimonial-card {
        background: rgba(0, 191, 165, 0.1);
        border-left: 4px solid #00BFA5;
        padding: 40px;
        margin-bottom: 30px;
        border-radius: 8px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .testimonial-text {
        font-size: 16px;
        color: #ffffff;
        line-height: 1.8;
        margin-bottom: 20px;
        font-style: italic;
    }
    
    .testimonial-author {
        font-size: 14px;
        font-weight: 700;
        color: #00BFA5;
    }
    
    .testimonial-role {
        font-size: 13px;
        color: #cccccc;
        font-weight: 500;
    }
    
    /* CTA FINAL SECTION */
    .cta-final-section {
        background: linear-gradient(135deg, #00BFA5 0%, #00A89C 100%);
        color: #000000;
        padding: 100px 60px;
        text-align: center;
        border-top: 2px dashed #FF4444;
    }
    
    .cta-final-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
        letter-spacing: -0.5px;
    }
    
    .cta-final-desc {
        font-size: 18px;
        margin-bottom: 50px;
        opacity: 0.9;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .cta-final-button {
        background: #000000;
        color: #00BFA5;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    .cta-final-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    
    /* FOOTER */
    .footer {
        background: #000000;
        color: rgba(255, 255, 255, 0.7);
        padding: 60px;
        text-align: center;
        border-top: 2px solid #00BFA5;
    }
    
    .footer-text {
        font-size: 15px;
        margin-bottom: 10px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(0, 191, 165, 0.2);
        padding-top: 30px;
        margin-top: 30px;
        font-size: 13px;
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
        
        .hero-content {
            grid-template-columns: 1fr;
            gap: 40px;
        }
        
        .hero-text h1 {
            font-size: 36px;
        }
        
        .feature-item {
            grid-template-columns: 1fr;
            gap: 30px;
        }
        
        .feature-item:nth-child(even) {
            direction: ltr;
        }
        
        .products-section,
        .features-section,
        .stats-section,
        .testimonials-section,
        .cta-final-section {
            padding: 60px 20px;
        }
        
        .section-title {
            font-size: 32px;
        }
        
        .cta-final-title {
            font-size: 32px;
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
navbar_html = '<div class="navbar"><a href="#" class="navbar-logo">📱 TechStore</a><div class="navbar-links"><a href="#" class="navbar-link">Produtos</a><a href="#" class="navbar-link">Sobre</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Comprar Agora</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-text">
            <h1>Celulares <span class="highlight">Premium</span></h1>
            <p>Descubra a melhor seleção de celulares de alta performance com os melhores preços do mercado. Tecnologia de ponta ao seu alcance.</p>
            <button class="hero-cta">Explorar Catálogo</button>
        </div>
        <div class="hero-image">📱</div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
features_html = '''<div class="features-section">
    <div class="feature-item">
        <div>
            <div class="feature-number">#1</div>
            <div class="feature-title">Tecnologia de <span class="highlight">Ponta</span></div>
            <div class="feature-desc">Processadores de última geração, câmeras revolucionárias e baterias que duram o dia todo. Todos os nossos celulares possuem especificações premium para garantir a melhor experiência.</div>
        </div>
        <div class="feature-icon">⚡</div>
    </div>
    
    <div class="feature-item">
        <div class="feature-icon">💎</div>
        <div>
            <div class="feature-number">#2</div>
            <div class="feature-title">Design <span class="highlight">Exclusivo</span></div>
            <div class="feature-desc">Celulares com design premium e acabamento impecável. Cada detalhe foi pensado para oferecer conforto, elegância e durabilidade. Materiais de alta qualidade em todos os modelos.</div>
        </div>
    </div>
    
    <div class="feature-item">
        <div>
            <div class="feature-number">#3</div>
            <div class="feature-title">Garantia e <span class="highlight">Suporte</span></div>
            <div class="feature-desc">Garantia de 2 anos em todos os produtos. Atendimento técnico 24/7 para resolver qualquer dúvida. Trocas e devoluções sem complicações. Sua satisfação é nossa prioridade.</div>
        </div>
        <div class="feature-icon">🛡️</div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ==================== PRODUCTS SECTION ====================
products_html = '''<div class="products-section">
    <div class="section-title">Nossos <span class="highlight">Produtos</span></div>
    <div class="products-grid">
        <div class="product-card">
            <div class="product-icon">📱</div>
            <div class="product-title">iPhone 15 Pro</div>
            <div class="product-desc">Câmera profissional, processador A17 Pro, design em titânio. O melhor do mercado.</div>
            <div class="product-price">R$ 7.999</div>
        </div>
        <div class="product-card">
            <div class="product-icon">🔥</div>
            <div class="product-title">Samsung Galaxy S24</div>
            <div class="product-desc">Tela AMOLED 120Hz, câmera 200MP, bateria de longa duração. Potência pura.</div>
            <div class="product-price">R$ 6.499</div>
        </div>
        <div class="product-card">
            <div class="product-icon">⚡</div>
            <div class="product-title">Google Pixel 8</div>
            <div class="product-desc">IA integrada, câmera computacional, software puro. Inteligência artificial no seu bolso.</div>
            <div class="product-price">R$ 5.299</div>
        </div>
        <div class="product-card">
            <div class="product-icon">💫</div>
            <div class="product-title">OnePlus 12</div>
            <div class="product-desc">Carregamento ultra-rápido, design elegante, performance excepcional. Velocidade extrema.</div>
            <div class="product-price">R$ 4.799</div>
        </div>
        <div class="product-card">
            <div class="product-icon">🎮</div>
            <div class="product-title">POCO F6 Pro</div>
            <div class="product-desc">Processador flagship, tela 144Hz, preço competitivo. Melhor custo-benefício.</div>
            <div class="product-price">R$ 3.299</div>
        </div>
        <div class="product-card">
            <div class="product-icon">🌟</div>
            <div class="product-title">Xiaomi 14</div>
            <div class="product-desc">Câmera Leica, design premium, preço acessível. O melhor da Xiaomi.</div>
            <div class="product-price">R$ 3.899</div>
        </div>
    </div>
</div>'''
st.markdown(products_html, unsafe_allow_html=True)

# ==================== STATS SECTION ====================
stats_html = '''<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-number">50K+</div>
            <div class="stat-label">Clientes Satisfeitos</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">200+</div>
            <div class="stat-label">Modelos Disponíveis</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">98%</div>
            <div class="stat-label">Taxa de Satisfação</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Atendimento</div>
        </div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# ==================== TESTIMONIALS SECTION ====================
testimonials_html = '''<div class="testimonials-section">
    <div class="section-title">O que nossos <span class="highlight">clientes dizem</span></div>
    <div class="testimonial-card">
        <div class="testimonial-text">"Melhor loja de celulares que já comprei! Atendimento impecável, produtos de qualidade garantida e preços muito competitivos. Recomendo para todos!"</div>
        <div class="testimonial-author">Ana Silva</div>
        <div class="testimonial-role">Cliente desde 2022</div>
    </div>
    <div class="testimonial-card">
        <div class="testimonial-text">"Comprei meu iPhone aqui e foi uma experiência fantástica. Entrega rápida, produto original e ainda ganhei acessórios grátis. Voltarei com certeza!"</div>
        <div class="testimonial-author">Carlos Mendes</div>
        <div class="testimonial-role">Cliente Premium</div>
    </div>
    <div class="testimonial-card">
        <div class="testimonial-text">"A TechStore é confiável, rápida e oferece os melhores preços. Já comprei 3 celulares aqui para minha família. Muito satisfeito com tudo!"</div>
        <div class="testimonial-author">Marina Costa</div>
        <div class="testimonial-role">Cliente Fiel</div>
    </div>
</div>'''
st.markdown(testimonials_html, unsafe_allow_html=True)

# ==================== CTA FINAL SECTION ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-title">Pronto para seu novo celular?</div>
    <div class="cta-final-desc">Explore nosso catálogo completo e encontre o celular perfeito para você. Frete grátis em compras acima de R$ 2.000!</div>
    <button class="cta-final-button">Começar Agora</button>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">📞 (11) 98765-4321 | 📧 contato@techstore.com.br</div><div class="footer-text">📍 São Paulo, SP - Brasil</div><div class="footer-copyright">© 2025 TechStore. Todos os direitos reservados. Sua loja de celulares premium de confiança.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
