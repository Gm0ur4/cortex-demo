import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Luxe Resort - Experiência de Luxo Absoluto",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ULTRA LUXUOSO - HOTEL DE LUXO
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Lato:wght@300;400;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #f5f3f0;
        font-family: 'Lato', sans-serif;
        color: #2c2c2c;
        line-height: 1.8;
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
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        padding: 20px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(184, 134, 11, 0.2);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    .navbar-logo {
        font-size: 28px;
        font-weight: 900;
        color: #1a1a1a;
        text-decoration: none;
        letter-spacing: 2px;
        font-family: 'Playfair Display', serif;
    }
    
    .navbar-logo-highlight {
        color: #B8860B;
    }
    
    .navbar-links {
        display: flex;
        gap: 60px;
        align-items: center;
    }
    
    .navbar-link {
        color: #2c2c2c;
        text-decoration: none;
        font-weight: 400;
        font-size: 13px;
        transition: all 0.3s ease;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .navbar-link:hover {
        color: #B8860B;
    }
    
    .navbar-cta {
        background: #B8860B;
        color: white;
        padding: 12px 40px;
        border-radius: 2px;
        text-decoration: none;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.25);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .navbar-cta:hover {
        background: #9a7009;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(184, 134, 11, 0.35);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect fill="%23d4a574" width="1200" height="600"/></svg>');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        height: 700px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-content {
        text-align: center;
        color: white;
        z-index: 2;
        position: relative;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        margin-bottom: 20px;
        letter-spacing: 2px;
        font-family: 'Playfair Display', serif;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 20px;
        font-weight: 300;
        margin-bottom: 50px;
        letter-spacing: 1px;
        opacity: 0.95;
    }
    
    .hero-cta {
        display: inline-block;
        background: #B8860B;
        color: white;
        padding: 16px 50px;
        border-radius: 2px;
        font-weight: 700;
        font-size: 13px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .hero-cta:hover {
        background: #9a7009;
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(184, 134, 11, 0.4);
    }
    
    /* BOOKING SECTION */
    .booking-section {
        background: white;
        padding: 60px 80px;
        margin-top: -80px;
        position: relative;
        z-index: 10;
    }
    
    .booking-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 2px;
        padding: 40px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        max-width: 1000px;
        margin: 0 auto;
    }
    
    .booking-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 30px;
        color: #1a1a1a;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .booking-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
    }
    
    .booking-input {
        padding: 12px 16px;
        border: 1px solid #d0d0d0;
        border-radius: 2px;
        font-size: 14px;
        font-family: 'Lato', sans-serif;
    }
    
    .booking-input:focus {
        outline: none;
        border-color: #B8860B;
        box-shadow: 0 0 0 2px rgba(184, 134, 11, 0.1);
    }
    
    .booking-button {
        background: #B8860B;
        color: white;
        padding: 12px 40px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 13px;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.25);
    }
    
    .booking-button:hover {
        background: #9a7009;
        transform: translateY(-2px);
    }
    
    /* ABOUT SECTION */
    .about-section {
        padding: 100px 80px;
        background: white;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 80px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .section-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
        color: #1a1a1a;
        letter-spacing: 1px;
        font-family: 'Playfair Display', serif;
    }
    
    .section-title-highlight {
        color: #B8860B;
    }
    
    .section-description {
        font-size: 16px;
        color: #666666;
        line-height: 1.8;
        font-weight: 300;
    }
    
    .about-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .about-text h3 {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 20px;
        color: #1a1a1a;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .about-text p {
        font-size: 15px;
        color: #555555;
        line-height: 1.9;
        margin-bottom: 20px;
        font-weight: 300;
    }
    
    .about-image {
        background: linear-gradient(135deg, #B8860B 0%, #D4A574 100%);
        height: 400px;
        border-radius: 2px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 100px;
        color: rgba(255, 255, 255, 0.2);
    }
    
    /* ROOMS SECTION */
    .rooms-section {
        padding: 100px 80px;
        background: #f5f3f0;
    }
    
    .rooms-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .room-card {
        background: white;
        border-radius: 2px;
        overflow: hidden;
        transition: all 0.4s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    .room-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
    }
    
    .room-image {
        background: linear-gradient(135deg, #D4A574 0%, #B8860B 100%);
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        color: rgba(255, 255, 255, 0.2);
    }
    
    .room-content {
        padding: 40px;
    }
    
    .room-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #1a1a1a;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .room-desc {
        font-size: 14px;
        color: #666666;
        line-height: 1.7;
        margin-bottom: 20px;
        font-weight: 300;
    }
    
    .room-price {
        font-size: 24px;
        font-weight: 700;
        color: #B8860B;
        margin-bottom: 20px;
    }
    
    .room-cta {
        background: #B8860B;
        color: white;
        padding: 12px 32px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 12px;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .room-cta:hover {
        background: #9a7009;
    }
    
    /* SERVICES SECTION */
    .services-section {
        padding: 100px 80px;
        background: white;
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .service-card {
        text-align: center;
        padding: 40px;
        border-radius: 2px;
        background: #f9f7f4;
        transition: all 0.4s ease;
    }
    
    .service-card:hover {
        background: white;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }
    
    .service-icon {
        font-size: 48px;
        margin-bottom: 20px;
    }
    
    .service-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #1a1a1a;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .service-desc {
        font-size: 14px;
        color: #666666;
        line-height: 1.7;
        font-weight: 300;
    }
    
    /* TESTIMONIALS SECTION */
    .testimonials-section {
        padding: 100px 80px;
        background: #f5f3f0;
    }
    
    .testimonial-card {
        background: white;
        padding: 50px;
        border-radius: 2px;
        margin-bottom: 30px;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    .testimonial-text {
        font-size: 16px;
        color: #2c2c2c;
        line-height: 1.9;
        margin-bottom: 20px;
        font-style: italic;
        font-weight: 300;
    }
    
    .testimonial-author {
        font-size: 14px;
        font-weight: 700;
        color: #1a1a1a;
        font-family: 'Playfair Display', serif;
    }
    
    .testimonial-role {
        font-size: 12px;
        color: #B8860B;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* CTA FINAL SECTION */
    .cta-final-section {
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), linear-gradient(135deg, #8B7355 0%, #A0826D 100%);
        color: white;
        padding: 120px 80px;
        text-align: center;
    }
    
    .cta-final-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
        letter-spacing: 1px;
        font-family: 'Playfair Display', serif;
    }
    
    .cta-final-desc {
        font-size: 18px;
        margin-bottom: 50px;
        opacity: 0.95;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;
    }
    
    .cta-final-button {
        background: #B8860B;
        color: white;
        padding: 16px 50px;
        border: none;
        border-radius: 2px;
        font-weight: 700;
        font-size: 13px;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .cta-final-button:hover {
        background: #9a7009;
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(184, 134, 11, 0.4);
    }
    
    /* FOOTER */
    .footer {
        background: #1a1a1a;
        color: rgba(255, 255, 255, 0.7);
        padding: 80px;
        text-align: center;
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 300;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(184, 134, 11, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
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
            height: 400px;
        }
        
        .hero-title {
            font-size: 36px;
        }
        
        .about-grid {
            grid-template-columns: 1fr;
            gap: 40px;
        }
        
        .about-section,
        .rooms-section,
        .services-section,
        .testimonials-section,
        .cta-final-section,
        .booking-section {
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
navbar_html = '<div class="navbar"><a href="#" class="navbar-logo">LUXE<span class="navbar-logo-highlight">RESORT</span></a><div class="navbar-links"><a href="#" class="navbar-link">Acomodações</a><a href="#" class="navbar-link">Serviços</a><a href="#" class="navbar-link">Experiências</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Reservar</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">Luxo Absoluto</div>
        <div class="hero-subtitle">Uma experiência de hospedagem incomparável</div>
        <button class="hero-cta">Descobrir Mais</button>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== BOOKING SECTION ====================
booking_html = '''<div class="booking-section">
    <div class="booking-card">
        <div class="booking-title">Verificar Disponibilidade</div>
        <div class="booking-grid">
            <input type="date" class="booking-input" placeholder="Data de Chegada">
            <input type="date" class="booking-input" placeholder="Data de Saída">
            <select class="booking-input">
                <option>Hóspedes</option>
                <option>1 Hóspede</option>
                <option>2 Hóspedes</option>
                <option>3+ Hóspedes</option>
            </select>
            <button class="booking-button">Verificar</button>
        </div>
    </div>
</div>'''
st.markdown(booking_html, unsafe_allow_html=True)

# ==================== ABOUT SECTION ====================
about_html = '''<div class="about-section">
    <div class="section-header">
        <div class="section-title">Bem-vindo ao <span class="section-title-highlight">LuxeResort</span></div>
        <div class="section-description">Onde o luxo encontra a elegância em perfeita harmonia</div>
    </div>
    <div class="about-grid">
        <div class="about-text">
            <h3>Uma Experiência Inesquecível</h3>
            <p>Nosso resort de luxo oferece o melhor em hospedagem, gastronomia e bem-estar. Cada detalhe foi cuidadosamente pensado para proporcionar conforto absoluto e uma experiência memorável.</p>
            <p>Com suítes elegantemente decoradas, serviço impecável e amenidades de classe mundial, garantimos que sua estadia seja simplesmente extraordinária.</p>
        </div>
        <div class="about-image"></div>
    </div>
</div>'''
st.markdown(about_html, unsafe_allow_html=True)

# ==================== ROOMS SECTION ====================
rooms_html = '''<div class="rooms-section">
    <div class="section-header">
        <div class="section-title">Nossas <span class="section-title-highlight">Acomodações</span></div>
        <div class="section-description">Suítes e bangalôs de luxo com vista panorâmica</div>
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
                <div class="room-desc">Luxo incomparável com vista para o mar. Jacuzzi privado, serviço de butler e acesso VIP a todos os serviços.</div>
                <div class="room-price">R$ 1.800/noite</div>
                <button class="room-cta">Reservar</button>
            </div>
        </div>
        <div class="room-card">
            <div class="room-image"></div>
            <div class="room-content">
                <div class="room-title">Villa Privativa</div>
                <div class="room-desc">Isolamento total e privacidade absoluta. Piscina privada, spa pessoal e chef particular disponível.</div>
                <div class="room-price">R$ 3.500/noite</div>
                <button class="room-cta">Reservar</button>
            </div>
        </div>
    </div>
</div>'''
st.markdown(rooms_html, unsafe_allow_html=True)

# ==================== SERVICES SECTION ====================
services_html = '''<div class="services-section">
    <div class="section-header">
        <div class="section-title">Serviços <span class="section-title-highlight">Exclusivos</span></div>
        <div class="section-description">Tudo que você precisa para uma estadia perfeita</div>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-icon">🍽️</div>
            <div class="service-title">Gastronomia Refinada</div>
            <div class="service-desc">Restaurantes gourmet com chefs renomados e culinária internacional de alta qualidade.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">🧖</div>
            <div class="service-title">Spa de Luxo</div>
            <div class="service-desc">Tratamentos de bem-estar com produtos premium e terapeutas especializados.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">🏊</div>
            <div class="service-title">Piscinas Aquecidas</div>
            <div class="service-desc">Piscinas de água salgada aquecida com vista panorâmica e serviço de bar.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">🎭</div>
            <div class="service-title">Entretenimento</div>
            <div class="service-desc">Shows ao vivo, eventos especiais e atividades de lazer para toda a família.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">🚗</div>
            <div class="service-title">Transporte VIP</div>
            <div class="service-desc">Serviço de transfer com veículos de luxo e motorista particular.</div>
        </div>
        <div class="service-card">
            <div class="service-icon">🎯</div>
            <div class="service-title">Concierge 24/7</div>
            <div class="service-desc">Atendimento personalizado para todas as suas necessidades e desejos.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# ==================== TESTIMONIALS SECTION ====================
testimonials_html = '''<div class="testimonials-section">
    <div class="section-header">
        <div class="section-title">Avaliações de <span class="section-title-highlight">Hóspedes</span></div>
        <div class="section-description">O que nossos clientes dizem sobre sua experiência</div>
    </div>
    <div class="testimonial-card">
        <div class="testimonial-text">"Uma experiência absolutamente magnífica. Cada detalhe foi perfeito, desde o atendimento impecável até as acomodações luxuosas. Voltaremos com certeza!"</div>
        <div class="testimonial-author">Mariana Silva</div>
        <div class="testimonial-role">Hóspede Premium</div>
    </div>
    <div class="testimonial-card">
        <div class="testimonial-text">"O melhor resort que já visitei. A gastronomia é de classe mundial, o spa é extraordinário e a equipe é extremamente atenciosa. Recomendo para todos!"</div>
        <div class="testimonial-author">Carlos Mendes</div>
        <div class="testimonial-role">Hóspede VIP</div>
    </div>
    <div class="testimonial-card">
        <div class="testimonial-text">"Luxo, elegância e conforto em perfeita harmonia. Cada momento foi especial. A villa privativa superou todas as expectativas. Simplesmente perfeito!"</div>
        <div class="testimonial-author">Juliana Costa</div>
        <div class="testimonial-role">Hóspede Elite</div>
    </div>
</div>'''
st.markdown(testimonials_html, unsafe_allow_html=True)

# ==================== CTA FINAL SECTION ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-title">Reserve Sua Experiência</div>
    <div class="cta-final-desc">Viva momentos inesquecíveis em nosso resort de luxo. Acomodações exclusivas, serviços impecáveis e memórias para a vida toda.</div>
    <button class="cta-final-button">Fazer Reserva Agora</button>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">Telefone: +55 (11) 98765-4321 | Email: reservas@luxeresort.com.br</div><div class="footer-text">Endereço: Av. Costeira, 5000 - Praia Paradisíaca, SP</div><div class="footer-copyright">© 2025 LuxeResort. Todos os direitos reservados. Experiência de luxo absoluto.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
