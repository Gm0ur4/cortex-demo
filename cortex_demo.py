import streamlit as st

st.set_page_config(
    page_title="Landing Page - Conversão Premium",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d1117 100%);
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    @keyframes heroSlide {
        0% { transform: translateX(-100px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes counterUp {
        0% { transform: translateY(30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes lineExpand {
        0% { width: 0; }
        100% { width: 100%; }
    }
    
    @keyframes faqSlide {
        0% { max-height: 0; opacity: 0; }
        100% { max-height: 500px; opacity: 1; }
    }
    
    @keyframes featureFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    @keyframes ctaPulse {
        0%, 100% { box-shadow: 0 0 20px rgba(34, 197, 94, 0.3); }
        50% { box-shadow: 0 0 50px rgba(34, 197, 94, 0.7); }
    }
    
    /* NAVBAR */
    .navbar {
        background: rgba(13, 17, 23, 0.95);
        backdrop-filter: blur(30px);
        padding: 20px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(34, 197, 94, 0.15);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 900;
        background: linear-gradient(90deg, #22c55e 0%, #16a34a 100%);
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
        color: #8b949e;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
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
        background: #22c55e;
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after { width: 100%; }
    .nav-link:hover { color: #22c55e; }
    
    /* HERO SECTION */
    .hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 100px 80px;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(34, 197, 94, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        top: -300px;
        right: -300px;
    }
    
    .hero::after {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(34, 197, 94, 0.05) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -200px;
        left: -200px;
    }
    
    .hero-content {
        max-width: 600px;
        position: relative;
        z-index: 2;
        animation: heroSlide 1s ease-out;
    }
    
    .hero-label {
        font-size: 13px;
        color: #22c55e;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
        font-weight: 800;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 25px;
        font-family: 'Syne', sans-serif;
        letter-spacing: -1px;
    }
    
    .hero-desc {
        font-size: 18px;
        color: #8b949e;
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
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        color: #ffffff;
        padding: 16px 50px;
        border: none;
        border-radius: 6px;
        font-weight: 800;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 30px rgba(34, 197, 94, 0.3);
        animation: ctaPulse 2s ease-in-out infinite;
    }
    
    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 60px rgba(34, 197, 94, 0.7);
    }
    
    .btn-secondary {
        background: transparent;
        color: #22c55e;
        padding: 16px 50px;
        border: 2px solid #22c55e;
        border-radius: 6px;
        font-weight: 800;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-secondary:hover {
        background: rgba(34, 197, 94, 0.1);
    }
    
    .hero-visual {
        position: relative;
        z-index: 2;
        width: 400px;
        height: 500px;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(22, 163, 74, 0.05));
        border: 2px solid rgba(34, 197, 94, 0.2);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 100px;
    }
    
    /* BENEFITS SECTION - NOVO ELEMENTO */
    .benefits-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
    }
    
    .benefits-container {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 50px;
    }
    
    .benefit-item {
        padding: 50px;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.05), rgba(34, 197, 94, 0.02));
        border-left: 4px solid #22c55e;
        border-radius: 8px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: counterUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .benefit-item:nth-child(1) { animation-delay: 0.1s; }
    .benefit-item:nth-child(2) { animation-delay: 0.2s; }
    .benefit-item:nth-child(3) { animation-delay: 0.3s; }
    
    .benefit-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(34, 197, 94, 0.1), transparent);
        transition: left 0.6s ease;
    }
    
    .benefit-item:hover::before { left: 100%; }
    
    .benefit-item:hover {
        transform: translateY(-10px);
        border-left-color: #16a34a;
        box-shadow: 0 0 40px rgba(34, 197, 94, 0.2);
    }
    
    .benefit-number {
        font-size: 48px;
        font-weight: 900;
        color: #22c55e;
        margin-bottom: 20px;
        font-family: 'Syne', sans-serif;
    }
    
    .benefit-title {
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #ffffff;
    }
    
    .benefit-desc {
        font-size: 15px;
        color: #8b949e;
        line-height: 1.8;
    }
    
    /* FEATURES SECTION - NOVO LAYOUT */
    .features-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 100px;
        font-family: 'Syne', sans-serif;
        letter-spacing: -1px;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 60px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .feature-block {
        display: flex;
        gap: 40px;
        align-items: flex-start;
        padding: 50px;
        border: 1px solid rgba(34, 197, 94, 0.15);
        border-radius: 8px;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.03), transparent);
        transition: all 0.4s ease;
        animation: featureFloat 3s ease-in-out infinite;
    }
    
    .feature-block:nth-child(1) { animation-delay: 0s; }
    .feature-block:nth-child(2) { animation-delay: 0.5s; }
    .feature-block:nth-child(3) { animation-delay: 1s; }
    .feature-block:nth-child(4) { animation-delay: 1.5s; }
    
    .feature-block:hover {
        border-color: #22c55e;
        box-shadow: 0 0 40px rgba(34, 197, 94, 0.2);
    }
    
    .feature-icon {
        font-size: 48px;
        min-width: 60px;
    }
    
    .feature-content h3 {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 12px;
        color: #ffffff;
    }
    
    .feature-content p {
        font-size: 15px;
        color: #8b949e;
        line-height: 1.8;
    }
    
    /* FAQ SECTION - ELEMENTO NOVO */
    .faq-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
    }
    
    .faq-container {
        max-width: 900px;
        margin: 0 auto;
    }
    
    .faq-item {
        margin-bottom: 20px;
        border: 1px solid rgba(34, 197, 94, 0.15);
        border-radius: 8px;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.03), transparent);
        transition: all 0.3s ease;
    }
    
    .faq-item:hover {
        border-color: #22c55e;
        box-shadow: 0 0 30px rgba(34, 197, 94, 0.15);
    }
    
    .faq-question {
        padding: 25px 30px;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        font-size: 16px;
        color: #ffffff;
        transition: all 0.3s ease;
    }
    
    .faq-question:hover {
        color: #22c55e;
    }
    
    .faq-arrow {
        font-size: 20px;
        transition: transform 0.3s ease;
    }
    
    .faq-item.active .faq-arrow {
        transform: rotate(180deg);
    }
    
    .faq-answer {
        padding: 0 30px;
        max-height: 0;
        overflow: hidden;
        transition: all 0.3s ease;
        color: #8b949e;
        font-size: 15px;
        line-height: 1.8;
    }
    
    .faq-item.active .faq-answer {
        padding: 0 30px 25px 30px;
        max-height: 500px;
    }
    
    /* PRICING SECTION */
    .pricing-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    }
    
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .pricing-card {
        padding: 50px;
        border: 2px solid rgba(34, 197, 94, 0.2);
        border-radius: 8px;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.05), rgba(34, 197, 94, 0.02));
        transition: all 0.4s ease;
        position: relative;
        animation: counterUp 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .pricing-card:nth-child(1) { animation-delay: 0.1s; }
    .pricing-card:nth-child(2) { animation-delay: 0.2s; }
    .pricing-card:nth-child(3) { animation-delay: 0.3s; }
    
    .pricing-card:hover {
        transform: translateY(-15px);
        border-color: #22c55e;
        box-shadow: 0 0 50px rgba(34, 197, 94, 0.3);
    }
    
    .pricing-name {
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #ffffff;
    }
    
    .pricing-price {
        font-size: 48px;
        font-weight: 900;
        color: #22c55e;
        margin-bottom: 10px;
        font-family: 'Syne', sans-serif;
    }
    
    .pricing-period {
        font-size: 13px;
        color: #8b949e;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .pricing-features {
        list-style: none;
        margin-bottom: 40px;
    }
    
    .pricing-features li {
        padding: 12px 0;
        color: #8b949e;
        font-size: 14px;
        border-bottom: 1px solid rgba(34, 197, 94, 0.1);
    }
    
    .pricing-features li::before {
        content: '✓ ';
        color: #22c55e;
        font-weight: 800;
        margin-right: 10px;
    }
    
    .pricing-btn {
        width: 100%;
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        color: #ffffff;
        padding: 14px;
        border: none;
        border-radius: 6px;
        font-weight: 800;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .pricing-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 30px rgba(34, 197, 94, 0.4);
    }
    
    /* CTA FINAL */
    .cta-final {
        padding: 150px 80px;
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-final::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(13, 17, 23, 0.1);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-final-title {
        font-size: 56px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 30px;
        font-family: 'Syne', sans-serif;
        letter-spacing: -1px;
    }
    
    .cta-final-desc {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.95);
        max-width: 700px;
        margin: 0 auto 50px;
    }
    
    .cta-final-btn {
        background: #0d1117;
        color: #22c55e;
        padding: 18px 60px;
        border: 2px solid #0d1117;
        border-radius: 6px;
        font-weight: 800;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .cta-final-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(13, 17, 23, 0.3);
    }
    
    /* FOOTER */
    .footer {
        background: #0d1117;
        color: #8b949e;
        padding: 80px;
        text-align: center;
        border-top: 1px solid rgba(34, 197, 94, 0.15);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 15px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(34, 197, 94, 0.15);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .hero { flex-direction: column; padding: 50px 20px; min-height: auto; }
        .hero-title { font-size: 42px; }
        .hero-visual { width: 100%; margin-top: 40px; }
        .benefits-container { grid-template-columns: 1fr; gap: 30px; }
        .features-grid { grid-template-columns: 1fr; gap: 30px; }
        .pricing-grid { grid-template-columns: 1fr; }
        .cta-final { padding: 100px 20px; }
        .cta-final-title { font-size: 36px; }
        .section-title { font-size: 36px; }
    }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.querySelector('.faq-question').addEventListener('click', function() {
            item.classList.toggle('active');
        });
    });
});
</script>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# NAVBAR
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">CONVERSÃO</div>
    <div class="navbar-nav">
        <a href="#" class="nav-link">Benefícios</a>
        <a href="#" class="nav-link">Recursos</a>
        <a href="#" class="nav-link">Preços</a>
        <a href="#" class="nav-link">FAQ</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# HERO
