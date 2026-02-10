# -*- coding: utf-8 -*-
"""
Landing Page de Alta Conversão para Geração de Leads

Autor: Manus AI
Data: 10 de Fevereiro de 2026

Estrutura completa com 12 seções focadas em conversão, design profissional,
cores vibrantes e layouts modernos para maximizar a geração de leads.
"""

import streamlit as st

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(
    page_title="Solução X | Transforme seu Negócio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS E ESTILOS GLOBAIS ---
css_styles = """
<style>
    /* === VARIÁVEIS DE COR E FONTE === */
    :root {
        --primary: #0052FF; /* Azul vibrante */
        --secondary: #FF005C; /* Rosa/Magenta vibrante */
        --accent: #FFD600; /* Amarelo para destaque */
        --dark: #0D0221; /* Roxo/Azul bem escuro */
        --light: #F0F2F6;
        --text-dark: #FFFFFF;
        --text-muted: #A9B4D9;
        --font-family: 'Inter', sans-serif;
    }

    /* === RESET E ESTILOS BASE === */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    body { background-color: var(--dark) !important; color: var(--text-light); font-family: var(--font-family); }
    .main { background: transparent !important; }
    h1, h2, h3 { font-weight: 700; color: var(--text-dark); }
    p { color: var(--text-muted); line-height: 1.7; }
    .section-container { padding: 5rem 2rem; max-width: 1100px; margin: auto; text-align: center; }

    /* === HEADER === */
    .header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 1rem 2rem; position: fixed; top: 0; left: 0; right: 0; z-index: 100;
        background: rgba(13, 2, 33, 0.8); backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .logo { font-size: 1.5rem; font-weight: 900; color: var(--text-dark); }

    /* === BOTÕES (CTA) === */
    .cta-button {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white; padding: 12px 28px; border-radius: 50px; text-decoration: none;
        font-weight: 600; transition: all 0.3s ease; display: inline-block;
        border: none; box-shadow: 0 5px 20px rgba(0, 82, 255, 0.4);
    }
    .cta-button:hover { transform: translateY(-3px); box-shadow: 0 8px 30px rgba(255, 0, 92, 0.5); }

    /* === HERO SECTION === */
    .hero { padding-top: 10rem; }
    .hero h1 { font-size: 3.8rem; font-weight: 900; margin-bottom: 1rem; line-height: 1.2; }
    .hero .subheadline { font-size: 1.2rem; max-width: 600px; margin: 0 auto 2rem auto; }

    /* === SEÇÃO PROBLEMA/SOLUÇÃO === */
    .problem-solution { background: rgba(255,255,255,0.05); border-radius: 20px; }

    /* === BENEFÍCIOS (CARDS) === */
    .benefits-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; text-align: left; }
    .benefit-card {
        background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s ease;
    }
    .benefit-card:hover { transform: translateY(-10px); border-color: var(--primary); }
    .benefit-card .icon { font-size: 2.5rem; color: var(--accent); }

    /* === COMO FUNCIONA (PASSOS) === */
    .how-it-works-steps { display: flex; justify-content: space-between; gap: 2rem; margin-top: 3rem; }
    .step { flex: 1; }
    .step .number { font-size: 2rem; font-weight: 900; color: var(--primary); }

    /* === PROVA SOCIAL === */
    .social-proof { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; border-radius: 20px; }
    .social-proof h2, .social-proof p { color: white; }

    /* === FAQ === */
    .st-emotion-cache-1h9usn1 { border-color: rgba(255,255,255,0.2); }

    /* === FOOTER === */
    .footer { border-top: 1px solid rgba(255,255,255,0.1); padding: 2rem; }

</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="header">
    <div class="logo">Solução X</div>
    <a href="#cta-final" class="cta-button">Começar Agora</a>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="section-container hero">
    <h1>Transforme sua Operação com Inteligência Artificial</h1>
    <p class="subheadline">Automatize 90% das suas tarefas manuais, reduza custos e acelere seu crescimento com a nossa plataforma de IA.</p>
    <a href="#cta-final" class="cta-button" style="padding: 18px 40px; font-size: 1.2rem;">Receber uma Demonstração Gratuita</a>
</div>
""", unsafe_allow_html=True)

# --- 3. PROBLEMA ---
st.markdown("""
<div class="section-container problem-solution">
    <h2>Você perde horas com tarefas repetitivas?</h2>
    <p>Processos manuais são lentos, caros e propensos a erros. Sua equipe gasta mais tempo em planilhas e e-mails do que em atividades que realmente geram valor, travando o crescimento do seu negócio.</p>
</div>
""", unsafe_allow_html=True)

