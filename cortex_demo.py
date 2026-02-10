import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Agência Digital - Transforme seu Negócio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ULTRA PROFISSIONAL - INSPIRADO EM GREATPAGES
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #ffffff;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        color: #1a1a1a;
        line-height: 1.6;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: #ffffff;
    }
    
    /* NAVBAR */
    .navbar {
        background: #ffffff;
        padding: 16px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #f0f0f0;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 900;
        color: #0066FF;
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: #1a1a1a;
        text-decoration: none;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .navbar-link:hover {
        color: #0066FF;
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, #0066FF, #0052CC);
        color: white;
        padding: 10px 28px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.2);
    }
    
    .navbar-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 102, 255, 0.3);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(180deg, #ffffff 0%, #f8f9ff 100%);
        padding: 120px 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(0, 102, 255, 0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(0, 102, 255, 0.05) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 64px;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 24px;
        color: #1a1a1a;
        letter-spacing: -1px;
    }
    
    .hero-title-highlight {
        color: #0066FF;
    }
    
    .hero-subtitle {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 50px;
        color: #666666;
        font-weight: 400;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 80px;
        margin-top: 60px;
        padding-top: 60px;
        border-top: 1px solid #e0e0e0;
    }
    
    .hero-stat {
        text-align: center;
    }
    
    .hero-stat-number {
        font-size: 36px;
        font-weight: 900;
        color: #0066FF;
        margin-bottom: 8px;
    }
    
    .hero-stat-label {
        font-size: 14px;
        color: #666666;
        font-weight: 500;
    }
    
    /* BADGES */
    .badges-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 30px;
    }
    
    .badge {
        background: #f0f0f0;
        color: #1a1a1a;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    
    .badge-icon {
        font-size: 14px;
    }
    
    .badge-primary {
        background: #0066FF;
        color: white;
    }
    
    .badge-success {
        background: #00AA44;
        color: white;
    }
    
    .badge-warning {
        background: #FF6600;
        color: white;
    }
    
    /* BUTTONS */
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #0066FF, #0052CC);
        color: white;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.25);
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 102, 255, 0.35);
    }
    
    .cta-button-secondary {
        background: white;
        color: #0066FF;
        border: 2px solid #0066FF;
        box-shadow: none;
    }
    
    .cta-button-secondary:hover {
        background: #f0f6ff;
    }
    
    /* FEATURES SECTION */
    .features-section {
        padding: 100px 60px;
        background: #ffffff;
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
        letter-spacing: -0.5px;
    }
    
    .section-title-highlight {
        color: #0066FF;
    }
    
    .section-description {
        font-size: 18px;
        color: #666666;
        line-height: 1.7;
        font-weight: 400;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .feature-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        transition: all 0.4s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: #0066FF;
        box-shadow: 0 12px 40px rgba(0, 102, 255, 0.12);
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 20px;
        display: inline-block;
    }
    
    .feature-title {
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 12px;
        color: #1a1a1a;
    }
    
    .feature-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.7;
    }
    
    /* SERVICES SECTION */
    .services-section {
        padding: 100px 60px;
        background: #f8f9ff;
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .service-card {
        background: white;
        padding: 50px 40px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        text-align: center;
        transition: all 0.4s ease;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        border-color: #0066FF;
        box-shadow: 0 16px 48px rgba(0, 102, 255, 0.15);
    }
    
    .service-number {
        font-size: 48px;
        font-weight: 900;
        color: #0066FF;
        margin-bottom: 16px;
    }
    
    .service-title {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 16px;
        color: #1a1a1a;
    }
    
    .service-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.7;
    }
    
    /* TESTIMONIALS SECTION */
    .testimonials-section {
        padding: 100px 60px;
        background: #ffffff;
    }
    
    .testimonial-card {
        background: #f8f9ff;
        padding: 40px;
        border-radius: 12px;
        border-left: 4px solid #0066FF;
        margin-bottom: 30px;
    }
    
    .testimonial-text {
        font-size: 16px;
        color: #1a1a1a;
        line-height: 1.8;
        margin-bottom: 20px;
        font-style: italic;
    }
    
    .testimonial-author {
        font-size: 14px;
        font-weight: 700;
        color: #1a1a1a;
    }
    
    .testimonial-role {
        font-size: 13px;
        color: #666666;
        font-weight: 500;
    }
    
    /* CTA FINAL SECTION */
    .cta-final-section {
        background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);
        color: white;
        padding: 100px 60px;
        text-align: center;
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
        opacity: 0.95;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .cta-final-button {
        background: white;
        color: #0066FF;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .cta-final-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }
    
    /* FOOTER */
    .footer {
        background: #1a1a1a;
        color: rgba(255, 255, 255, 0.7);
        padding: 60px;
        text-align: center;
    }
    
    .footer-text {
        font-size: 15px;
        margin-bottom: 10px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
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
        
        .hero-section {
            padding: 60px 20px;
        }
        
        .hero-title {
            font-size: 36px;
        }
        
        .hero-stats {
            flex-direction: column;
            gap: 40px;
        }
        
        .features-section,
        .services-section,
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
navbar_html = '<div class="navbar"><a href="#" class="navbar-logo">🚀 Agência Digital</a><div class="navbar-links"><a href="#" class="navbar-link">Serviços</a><a href="#" class="navbar-link">Sobre</a><a href="#" class="navbar-link">Portfólio</a><a href="#" class="navbar-link">Contato</a><a href="#" class="navbar-cta">Começar Agora</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="badges-container">
            <div class="badge badge-primary"><span class="badge-icon">⭐</span> Agência Premium</div>
            <div class="badge"><span class="badge-icon">🏆</span> Prêmio Melhor Agência 2024</div>
            <div class="badge"><span class="badge-icon">✓</span> +500 Clientes Satisfeitos</div>
        </div>
        <div class="hero-title">Transforme seu negócio com <span class="hero-title-highlight">marketing digital estratégico</span></div>
        <div class="hero-subtitle">Crescimento comprovado através de estratégias personalizadas, criatividade e tecnologia de ponta</div>
        <button class="cta-button">Agende uma Consultoria Gratuita</button>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-number">+500%</div>
                <div class="hero-stat-label">Crescimento Médio em Vendas</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-number">98%</div>
                <div class="hero-stat-label">Taxa de Satisfação de Clientes</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-number">12+</div>
                <div class="hero-stat-label">Anos de Experiência</div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
features_html = '''<div class="features-section">
    <div class="section-header">
        <div class="section-title">Por que escolher nossa <span class="section-title-highlight">agência?</span></div>
        <div class="section-description">Oferecemos soluções completas de marketing digital que transformam visitantes em clientes</div>
    </div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Estratégia Personalizada</div>
            <div class="feature-desc">Cada negócio é único. Criamos estratégias sob medida para seus objetivos específicos.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Resultados Mensuráveis</div>
            <div class="feature-desc">Relatórios detalhados e transparentes. Você acompanha cada métrica em tempo real.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Crescimento Acelerado</div>
            <div class="feature-desc">Técnicas comprovadas para aumentar sua visibilidade e conversões rapidamente.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Inovação Constante</div>
            <div class="feature-desc">Sempre atualizados com as últimas tendências e tecnologias do mercado.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">👥</div>
            <div class="feature-title">Equipe Experiente</div>
            <div class="feature-desc">Profissionais certificados com experiência em diversos segmentos de mercado.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <div class="feature-title">Parceria de Longo Prazo</div>
            <div class="feature-desc">Não somos apenas fornecedores, somos parceiros no crescimento do seu negócio.</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ==================== SERVICES SECTION ====================
services_html = '''<div class="services-section">
    <div class="section-header">
        <div class="section-title">Nossos <span class="section-title-highlight">Serviços</span></div>
        <div class="section-description">Soluções completas de marketing digital para impulsionar seu negócio</div>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-number">01</div>
            <div class="service-title">Google Ads</div>
            <div class="service-desc">Campanhas otimizadas para máximo ROI. Anúncios que convertem visitantes em clientes.</div>
        </div>
        <div class="service-card">
            <div class="service-number">02</div>
            <div class="service-title">Social Media</div>
            <div class="service-desc">Gestão completa de redes sociais com conteúdo estratégico e engajamento real.</div>
        </div>
        <div class="service-card">
            <div class="service-number">03</div>
            <div class="service-title">SEO Avançado</div>
            <div class="service-desc">Posicionamento orgânico no Google para tráfego qualificado e sustentável.</div>
        </div>
        <div class="service-card">
            <div class="service-number">04</div>
            <div class="service-title">Criação de Conteúdo</div>
            <div class="service-desc">Conteúdo de qualidade que atrai, engaja e converte seu público-alvo.</div>
        </div>
        <div class="service-card">
            <div class="service-number">05</div>
            <div class="service-title">Email Marketing</div>
            <div class="service-desc">Campanhas de email segmentadas com alta taxa de abertura e conversão.</div>
        </div>
        <div class="service-card">
            <div class="service-number">06</div>
            <div class="service-title">Análise e Relatórios</div>
            <div class="service-desc">Dados precisos e insights acionáveis para otimizar suas estratégias.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# ==================== TESTIMONIALS SECTION ====================
testimonials_html = '''<div class="testimonials-section">
    <div class="section-header">
        <div class="section-title">O que nossos <span class="section-title-highlight">clientes dizem</span></div>
        <div class="section-description">Histórias reais de sucesso e transformação digital</div>
    </div>
    <div style="max-width: 900px; margin: 0 auto;">
        <div class="testimonial-card">
            <div class="testimonial-text">"A agência transformou completamente meu negócio. Em 6 meses, triplicamos nossas vendas. Profissionais incríveis!"</div>
            <div class="testimonial-author">João Silva</div>
            <div class="testimonial-role">CEO - E-commerce Fashion</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"Melhor investimento que fiz. O retorno foi imediato e os resultados continuam crescendo. Recomendo muito!"</div>
            <div class="testimonial-author">Maria Santos</div>
            <div class="testimonial-role">Proprietária - Consultoria Empresarial</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"Equipe profissional, dedicada e com resultados comprovados. Não tenho dúvidas em recomendar para qualquer negócio."</div>
            <div class="testimonial-author">Carlos Oliveira</div>
            <div class="testimonial-role">Diretor - Agência Imobiliária</div>
        </div>
    </div>
</div>'''
st.markdown(testimonials_html, unsafe_allow_html=True)

# ==================== CTA FINAL SECTION ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-title">Pronto para crescer?</div>
    <div class="cta-final-desc">Agende uma consultoria gratuita com nossos especialistas e descubra como podemos transformar seu negócio</div>
    <button class="cta-final-button">Agende Agora</button>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">📞 (11) 98765-4321 | 📧 contato@agenciadigital.com.br</div><div class="footer-text">📍 São Paulo, SP - Brasil</div><div class="footer-copyright">© 2025 Agência Digital. Todos os direitos reservados. Transformando negócios através do marketing digital.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