hero_html = '''<div class="hero">
    <div class="hero-content">
        <div class="hero-label">Bem-vindo</div>
        <div class="hero-title">Aumente suas Vendas em 300%</div>
        <div class="hero-desc">Solução completa para transformar visitantes em clientes. Tecnologia comprovada que gera resultados reais.</div>
        <div class="hero-cta">
            <button class="btn-primary">Começar Agora</button>
            <button class="btn-secondary">Ver Demo</button>
        </div>
    </div>
    <div class="hero-visual">📈</div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# BENEFITS
benefits_html = '''<div class="benefits-section">
    <div class="benefits-container">
        <div class="benefit-item">
            <div class="benefit-number">10x</div>
            <div class="benefit-title">Mais Rápido</div>
            <div class="benefit-desc">Implementação em minutos, não em meses. Comece a gerar resultados imediatamente.</div>
        </div>
        <div class="benefit-item">
            <div class="benefit-number">99.9%</div>
            <div class="benefit-title">Uptime</div>
            <div class="benefit-desc">Infraestrutura robusta garantindo disponibilidade total do seu negócio.</div>
        </div>
        <div class="benefit-item">
            <div class="benefit-number">24/7</div>
            <div class="benefit-title">Suporte</div>
            <div class="benefit-desc">Equipe dedicada pronta para ajudar em qualquer momento do dia.</div>
        </div>
    </div>