# --- 4. SOLUÇÃO ---
st.markdown("""
<div class="section-container">
    <h2>A Solução X Automatiza Tudo para Você</h2>
    <p>Nossa plataforma utiliza IA para entender seus processos, automatizar tarefas e liberar sua equipe para focar no que importa: estratégia e inovação. Diga adeus ao trabalho manual e olá para a eficiência máxima.</p>
</div>
""", unsafe_allow_html=True)

# --- 5. BENEFÍCIOS ---
st.markdown("""
<div class="section-container">
    <h2>Resultados que Você Pode Esperar</h2>
    <div class="benefits-grid">
        <div class="benefit-card">
            <div class="icon">⏱️</div>
            <h3>Economia de Tempo</h3>
            <p>Reduza o tempo gasto em tarefas manuais em até 90% e acelere seus ciclos de trabalho.</p>
        </div>
        <div class="benefit-card">
            <div class="icon">💰</div>
            <h3>Redução de Custos</h3>
            <p>Diminua os custos operacionais eliminando a necessidade de trabalho repetitivo e propenso a erros.</p>
        </div>
        <div class="benefit-card">
            <div class="icon">📈</div>
            <h3>Aumento de Produtividade</h3>
            <p>Capacite sua equipe para focar em inovação e estratégia, gerando mais resultados com menos esforço.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. DIFERENCIAIS ---
st.markdown("""
<div class="section-container problem-solution">
    <h2>Por que a Solução X é Diferente?</h2>
    <p>Ao contrário de outras ferramentas, nossa IA é treinada especificamente para o seu setor. Isso significa uma implementação 10x mais rápida e resultados mais precisos desde o primeiro dia. Não é uma solução genérica, é a sua solução.</p>
</div>
""", unsafe_allow_html=True)

# --- 7. COMO FUNCIONA ---
st.markdown("""
<div class="section-container">
    <h2>Comece em 3 Passos Simples</h2>
    <div class="how-it-works-steps">
        <div class="step">
            <div class="number">1</div>
            <h3>Conecte suas Ferramentas</h3>
            <p>Integre com seus sistemas atuais em poucos cliques.</p>
        </div>
        <div class="step">
            <div class="number">2</div>
            <h3>Configure seus Processos</h3>
            <p>Nossa IA aprende suas tarefas observando sua equipe.</p>
        </div>
        <div class="step">
            <div class="number">3</div>
            <h3>Ative a Automação</h3>
            <p>Relaxe e veja a mágica acontecer em tempo real.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 8. PROVA SOCIAL ---
st.markdown("""
<div class="section-container social-proof">
    <h2>Junte-se a mais de 5.000 Empresas de Sucesso</h2>
    <p style="font-size: 1.5rem; font-weight: 600;">"A Solução X mudou o jogo para nós. Reduzimos nossos custos operacionais em 40% em apenas 3 meses."</p>
    <p>- CEO da Empresa Y</p>
</div>
""", unsafe_allow_html=True)

# --- 9. GARANTIA ---
st.markdown("""
<div class="section-container">
    <h2>Nosso Compromisso com seu Sucesso</h2>
    <p>Temos tanta confiança em nossa solução que oferecemos uma garantia de satisfação. Se você não economizar pelo menos 20 horas de trabalho no primeiro mês, nós te damos seu dinheiro de volta. Sem perguntas.</p>
</div>
""", unsafe_allow_html=True)

# --- 10. CTA FINAL ---
st.markdown('<div id="cta-final"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown("""
    <div class="section-container problem-solution">
        <h2>Pronto para Acelerar seu Crescimento?</h2>
        <p>Agende uma demonstração gratuita e personalizada com um de nossos especialistas e veja como a Solução X pode transformar seu negócio.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Seu nome")
    with col2:
        st.text_input("Seu e-mail corporativo")
    
    st.button("Agendar Minha Demo Agora", use_container_width=True, type="primary")

# --- 11. FAQ ---
st.markdown("""
<div class="section-container">
    <h2>Perguntas Frequentes</h2>
</div>
""", unsafe_allow_html=True)

with st.expander("A implementação é complicada?"):
    st.write("Não! Nossa equipe de especialistas cuida de todo o processo de implementação para você. A maioria dos nossos clientes está com tudo funcionando em menos de 7 dias.")
with st.expander("Meus dados estão seguros?"):
    st.write("Sim. Usamos criptografia de ponta-a-ponta e seguimos os mais altos padrões de segurança do mercado, incluindo certificações ISO 27001 e conformidade com GDPR.")
with st.expander("A Solução X integra com meu software atual?"):
    st.write("Provavelmente sim. Temos integrações nativas com mais de 200 ferramentas populares, como Salesforce, Slack, Google Workspace e muito mais. Para casos específicos, nossa API flexível permite qualquer conexão.")

# --- 12. FOOTER ---
st.markdown("""
<div class="section-container footer">
    <p>© 2026 Solução X. Todos os direitos reservados. Feito com ❤️ por Manus AI.</p>
</div>
""", unsafe_allow_html=True)
