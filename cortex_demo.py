import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Andy Raskin | Strategic Narrative",
    page_icon="✍️",
    layout="centered" # O site dele é focado no centro para leitura
)

# --- CSS PARA ESTILO MINIMALISTA (ANDY RASKIN) ---
st.markdown("""
<style>
    /* Importando fontes serifadas para o ar de autoridade/escrita */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1a1a1a;
        line-height: 1.8;
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        font-weight: 900 !important;
        letter-spacing: -1px;
    }

    /* Hero Section */
    .hero-text {
        font-size: 64px;
        line-height: 1.1;
        margin-top: 100px;
        margin-bottom: 40px;
    }

    /* Citações / Testemunhos */
    .testimonial-box {
        font-family: 'Lora', serif;
        font-size: 22px;
        font-style: italic;
        border-left: 3px solid #000;
        padding-left: 30px;
        margin: 60px 0;
        color: #444;
    }

    /* Grid de Logos */
    .logo-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 50px;
        align-items: center;
        opacity: 0.6;
        filter: grayscale(100%);
        margin: 50px 0;
    }

    /* Seções de Texto Compridas */
    .content-block {
        margin-bottom: 100px;
    }
    
    .section-label {
        text-transform: uppercase;
        font-weight: 700;
        font-size: 12px;
        letter-spacing: 2px;
        color: #888;
        margin-bottom: 20px;
    }

    /* Botão Minimalista */
    div.stButton > button {
        background-color: #000;
        color: #fff;
        border-radius: 0;
        padding: 15px 40px;
        font-weight: 700;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #333;
        color: #fff;
    }
    
    /* Footer */
    .footer-andy {
        padding: 100px 0 50px 0;
        border-top: 1px solid #eee;
        font-size: 14px;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER SIMPLES ---
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0;">
    <div style="font-weight: 800; font-size: 20px; letter-spacing: -1px;">ANDY RASKIN</div>
    <div style="font-size: 14px; font-weight: 600; gap: 20px; display: flex;">
        <span>NARRATIVE</span>
        <span>ARTICLES</span>
        <span>ABOUT</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown('<h1 class="hero-text">Ajudo CEOs a liderar através da narrativa estratégica.</h1>', unsafe_allow_html=True)

st.markdown("""
<p style="font-size: 24px; color: #555; font-family: 'Lora', serif;">
    Quando a sua equipe, seus investidores e seus clientes não conseguem explicar o que você faz, o problema não é o seu produto. É a sua história.
</p>
""", unsafe_allow_html=True)

st.write("")
st.button("TRABALHE COMIGO")

# --- 3. PROVA SOCIAL (LOGOS) ---
st.markdown('<div style="margin-top: 100px;" class="section-label">LIDERANÇAS QUE CONFIAM</div>', unsafe_allow_html=True)
st.markdown("""
<div class="logo-grid">
    <span style="font-size: 24px; font-weight: 800;">Salesforce</span>
    <span style="font-size: 24px; font-weight: 800;">Uber</span>
    <span style="font-size: 24px; font-weight: 800;">IBM</span>
    <span style="font-size: 24px; font-weight: 800;">Square</span>
    <span style="font-size: 24px; font-weight: 800;">Intel</span>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- 4. SEÇÃO COMPRIDA: O MANIFESTO ---
st.markdown('<div class="content-block">', unsafe_allow_html=True)
st.markdown('<div class="section-label">A ABORDAGEM</div>', unsafe_allow_html=True)
st.markdown("## O maior deck de vendas que eu já vi.")
st.write("""
A maioria das empresas foca em "por que somos melhores". Mas o cérebro humano não é programado para se importar com comparações de funcionalidades. 

O que os CEOs de sucesso fazem é criar um **"Antigo Jogo vs. Novo Jogo"**. Eles mostram que o mundo mudou de uma forma que torna a antiga maneira de fazer as coisas obsoleta. 
Minha missão é ajudar você a definir essa mudança.
""")

st.markdown("""
<div class="testimonial-box">
    "Andy nos ajudou a encontrar a narrativa que unificou toda a nossa empresa. Não foi apenas marketing, foi estratégia de liderança."
    <br><br>
    <span style="font-style: normal; font-size: 16px; font-weight: 700; color: #000;">— CEO, Unicórnio de Tecnologia</span>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. SEÇÃO COMPRIDA: SERVIÇOS ---
st.markdown('<div class="content-block">', unsafe_allow_html=True)
st.markdown('<div class="section-label">SERVIÇOS</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Mentoria de Narrativa")
    st.write("Sessões individuais com fundadores e CEOs para alinhar a história da categoria.")
with col2:
    st.markdown("### Workshops de Liderança")
    st.write("Alinhamento para equipes de liderança para garantir que todos falem a mesma língua.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. SEÇÃO COMPRIDA: ARTIGOS (ESTILO BLOG) ---
st.markdown('<div class="content-block">', unsafe_allow_html=True)
st.markdown('<div class="section-label">LEITURA RECOMENDADA</div>', unsafe_allow_html=True)

def article_item(title, summary):
    st.markdown(f"#### {title}")
    st.write(summary)
    st.markdown('<p style="font-size: 12px; font-weight: 700; color: #000; text-decoration: underline; cursor: pointer;">LER ARTIGO</p>', unsafe_allow_html=True)
    st.write("")

article_item("A Mudança Inegável", "Por que você deve focar na mudança do mundo, não nos seus benefícios.")
article_item("O Fim da Proposta de Valor", "Por que o conceito tradicional de UVP está matando sua diferenciação.")
article_item("Liderando com História", "Como os melhores CEOs usam a narrativa para recrutar talentos nível A.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("""
<div class="footer-andy">
    <div style="display: flex; justify-content: space-between;">
        <div>
            <b>Andy Raskin</b><br>
            San Francisco, CA
        </div>
        <div style="text-align: right;">
            LinkedIn / Twitter / Medium <br>
            © 2024 Todos os direitos reservados.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
