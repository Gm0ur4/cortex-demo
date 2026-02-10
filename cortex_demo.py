# -*- coding: utf-8 -*-
"""
Landing Page Premium em Streamlit - Nexus AI

Autor: Manus AI
Data: 10 de Fevereiro de 2026

Uma landing page profissional e interativa para maximizar conversões.
Inclui design moderno, animações CSS, componentes interativos e estrutura
otimizada para vendas.
"""

import streamlit as st

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(
    page_title="Nexus AI - Transforme Seus Dados em Lucro",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INJETAR CSS CUSTOMIZADO ---
st.markdown('''
<style>
    /* === RESET E ESTILOS GERAIS === */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);
        color: #e0e0e0;
        line-height: 1.6;
    }
    
    .main {
        background: transparent;
    }
    
    /* === SEÇÃO HERO === */
    .hero-section {
        background: linear-gradient(135deg, rgba(15, 15, 30, 0.9) 0%, rgba(26, 26, 46, 0.9) 50%, rgba(22, 33, 62, 0.9) 100%);
        padding: 6rem 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        border-bottom: 2px solid rgba(0, 188, 212, 0.3);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(0, 188, 212, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(255, 64, 129, 0.1) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .hero-text {
        position: relative;
        z-index: 1;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #00bcd4 0%, #ff4081 50%, #00bcd4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 3s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(10deg); }
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #b0b0b0;
        margin-bottom: 2.5rem;
        line-height: 1.8;
    }
    
    .hero-button {
        display: inline-block;
        background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);
        color: white;
        padding: 1.2rem 2.5rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0, 188, 212, 0.3);
        border: 2px solid transparent;
    }
    
    .hero-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 188, 212, 0.5);
        background: linear-gradient(135deg, #0097a7 0%, #00838f 100%);
    }
    
    .hero-subtext {
        margin-top: 1.5rem;
        color: #888;
        font-size: 0.95rem;
    }
    
    /* === SEÇÕES GERAIS === */
    .section {
        padding: 5rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .section-title {
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 3rem;
        color: #00bcd4;
        position: relative;
        padding-bottom: 1rem;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #00bcd4, #ff4081);
        border-radius: 2px;
    }
    
    /* === CARDS DE FEATURES === */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 188, 212, 0.05) 100%);
        border: 1px solid rgba(0, 188, 212, 0.2);
        border-radius: 15px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        border-color: rgba(0, 188, 212, 0.5);
        box-shadow: 0 20px 40px rgba(0, 188, 212, 0.2);
        background: linear-gradient(135deg, rgba(0, 188, 212, 0.1) 0%, rgba(255, 64, 129, 0.05) 100%);
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: inline-block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .feature-card h3 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #00bcd4;
    }
    
    .feature-card p {
        color: #a0a0a0;
        line-height: 1.7;
    }
    
    /* === SEÇÃO DE LOGOS === */
    .logos-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 3rem;
        flex-wrap: wrap;
        margin: 3rem 0;
        opacity: 0.7;
    }
    
    .logo-item {
        font-size: 1.3rem;
        font-weight: 600;
        color: #666;
        padding: 1rem 2rem;
        border: 1px solid rgba(0, 188, 212, 0.2);
        border-radius: 8px;
        background: rgba(0, 188, 212, 0.05);
    }
    
    /* === PRICING === */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .pricing-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 188, 212, 0.05) 100%);
        border: 2px solid rgba(0, 188, 212, 0.2);
        border-radius: 15px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .pricing-card.featured {
        border-color: rgba(0, 188, 212, 0.8);
        transform: scale(1.05);
        box-shadow: 0 20px 50px rgba(0, 188, 212, 0.3);
    }
    
    .pricing-card:hover {
        border-color: rgba(0, 188, 212, 0.6);
        box-shadow: 0 15px 40px rgba(0, 188, 212, 0.2);
    }
    
    .pricing-card h3 {
        font-size: 1.8rem;
        margin-bottom: 1rem;
        color: #00bcd4;
    }
    
    .price {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00bcd4;
        margin-bottom: 1.5rem;
    }
    
    .price-period {
        color: #888;
        font-size: 0.9rem;
    }
    
    .pricing-features {
        list-style: none;
        margin: 2rem 0;
        text-align: left;
    }
    
    .pricing-features li {
        padding: 0.8rem 0;
        color: #a0a0a0;
        border-bottom: 1px solid rgba(0, 188, 212, 0.1);
    }
    
    .pricing-features li:last-child {
        border-bottom: none;
    }
    
    .pricing-button {
        width: 100%;
        padding: 1rem;
        margin-top: 1.5rem;
        background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .pricing-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 188, 212, 0.3);
    }
    
    /* === TESTIMONIALS === */
    .testimonial-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 188, 212, 0.05) 100%);
        border-left: 5px solid #00bcd4;
        border-radius: 10px;
        padding: 2rem;
        margin: 2rem 0;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .testimonial-text {
        font-size: 1.1rem;
        color: #c0c0c0;
        margin-bottom: 1rem;
        font-style: italic;
    }
    
    .testimonial-author {
        color: #00bcd4;
        font-weight: 700;
    }
    
    /* === CTA SECTION === */
    .cta-section {
        background: linear-gradient(135deg, rgba(0, 188, 212, 0.1) 0%, rgba(255, 64, 129, 0.1) 100%);
        border: 2px solid rgba(0, 188, 212, 0.3);
        border-radius: 20px;
        padding: 4rem 2rem;
        text-align: center;
        margin: 4rem 0;
    }
    
    .cta-title {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #00bcd4;
    }
    
    .cta-subtitle {
        font-size: 1.2rem;
        color: #a0a0a0;
        margin-bottom: 2rem;
    }
    
    /* === FOOTER === */
    .footer {
        text-align: center;
        padding: 3rem 2rem;
        border-top: 1px solid rgba(0, 188, 212, 0.2);
        color: #666;
        margin-top: 4rem;
    }
    
    /* === RESPONSIVIDADE === */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
        
        .pricing-card.featured {
            transform: scale(1);
        }
    }
</style>
''', unsafe_allow_html=True)

# --- SEÇÃO HERO ---
st.markdown('''
<div class="hero-section">
    <div class="hero-text">
        <h1 class="hero-title">Nexus AI: Transforme Seus Dados em Lucro</h1>
        <p class="hero-subtitle">
            Plataforma de IA que automatiza análises, prevê tendências e gera insights acionáveis. 
            Aumente seu faturamento em até 300% com decisões baseadas em dados inteligentes.
        </p>
        <a href="#cta" class="hero-button">Comece seu Teste Grátis</a>
        <p class="hero-subtext">✓ Sem cartão de crédito | ✓ Acesso completo por 14 dias | ✓ Cancele quando quiser</p>
    </div>
</div>
''', unsafe_allow_html=True)

# --- SEÇÃO FEATURES ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Funcionalidades que Vendem</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">🔮</div>
        <h3>Análise Preditiva</h3>
        <p>Modelos de machine learning que antecipam tendências do mercado com 95% de precisão. Saiba o que vai acontecer antes de seus concorrentes.</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">⚙️</div>
        <h3>Automação Inteligente</h3>
        <p>Automatize 80% das suas tarefas repetitivas. Libere seu time para focar em estratégia enquanto a IA trabalha 24/7.</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <h3>Insights Acionáveis</h3>
        <p>Dashboards intuitivos que transformam dados complexos em decisões claras. Veja o que importa em segundos.</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO SOCIAL PROOF ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Aprovado pelas Maiores Empresas</h2>', unsafe_allow_html=True)

st.markdown('''
<div class="logos-container">
    <div class="logo-item">🏢 Tech Corp</div>
    <div class="logo-item">🏢 Finance Plus</div>
    <div class="logo-item">🏢 Retail Max</div>
    <div class="logo-item">🏢 Cloud Sys</div>
    <div class="logo-item">🏢 Data Hub</div>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div style="text-align: center; margin-top: 2rem;">
    <p style="font-size: 1.2rem; color: #00bcd4; font-weight: 700;">
        ⭐ 4.9/5 em 2.500+ avaliações
    </p>
    <p style="color: #a0a0a0;">
        "Aumentamos nosso ROI em 250% em 3 meses" - CEO da Tech Corp
    </p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO PRICING ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Escolha o Plano Perfeito</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="pricing-card">
        <h3>Starter</h3>
        <div class="price">R$ 299<span class="price-period">/mês</span></div>
        <ul class="pricing-features">
            <li>✓ Análise Preditiva Básica</li>
            <li>✓ 10.000 Requisições/mês</li>
            <li>✓ 1 Dashboard</li>
            <li>✓ Suporte por Email</li>
            <li>✗ Automação Avançada</li>
        </ul>
        <button class="pricing-button">Começar Agora</button>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="pricing-card featured">
        <h3>⭐ Pro (Mais Popular)</h3>
        <div class="price">R$ 899<span class="price-period">/mês</span></div>
        <ul class="pricing-features">
            <li>✓ Análise Preditiva Avançada</li>
            <li>✓ 100.000 Requisições/mês</li>
            <li>✓ 10 Dashboards</li>
            <li>✓ Automação Inteligente</li>
            <li>✓ Suporte Prioritário 24/7</li>
        </ul>
        <button class="pricing-button">Começar Agora</button>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="pricing-card">
        <h3>Enterprise</h3>
        <div class="price">Customizado</div>
        <ul class="pricing-features">
            <li>✓ Tudo do Pro</li>
            <li>✓ Requisições Ilimitadas</li>
            <li>✓ Dashboards Ilimitados</li>
            <li>✓ Gerente de Conta Dedicado</li>
            <li>✓ Integrações Customizadas</li>
        </ul>
        <button class="pricing-button">Falar com Vendas</button>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO TESTIMONIALS ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">O Que Nossos Clientes Dizem</h2>', unsafe_allow_html=True)

st.markdown('''
<div class="testimonial-card">
    <p class="testimonial-text">
        "A Nexus AI revolucionou nossa forma de analisar dados. Em apenas 3 meses, aumentamos nosso ROI em 250%. 
        É simplesmente incrível como a plataforma nos ajuda a tomar decisões mais rápidas e precisas."
    </p>
    <p class="testimonial-author">— João Silva, CEO da Tech Corp</p>
</div>

<div class="testimonial-card">
    <p class="testimonial-text">
        "Economizamos 40 horas por semana em tarefas manuais. O time agora foca em estratégia enquanto a IA faz o trabalho pesado. 
        Recomendo para qualquer empresa que quer crescer rápido."
    </p>
    <p class="testimonial-author">— Maria Santos, Diretora de Operações da Finance Plus</p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO CTA FINAL ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div id="cta"></div>', unsafe_allow_html=True)
st.markdown('''
<div class="cta-section">
    <h2 class="cta-title">Pronto para Faturar Milhões?</h2>
    <p class="cta-subtitle">
        Junte-se a 500+ empresas que já estão transformando seus negócios com a Nexus AI.
    </p>
</div>
''', unsafe_allow_html=True)

# Formulário de inscrição
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    email = st.text_input(
        "Seu melhor email",
        placeholder="seu.email@empresa.com",
        label_visibility="collapsed"
    )
    
    if st.button("🚀 Começar Teste Grátis", use_container_width=True):
        if email and "@" in email:
            st.success(f"✅ Ótimo! Enviamos um email de confirmação para {email}. Verifique sua caixa de entrada!")
        else:
            st.error("❌ Por favor, insira um email válido.")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('''
<div class="footer">
    <p>© 2026 Nexus AI. Todos os direitos reservados.</p>
    <p style="margin-top: 1rem; font-size: 0.9rem;">
        Feito com ❤️ por <strong>Manus AI</strong> | 
        <a href="#" style="color: #00bcd4; text-decoration: none;">Privacidade</a> | 
        <a href="#" style="color: #00bcd4; text-decoration: none;">Termos</a>
    </p>
</div>
''', unsafe_allow_html=True)
