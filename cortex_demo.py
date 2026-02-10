import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Rogue & Rosy | Floral & Design",
    page_icon="🌹",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (ROGUE & ROSY STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Great+Vibes&family=Inter:wght@300;400&display=swap');

    /* Cores de Base */
    :root {
        --rogue-green: #1b2621;
        --rosy-cream: #f9f5f0;
        --rogue-accent: #c47d6a;
    }

    .stApp {
        background-color: var(--rosy-cream);
        color: var(--rogue-green);
    }

    /* Tipografia Especial */
    h1, h2, h3, .serif-heavy {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .script-font {
        font-family: 'Great Vibes', cursive;
        text-transform: none;
        font-size: 1.5em;
        color: var(--rogue-accent);
        letter-spacing: 0;
    }

    /* Navegação Minimalista */
    .nav-rogue {
        display: flex;
        justify-content: space-between;
        padding: 40px 6%;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    /* Hero Section */
    .hero-rogue {
        padding: 80px 6% 120px 6%;
        text-align: center;
    }
    .hero-title {
        font-size: clamp(40px, 8vw, 110px);
        line-height: 0.9;
        margin-bottom: 20px;
    }

    /* Galeria com Molduras */
    .image-frame {
        border: 1px solid var(--rogue-green);
        padding: 15px;
        background: white;
        transition: transform 0.4s ease;
    }
    .image-frame:hover {
        transform: rotate(-1deg) scale(1.02);
    }

    /* Seções de Texto Editorial */
    .editorial-section {
        padding: 100px 15%;
        text-align: center;
        background-color: var(--rogue-green);
        color: var(--rosy-cream);
    }

    /* Botão Customizado */
    div.stButton > button {
        background-color: transparent;
        color: var(--rogue-green);
        border: 1px solid var(--rogue-green);
        border-radius: 0;
        padding: 15px 45px;
        font-family: 'Cormorant Garamond', serif;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: var(--rogue-green);
        color: var(--rosy-cream);
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-rogue">
    <div>Rogue & Rosy — 2026</div>
    <div style="display: flex; gap: 40px;">
        <span>Flores</span>
        <span>Estúdio</span>
        <span>Journal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown(f"""
<div class="hero-rogue">
    <span class="script-font">Bem-vindo à rebeldia</span>
    <h1 class="hero-title">BELLEZA EM<br>DECOMPOSIÇÃO</h1>
    <p style="max-width: 600px; margin: 30px auto; font-size: 16px; line-height: 1.8;">
        Criamos arranjos florais e experiências visuais que celebram o ciclo completo da vida: 
        do desabrochar selvagem à melancolia elegante da murchidão.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. SHOWCASE (LAYOUT EDITORIAL) ---
c1, c2, c3 = st.columns([1, 1.2, 1])

with c1:
    st.markdown('<div style="margin-top: 100px;">', unsafe_allow_html=True)
    st.markdown("""
    <div class="image-frame">
        <img src="https://images.unsplash.com/photo-1526047932273-341f2a7631f9?w=500" style="width:100%;">
        <p style="margin-top:15px; font-size:10px; text-align:center; letter-spacing:2px;">O JARDIM SECRETO</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="image-frame">
        <img src="https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=600" style="width:100%;">
        <p style="margin-top:15px; font-size:10px; text-align:center; letter-spacing:2px;">ALQUIMIA BOTÂNICA</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown('<div style="margin-top: 50px;">', unsafe_allow_html=True)
    st.markdown("""
    <div class="image-frame">
        <img src="https://images.unsplash.com/photo-1550983058-ba68da98383a?w=500" style="width:100%;">
        <p style="margin-top:15px; font-size:10px; text-align:center; letter-spacing:2px;">ROSAS SELVAGENS</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MANIFESTO (SEÇÃO ESCURA) ---
st.write("")
st.write("")
st.markdown("""
<div class="editorial-section">
    <h2 style="font-size: 40px; margin-bottom: 30px;">Poesia na Imperfeição</h2>
    <p style="font-size: 18px; line-height: 2; opacity: 0.9;">
        Na Rogue & Rosy, não buscamos o arranjo perfeito de supermercado. 
        Nós buscamos o galho torto, a pétala caída, o contraste entre a espinha e a seda. 
        Nossa estética é um tributo às almas livres e aos corações românticos.
    </p>
    <div style="margin-top: 50px;">
        <span class="script-font" style="font-size: 3em; color: white;">Assinado, Rogue</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div style="padding: 100px 6% 40px 6%; text-align: center;">
    <h3 style="margin-bottom: 40px;">Deseja algo extraordinário?</h3>
</div>
""", unsafe_allow_html=True)

col_f, _ = st.columns([1, 1])
with col_f:
    st.button("ENCOMENDAR UM ARRANJO")

st.markdown("""
<div style="margin-top: 100px; padding-top: 40px; border-top: 1px solid rgba(27, 38, 33, 0.1); display: flex; justify-content: space-between; font-size: 11px; letter-spacing: 2px;">
    <div>© 2026 ROGUE & ROSY</div>
    <div>INSTAGRAM / PINTEREST / CONTATO</div>
</div>
""", unsafe_allow_html=True)
