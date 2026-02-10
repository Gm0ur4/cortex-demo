import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Barbie Pink - Vibe Criativa",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS BARBIE PINK - CRIATIVIDADE MÁXIMA
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 25%, #ff85c1 50%, #ffb6d9 75%, #ffc0cb 100%);
        background-size: 400% 400%;
        font-family: 'Fredoka', sans-serif;
        color: #ffffff;
        line-height: 1.8;
        overflow-x: hidden;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ANIMAÇÕES CRIATIVAS */
    @keyframes rainbowPulse {
        0% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
        50% { box-shadow: 0 0 50px rgba(255, 255, 255, 0.8); }
        100% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
    }
    
    @keyframes floatBounce {
        0%, 100% { transform: translateY(0px) rotateZ(-5deg); }
        50% { transform: translateY(-30px) rotateZ(5deg); }
    }
    
    @keyframes spinGlow {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.1); }
        100% { transform: rotate(360deg) scale(1); }
    }
    
    @keyframes slideInPink {
        0% { transform: translateX(-100px) rotateY(45deg); opacity: 0; }
        100% { transform: translateX(0) rotateY(0deg); opacity: 1; }
    }
    
    @keyframes popIn {
        0% { transform: scale(0.5); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes wiggle {
        0%, 100% { transform: rotateZ(-2deg); }
        50% { transform: rotateZ(2deg); }
    }
    
    @keyframes heartBeat {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.1); }
        50% { transform: scale(1); }
    }
    
    @keyframes neonFlicker {
        0%, 100% { text-shadow: 0 0 10px #ff1493, 0 0 20px #ff1493; }
        50% { text-shadow: 0 0 20px #ff1493, 0 0 40px #ff1493, 0 0 60px #ff1493; }
    }
    
    /* NAVBAR BARBIE */
    .navbar {
        background: linear-gradient(135deg, rgba(255, 20, 147, 0.95) 0%, rgba(255, 105, 180, 0.95) 100%);
        backdrop-filter: blur(20px);
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px dashed rgba(255, 255, 255, 0.5);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 8px 32px rgba(255, 20, 147, 0.4);
    }
    
    .navbar-logo {
        font-size: 36px;
        font-weight: 900;
        color: white;
        letter-spacing: 3px;
        font-family: 'Poppins', sans-serif;
        animation: neonFlicker 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        font-family: 'Fredoka', sans-serif;
    }
    
    .navbar-link::before {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 3px;
        background: white;
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::before {
        width: 100%;
    }
    
    .navbar-link:hover {
        transform: scale(1.1);
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, white, #ffe0ec);
        color: #ff1493;
        padding: 12px 32px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: 2px solid white;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.3);
        font-family: 'Fredoka', sans-serif;
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 255, 255, 0.5);
    }
    
    /* HERO SECTION BARBIE */
    .hero-section {
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 25%, #ff85c1 50%, #ffb6d9 75%, #ffc0cb 100%);
        background-size: 400% 400%;
        min-height: 800px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 80px 60px;
        animation: gradientShift 8s ease infinite;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
        animation: floatBounce 6s ease-in-out infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -150px;
        left: -150px;
        animation: floatBounce 8s ease-in-out infinite reverse;
    }
    
    .hero-content {
        text-align: center;
        z-index: 2;
        position: relative;
        max-width: 900px;
    }
    
    .hero-title {
        font-size: 80px;
        font-weight: 900;
        margin-bottom: 20px;
        color: white;
        letter-spacing: -2px;
        line-height: 1.1;
        font-family: 'Poppins', sans-serif;
        animation: neonFlicker 2s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.8);
    }
    
    .hero-subtitle {
        font-size: 24px;
        font-weight: 400;
        margin-bottom: 50px;
        color: white;
        letter-spacing: 2px;
        animation: slideInPink 1s ease-out;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.6);
    }
    
    .hero-cta-group {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .hero-cta-primary {
        background: linear-gradient(135deg, white, #ffe0ec);
        color: #ff1493;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid white;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 30px rgba(255, 255, 255, 0.4);
        font-family: 'Fredoka', sans-serif;
        animation: popIn 0.8s ease-out;
    }
    
    .hero-cta-primary:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 12px 40px rgba(255, 255, 255, 0.6);
    }
    
    .hero-cta-secondary {
        background: transparent;
        color: white;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid white;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
        font-family: 'Fredoka', sans-serif;
        animation: popIn 1s ease-out;
    }
    
    .hero-cta-secondary:hover {
        background: white;
        color: #ff1493;
        box-shadow: 0 8px 30px rgba(255, 255, 255, 0.5);
    }
    
    /* FEATURES SECTION */
    .features-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #ff69b4 0%, #ff85c1 50%, #ffb6d9 100%);
        position: relative;
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        color: white;
        letter-spacing: -1px;
        font-family: 'Poppins', sans-serif;
        animation: neonFlicker 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 224, 236, 0.95));
        border: 3px dashed rgba(255, 20, 147, 0.4);
        padding: 50px 40px;
        border-radius: 30px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInPink 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 8px 32px rgba(255, 20, 147, 0.2);
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
        background: linear-gradient(90deg, transparent, rgba(255, 20, 147, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-20px) rotateX(5deg) scale(1.05);
        border-color: #ff1493;
        box-shadow: 0 20px 50px rgba(255, 20, 147, 0.3);
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 20px;
        animation: spinGlow 4s ease-in-out infinite;
    }
    
    .feature-title {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #ff1493;
        letter-spacing: 0.5px;
        font-family: 'Poppins', sans-serif;
    }
    
    .feature-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.8;
        font-weight: 400;
    }
    
    /* PRICING TABLE */
    .pricing-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #ff85c1 0%, #ffb6d9 50%, #ffc0cb 100%);
    }
    
    .pricing-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        color: white;
        letter-spacing: -1px;
        font-family: 'Poppins', sans-serif;
        animation: neonFlicker 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
    }
    
    .pricing-table-wrapper {
        max-width: 1200px;
        margin: 0 auto;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(255, 224, 236, 0.98));
        border: 3px dashed rgba(255, 20, 147, 0.4);
        border-radius: 30px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(255, 20, 147, 0.25);
        animation: popIn 0.8s ease-out;
    }
    
    .pricing-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .pricing-table thead {
        background: linear-gradient(135deg, #ff1493, #ff69b4);
        color: white;
    }
    
    .pricing-table th {
        padding: 25px;
        text-align: left;
        font-weight: 700;
        font-size: 16px;
        letter-spacing: 1px;
        font-family: 'Poppins', sans-serif;
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .pricing-table th:last-child {
        border-right: none;
    }
    
    .pricing-table td {
        padding: 20px 25px;
        border-bottom: 1px solid rgba(255, 20, 147, 0.15);
        font-size: 14px;
        color: #2d2d2d;
    }
    
    .pricing-table tbody tr:hover {
        background: rgba(255, 20, 147, 0.08);
    }
    
    .pricing-table tbody tr:last-child td {
        border-bottom: none;
    }
    
    .price-value {
        font-size: 28px;
        font-weight: 700;
        color: #ff1493;
        font-family: 'Poppins', sans-serif;
    }
    
    .feature-check {
        color: #ff1493;
        font-weight: 700;
        font-size: 18px;
    }
    
    .feature-cross {
        color: #999999;
        font-weight: 700;
        font-size: 18px;
    }
    
    /* COMPARISON SECTION */
    .comparison-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #ff69b4 0%, #ff85c1 50%, #ffb6d9 100%);
    }
    
    .comparison-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        color: white;
        letter-spacing: -1px;
        font-family: 'Poppins', sans-serif;
        animation: neonFlicker 2s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
    }
    
    .comparison-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .comparison-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 224, 236, 0.95));
        border: 3px dashed rgba(255, 20, 147, 0.4);
        border-radius: 30px;
        padding: 50px 40px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInPink 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 8px 32px rgba(255, 20, 147, 0.2);
    }
    
    .comparison-card:nth-child(1) { animation-delay: 0.1s; }
    .comparison-card:nth-child(2) { animation-delay: 0.2s; }
    .comparison-card:nth-child(3) { animation-delay: 0.3s; }
    
    .comparison-card:hover {
        transform: translateY(-15px) scale(1.05);
        border-color: #ff1493;
        box-shadow: 0 20px 50px rgba(255, 20, 147, 0.3);
    }
    
    .comparison-number {
        font-size: 48px;
        font-weight: 900;
        color: #ff1493;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }
    
    .comparison-label {
        font-size: 18px;
        font-weight: 700;
        color: #2d2d2d;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-family: 'Fredoka', sans-serif;
    }
    
    /* CTA FINAL */
    .cta-final-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 25%, #ff85c1 50%, #ffb6d9 75%, #ffc0cb 100%);
        background-size: 400% 400%;
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: gradientShift 8s ease infinite;
    }
    
    .cta-final-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.1);
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
        font-family: 'Poppins', sans-serif;
        animation: neonFlicker 2s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.8);
    }
    
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        color: white;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 400;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.6);
    }
    
    .cta-final-button {
        background: white;
        color: #ff1493;
        padding: 18px 60px;
        border: 3px dashed #ff1493;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 25px rgba(255, 255, 255, 0.3);
        font-family: 'Fredoka', sans-serif;
        animation: popIn 1.2s ease-out;
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 12px 35px rgba(255, 255, 255, 0.5);
    }
    
    /* FOOTER */
    .footer {
        background: rgba(255, 20, 147, 0.95);
        color: white;
        padding: 80px;
        text-align: center;
        border-top: 3px dashed rgba(255, 255, 255, 0.5);
        box-shadow: 0 -8px 32px rgba(255, 20, 147, 0.3);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 400;
        font-family: 'Fredoka', sans-serif;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Fredoka', sans-serif;
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
        
        .features-section,
        .pricing-section,
        .comparison-section,
        .cta-final-section {
            padding: 80px 20px;
        }
        
        .section-title,
        .pricing-title,
        .comparison-title,
        .cta-final-title {
            font-size: 36px;
        }
        
        .pricing-table {
            font-size: 12px;
        }
        
        .pricing-table th,
        .pricing-table td {
            padding: 15px;
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
navbar_html = '<div class="navbar"><div class="navbar-logo">BARBIE PINK</div><div class="navbar-links"><a href="#" class="navbar-link">Coleção</a><a href="#" class="navbar-link">Vibes</a><a href="#" class="navbar-link">Preços</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Entrar</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">VIBE BARBIE</div>
        <div class="hero-subtitle">Criatividade, Cor e Diversão em Cada Clique</div>
        <div class="hero-cta-group">
            <button class="hero-cta-primary">Explorar Agora</button>
            <button class="hero-cta-secondary">Saiba Mais</button>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
features_html = '''<div class="features-section">
    <div class="section-title">Por Que Amar</div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🎀</div>
            <div class="feature-title">Estilo Único</div>
            <div class="feature-desc">Expressa sua personalidade com cores vibrantes e design criativo.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💖</div>
            <div class="feature-title">Diversão Total</div>
            <div class="feature-desc">Cada interação é uma experiência alegre e envolvente.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <div class="feature-title">Criatividade</div>
            <div class="feature-desc">Ferramentas poderosas para soltar sua imaginação.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌸</div>
            <div class="feature-title">Comunidade</div>
            <div class="feature-desc">Conecte-se com pessoas que compartilham sua vibe.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <div class="feature-title">Customização</div>
            <div class="feature-desc">Personalize tudo do seu jeito, sem limites.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Velocidade</div>
            <div class="feature-desc">Rápido, responsivo e sempre pronto para você.</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ==================== PRICING TABLE ====================
pricing_html = '''<div class="pricing-section">
    <div class="pricing-title">Planos Incríveis</div>
    <div class="pricing-table-wrapper">
        <table class="pricing-table">
            <thead>
                <tr>
                    <th>Recurso</th>
                    <th>Rosa</th>
                    <th>Magenta</th>
                    <th>Fúcsia</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Preço Mensal</strong></td>
                    <td><span class="price-value">R$ 49</span></td>
                    <td><span class="price-value">R$ 99</span></td>
                    <td><span class="price-value">R$ 199</span></td>
                </tr>
                <tr>
                    <td>Acesso Básico</td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Cores Exclusivas</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Suporte Prioritário</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Conteúdo Ilimitado</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Comunidade VIP</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>'''
st.markdown(pricing_html, unsafe_allow_html=True)

# ==================== COMPARISON SECTION ====================
comparison_html = '''<div class="comparison-section">
    <div class="comparison-title">Números Que Brilham</div>
    <div class="comparison-grid">
        <div class="comparison-card">
            <div class="comparison-number">100K+</div>
            <div class="comparison-label">Usuárias Felizes</div>
        </div>
        <div class="comparison-card">
            <div class="comparison-number">500+</div>
            <div class="comparison-label">Cores Disponíveis</div>
        </div>
        <div class="comparison-card">
            <div class="comparison-number">99.9%</div>
            <div class="comparison-label">Diversão Garantida</div>
        </div>
    </div>
</div>'''
st.markdown(comparison_html, unsafe_allow_html=True)

# ==================== CTA FINAL ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronta para Brilhar?</div>
        <div class="cta-final-desc">Junte-se à revolução rosa e descubra um mundo de cores, criatividade e diversão!</div>
        <button class="cta-final-button">Começar a Jornada</button>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">Email: hello@barbiepink.com | Telefone: +55 (11) 98765-4321</div><div class="footer-text">Endereço: Av. Criatividade, 1000 - São Paulo, SP</div><div class="footer-copyright">© 2025 Barbie Pink. Todos os direitos reservados. Vibe Rosa é Vibe Boa!</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