</div>'''
st.markdown(benefits_html, unsafe_allow_html=True)

# FEATURES
features_html = '''<div class="features-section">
    <div class="section-title">Recursos Poderosos</div>
    <div class="features-grid">
        <div class="feature-block">
            <div class="feature-icon">⚡</div>
            <div class="feature-content">
                <h3>Performance</h3>
                <p>Velocidade de carregamento otimizada para máxima conversão e SEO.</p>
            </div>
        </div>
        <div class="feature-block">
            <div class="feature-icon">🔒</div>
            <div class="feature-content">
                <h3>Segurança</h3>
                <p>Criptografia de ponta a ponta e conformidade com LGPD.</p>
            </div>
        </div>
        <div class="feature-block">
            <div class="feature-icon">📊</div>
            <div class="feature-content">
                <h3>Analytics</h3>
                <p>Dados em tempo real para otimizar suas campanhas continuamente.</p>
            </div>
        </div>
        <div class="feature-block">
            <div class="feature-icon">🎯</div>
            <div class="feature-content">
                <h3>Personalização</h3>
                <p>Customize cada aspecto para sua marca e público-alvo.</p>
            </div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# FAQ
faq_html = '''<div class="faq-section">
    <div class="section-title">Perguntas Frequentes</div>
    <div class="faq-container">
        <div class="faq-item">
            <div class="faq-question">
                Como funciona a integração?
                <span class="faq-arrow">▼</span>
            </div>
            <div class="faq-answer">
                A integração é simples e rápida. Você recebe um código que adiciona ao seu site em minutos. Nosso time técnico está disponível para ajudar em cada passo.
            </div>
        </div>
        <div class="faq-item">
            <div class="faq-question">
                Qual é o tempo de implementação?
                <span class="faq-arrow">▼</span>
            </div>
            <div class="faq-answer">
                A maioria dos clientes começa a ver resultados em menos de 48 horas. A implementação completa leva entre 1-2 semanas dependendo da complexidade.
            </div>
        </div>
        <div class="faq-item">
            <div class="faq-question">
                Posso cancelar a qualquer momento?
                <span class="faq-arrow">▼</span>
            </div>
            <div class="faq-answer">
                Sim, sem contratos de longo prazo. Você pode cancelar sua assinatura a qualquer momento, sem multas ou taxas adicionais.
            </div>
        </div>
        <div class="faq-item">
            <div class="faq-question">
                Qual suporte vocês oferecem?
                <span class="faq-arrow">▼</span>
            </div>
            <div class="faq-answer">
                Oferecemos suporte 24/7 via chat, email e telefone. Além disso, você tem acesso a documentação completa e webinars de treinamento.
            </div>
        </div>
        <div class="faq-item">
            <div class="faq-question">
                Como vocês garantem a segurança dos dados?
                <span class="faq-arrow">▼</span>
            </div>
            <div class="faq-answer">
                Utilizamos criptografia de ponta a ponta, servidores em data centers certificados e conformidade total com LGPD e GDPR.
            </div>
        </div>
    </div>
</div>'''
st.markdown(faq_html, unsafe_allow_html=True)

