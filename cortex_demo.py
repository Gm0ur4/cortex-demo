import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Luxury Resort - Experiência Premium",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS SOFISTICADO COM ANIMAÇÕES ABSURDAS
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');
    
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
    
    /* ANIMAÇÕES SOFISTICADAS */
    @keyframes slideInLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeInUp {
        from { transform: translateY(50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes scaleIn {
        from { transform: scale(0.9); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    @keyframes shimmer {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    
    @keyframes borderGlow {
        0%, 100% { border-color: rgba(218, 165, 32, 0.3); box-shadow: 0 0 10px rgba(218, 165, 32, 0.1); }
        50% { border-color: rgba(218, 165, 32, 0.8); box-shadow: 0 0 20px rgba(218, 165, 32, 0.3); }
    }
    
    @keyframes slideUp {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    /* NAVBAR */
    .navbar {
        background: rgba(10, 10, 10, 0.98);
        backdrop-filter: blur(15px);
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid rgba(218, 165, 32, 0.3);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    .navbar-logo {
        font-size: 32px;
        font-weight: 700;
        color: #DAA520;
        letter-spacing: 3px;
        font-family: 'Cormorant Garamond', serif;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .navbar-links {
        display: flex;
        gap: 60px;
        align-items: center;
    }
    
    .navbar-link {
        color: #ffffff;
        text-decoration: none;
        font-weight: 500;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        position: relative;
        animation: slideInRight 0.8s ease-out;
    }
    
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: #DAA520;
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #DAA520;
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, #DAA520, #B8860B);
        color: #000000;
        padding: 12px 40px;
        border-radius: 3px;
        text-decoration: none;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: 2px solid #DAA520;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(218, 165, 32, 0.3);
        animation: slideInRight 1s ease-out;
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(218, 165, 32, 0.5);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        background-size: cover;
        background-position: center;
        min-height: 750px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(218, 165, 32, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        top: -100px;
        right: -100px;
    }
    
    .hero-content {
        text-align: center;
        z-index: 2;
        position: relative;
        max-width: 900px;
        animation: fadeInUp 1s ease-out;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #DAA520;
        letter-spacing: 2px;
        font-family: 'Cormorant Garamond', serif;
        animation: slideInLeft 1s ease-out;
    }
    
    .hero-subtitle {
        font-size: 22px;
        font-weight: 300;
        margin-bottom: 50px;
        color: #ffffff;
        letter-spacing: 2px;
        animation: slideInRight 1.2s ease-out;
    }
    
    .hero-cta {
        background: linear-gradient(135deg, #DAA520, #B8860B);
        color: #000000;
        padding: 16px 50px;
        border-radius: 3px;
        font-weight: 700;
        font-size: 13px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid #DAA520;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(218, 165, 32, 0.3);
        animation: fadeInUp 1.4s ease-out;
    }
    
    .hero-cta:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(218, 165, 32, 0.5);
    }
    
    /* ABOUT SECTION */
    .about-section {
        padding: 120px 80px;
        background: #0a0a0a;
        position: relative;
    }
    
    .about-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .about-text h2 {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #DAA520;
        letter-spacing: 1px;
        font-family: 'Cormorant Garamond', serif;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .about-text p {
        font-size: 16px;
        color: #cccccc;
        line-height: 1.9;
        margin-bottom: 20px;
        font-weight: 300;
        animation: fadeInUp 1s ease-out;
    }
    
    .about-image {
        background: linear-gradient(135deg, #DAA520 0%, #B8860B 100%);
        height: 450px;
        border-radius: 3px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 120px;
        color: rgba(0, 0, 0, 0.1);
        animation: scaleIn 1s ease-out;
        border: 2px solid rgba(218, 165, 32, 0.3);
        animation: borderGlow 3s ease-in-out infinite;
    }
    
    /* SERVICES SECTION */
    .services-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 100px;
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #DAA520;
        letter-spacing: 1px;
        font-family: 'Cormorant Garamond', serif;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .section-description {
        font-size: 18px;
        color: #aaaaaa;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
        animation: fadeInUp 1s ease-out;
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .service-card {
        background: rgba(218, 165, 32, 0.05);
        border: 2px solid rgba(218, 165, 32, 0.3);
        padding: 50px 40px;
        border-radius: 3px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .service-card:nth-child(1) { animation-delay: 0.1s; }
    .service-card:nth-child(2) { animation-delay: 0.2s; }
    .service-card:nth-child(3) { animation-delay: 0.3s; }
    .service-card:nth-child(4) { animation-delay: 0.4s; }
    .service-card:nth-child(5) { animation-delay: 0.5s; }
    .service-card:nth-child(6) { animation-delay: 0.6s; }
    
    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(218, 165, 32, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .service-card:hover::before {
        left: 100%;
    }
    
    .service-card:hover {
        transform: translateY(-15px);
        border-color: #DAA520;
        box-shadow: 0 20px 50px rgba(218, 165, 32, 0.2);
    }
    
    .service-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #DAA520;
        letter-spacing: 1px;
        font-family: 'Cormorant Garamond', serif;
    }
    
    .service-desc {
        font-size: 15px;
        color: #aaaaaa;
        line-height: 1.8;
        font-weight: 300;
    }
    
    /* ROOMS SECTION */
    .rooms-section {
        padding: 120px 80px;
        background: #0a0a0a;
    }
    
    .rooms-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .room-card {
        background: rgba(218, 165, 32, 0.05);
        border: 2px solid rgba(218, 165, 32, 0.3);
        border-radius: 3px;
        overflow: hidden;
        transition: all 0.4s ease;
        animation: slideUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .room-card:nth-child(1) { animation-delay: 0.1s; }
    .room-card:nth-child(2) { animation-delay: 0.2s; }
    .room-card:nth-child(3) { animation-delay: 0.3s; }
    
    .room-card:hover {
        transform: translateY(-15px);
        border-color: #DAA520;
        box-shadow: 0 20px 50px rgba(218, 165, 32, 0.2);
    }
    
    .room-image {
        background: linear-gradient(135deg, #DAA520 0%, #B8860B 100%);
        height: 280px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 100px;
        color: rgba(0, 0, 0, 0.1);
    }
    
    .room-content {
        padding: 40px;
    }
    
    .room-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #DAA520;
        font-family: 'Cormorant Garamond', serif;
    }
    
    .room-desc {
        font-size: 15px;
        color: #aaaaaa;
        line-height: 1.8;
        margin-bottom: 20px;
        font-weight: 300;
    }
    
    .room-price {
        font-size: 28px;
        font-weight: 700;
        color: #DAA520;
        margin-bottom: 20px;
    }
    
    .room-cta {
        background: linear-gradient(135deg, #DAA520, #B8860B);
        color: #000000;
        padding: 12px 32px;
        border: none;
        border-radius: 3px;
        font-weight: 700;
        font-size: 12px;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .room-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(218, 165, 32, 0.3);
    }
    
    /* CTA FINAL SECTION */
    .cta-final-section {
        background: linear-gradient(135deg, #DAA520 0%, #B8860B 50%, #DAA520 100%);
        color: #000000;
        padding: 120px 80px;
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
        font-weight: 700;
        margin-bottom: 20px;
        letter-spacing: 1px;
        font-family: 'Cormorant Garamond', serif;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;
        animation: fadeInUp 1s ease-out;
    }
    
    .cta-final-button {
        background: #000000;
        color: #DAA520;
        padding: 16px 60px;
        border: 3px solid #DAA520;
        border-radius: 3px;
        font-weight: 700;
        font-size: 13px;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        animation: fadeInUp 1.2s ease-out;
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        background: #DAA520;
        color: #000000;
    }
    
    /* FOOTER */
    .footer {
        background: #0a0a0a;
        color: #888888;
        padding: 80px;
        text-align: center;
        border-top: 2px solid rgba(218, 165, 32, 0.3);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 300;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(218, 165, 32, 0.2);
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
        }
        
        .hero-title {
            font-size: 42px;
        }
        
        .about-grid {
            grid-template-columns: 1fr;
            gap: 40px;
        }
        
        .about-section,
        .services-section,
        .rooms-section,
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
navbar_html = '<div class="navbar"><div class="navbar-logo">LUXE</div><div class="navbar-links"><a href="#" class="navbar-link">Acomodações</a><a href="#" class="navbar-link">Serviços</a><a href="#" class="navbar-link">Experiências</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Reservar</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">Luxo Incomparável</div>
        <div class="hero-subtitle">Experiência de hospedagem que transcende</div>
        <button class="hero-cta">Explorar Agora</button>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== ABOUT SECTION ====================
about_html = '''<div class="about-section">
    <div class="about-grid">
        <div class="about-text">
            <h2>Bem-vindo ao Nosso Refúgio</h2>
            <p>Descubra um mundo de elegância e sofisticação onde cada detalhe foi cuidadosamente pensado para sua comodidade absoluta. Nossas acomodações premium oferecem o melhor em conforto e estilo.</p>
            <p>Mergulhe em uma experiência única onde o luxo encontra a hospitalidade. Cada momento em nosso resort é uma oportunidade de criar memórias inesquecíveis.</p>
        </div>
        <div class="about-image"></div>
    </div>
</div>'''
st.markdown(about_html, unsafe_allow_html=True)

# ==================== SERVICES SECTION ====================
services_html = '''<div class="services-section">
    <div class="section-header">
        <div class="section-title">Serviços Exclusivos</div>
        <div class="section-description">Tudo que você precisa para uma estadia perfeita</div>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-title">Gastronomia Refinada</div>
            <div class="service-desc">Restaurantes gourmet com chefs renomados e culinária internacional de alta qualidade.</div>
        </div>
        <div class="service-card">
            <div class="service-title">Spa de Luxo</div>
            <div class="service-desc">Tratamentos de bem-estar com produtos premium e terapeutas especializados.</div>
        </div>
        <div class="service-card">
            <div class="service-title">Piscinas Aquecidas</div>
            <div class="service-desc">Piscinas de água salgada aquecida com vista panorâmica e serviço de bar.</div>
        </div>
        <div class="service-card">
            <div class="service-title">Entretenimento</div>
            <div class="service-desc">Shows ao vivo, eventos especiais e atividades de lazer para toda a família.</div>
        </div>
        <div class="service-card">
            <div class="service-title">Transporte VIP</div>
            <div class="service-desc">Serviço de transfer com veículos de luxo e motorista particular.</div>
        </div>
        <div class="service-card">
            <div class="service-title">Concierge 24/7</div>
            <div class="service-desc">Atendimento personalizado para todas as suas necessidades e desejos.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# ==================== ROOMS SECTION ====================
rooms_html = '''<div class="rooms-section">
    <div class="section-header">
        <div class="section-title">Acomodações Premium</div>
        <div class="section-description">Escolha entre nossas suítes e villas exclusivas</div>
    </div>
    <div class="rooms-grid">
        <div class="room-card">
            <div class="room-image"></div>
            <div class="room-content">
                <div class="room-title">Suíte Deluxe</div>
                <div class="room-desc">Conforto supremo com vista para o jardim. Inclui banheiro de mármol, cama king-size e varanda privada.</div>
                <div class="room-price">R$ 1.200/noite</div>
                <button class="room-cta">Reservar</button>
            </div>
        </div>
        <div class="room-card">
            <div class="room-image"></div>
            <div class="room-content">
                <div class="room-title">Suíte Premium</div>
                <div class="room-desc">Luxo incomparável com vista para o mar. Jacuzzi privado, serviço de butler e acesso VIP.</div>
                <div class="room-price">R$ 1.800/noite</div>
                <button class="room-cta">Reservar</button>
            </div>
        </div>
        <div class="room-card">
            <div class="room-image"></div>
            <div class="room-content">
                <div class="room-title">Villa Privativa</div>
                <div class="room-desc">Isolamento total e privacidade absoluta. Piscina privada, spa pessoal e chef particular.</div>
                <div class="room-price">R$ 3.500/noite</div>
                <button class="room-cta">Reservar</button>
            </div>
        </div>
    </div>
</div>'''
st.markdown(rooms_html, unsafe_allow_html=True)

# ==================== CTA FINAL SECTION ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-content">
        <div class="cta-final-title">Reserve Sua Experiência</div>
        <div class="cta-final-desc">Viva momentos inesquecíveis em nosso resort de luxo. Acomodações exclusivas, serviços impecáveis e memórias para a vida toda.</div>
        <button class="cta-final-button">Fazer Reserva Agora</button>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">Telefone: +55 (11) 98765-4321 | Email: reservas@luxeresort.com.br</div><div class="footer-text">Endereço: Av. Costeira, 5000 - Praia Paradisíaca, SP</div><div class="footer-copyright">© 2025 Luxe Resort. Todos os direitos reservados. Experiência de luxo absoluto.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