# PRICING
pricing_html = '''<div class="pricing-section">
    <div class="section-title">Planos Simples</div>
    <div class="pricing-grid">
        <div class="pricing-card">
            <div class="pricing-name">Starter</div>
            <div class="pricing-price">R$ 99</div>
            <div class="pricing-period">Por mês</div>
            <ul class="pricing-features">
                <li>Até 1.000 visitantes</li>
                <li>1 formulário</li>
                <li>Suporte por email</li>
                <li>Relatórios básicos</li>
            </ul>
            <button class="pricing-btn">Começar</button>
        </div>
        <div class="pricing-card">
            <div class="pricing-name">Professional</div>
            <div class="pricing-price">R$ 299</div>
            <div class="pricing-period">Por mês</div>
            <ul class="pricing-features">
                <li>Até 10.000 visitantes</li>
                <li>Formulários ilimitados</li>
                <li>Suporte prioritário</li>
                <li>Relatórios avançados</li>
            </ul>
            <button class="pricing-btn">Começar</button>
        </div>
        <div class="pricing-card">
            <div class="pricing-name">Enterprise</div>
            <div class="pricing-price">R$ 999</div>
            <div class="pricing-period">Por mês</div>
            <ul class="pricing-features">
                <li>Visitantes ilimitados</li>
                <li>Tudo ilimitado</li>
                <li>Suporte 24/7 dedicado</li>
                <li>Consultoria estratégica</li>
            </ul>
            <button class="pricing-btn">Começar</button>
        </div>
    </div>
</div>'''
st.markdown(pricing_html, unsafe_allow_html=True)

# CTA FINAL
cta_html = '''<div class="cta-final">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronto para Crescer?</div>
        <div class="cta-final-desc">Junte-se a milhares de empresas que já aumentaram suas vendas com nossa plataforma.</div>
        <button class="cta-final-btn">Comece Agora Grátis</button>
    </div>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# FOOTER
footer_html = '''<div class="footer">
    <div class="footer-text">Email: contato@conversao.com | Telefone: +55 (11) 98765-4321</div>
    <div class="footer-text">LinkedIn: linkedin.com/company/conversao | Website: conversao.com</div>
    <div class="footer-copyright">© 2025 Conversão Premium. Todos os direitos reservados.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
