import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="YOLU | Night Care para Cabelos",
    page_icon="🌙",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (YOLU NIGHT VIBE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300&family=Noto+Sans+JP:wght@100;300;400&display=swap');

    /* Fundo Gradiente Noturno */
    .stApp {
        background: linear-gradient(180deg, #050a14 0%, #0f1c3d 50%, #1e1b4b 100%);
        color: #ffffff;
    }

    html, body, [class*="css"] {
        font-family: 'Noto Sans JP', sans-serif;
        font-weight: 300;
    }

    h1, h2, .serif-yolu {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-weight: 300;
        letter-spacing: 2px;
    }

    /* Header Transparente */
    .nav-yolu {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px 6%;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        background: rgba(5, 10, 20, 0.4);
        backdrop-filter: blur(8px);
    }
    .logo-yolu {
        font-size: 28px;
        letter-spacing: 5px;
        font-weight: 400;
    }

    /* Hero Section - A Noite Começa */
    .hero-yolu {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600'); /* Estrelas */
        background-size: cover;
        background-position: center;
        position: relative;
    }
    
    .hero-title-main {
        font-size: clamp(40px, 8vw, 100px);
        line-height: 1;
        margin-bottom: 20px;
        text-shadow: 0 0 20px rgba(255,255,255,0.3);
    }

    /* Cards de Produto (Estilo Minimalista Japonês) */
    .product-section {
        padding: 100px 6%;
    }

    .product-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0px;
        padding: 40px;
        text-align: center;
        transition: 0.5s;
    }
    .product-card:hover {
        background: rgba(255, 255, 255, 0.07);
        border-color: rgba(212, 175, 55, 0.5); /* Toque de ouro */
    }

    .btn-yolu {
        display: inline-block;
        padding: 12px 40px;
        border: 1px solid #fff;
        color: #fff;
        text-decoration: none;
        font-size: 12px;
        letter-spacing: 2px;
        margin-top: 20px;
        transition: 0.3s;
    }
    .btn-yolu:hover {
        background: #fff;
        color: #050a14;
    }

    /* Elemento Flutuante (Lua/Partícula) */
    .moon-bg {
        position: absolute;
        top: 10%;
        right: 10%;
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
        border-radius: 50%;
        filter: blur(30px);
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-yolu">
    <div class="logo-yolu">YOLU</div>
    <div style="display: flex; gap: 40px; font-size: 11px; letter-spacing: 1px;">
        <span>CONCEITO</span>
        <span>PRODUTOS</span>
        <span>CONTATO</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown("""
<div class="hero-yolu">
    <div class="moon-bg"></div>
    <p style="letter-spacing: 8px; font-size: 12px; margin-bottom: 30px;">BELEZA QUE NASCE À NOITE</p>
    <h1 class="hero-title-main serif-yolu">A Night Calm<br>Experience</h1>
    <p style="max-width: 600px; font-size: 14px; opacity: 0.8; line-height: 2;">
        Reparação profunda enquanto você dorme. <br>
        Sinta a tranquilidade da noite em cada fio.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. CONCEITO (SEÇÃO COMPRIDA) ---
st.markdown("""
<div style="padding: 150px 15%; text-align: center;">
    <h2 class="serif-yolu" style="font-size: 42px; margin-bottom: 40px;">Por que Cuidados Noturnos?</h2>
    <p style="font-size: 16px; line-height: 2.2; opacity: 0.7;">
        Durante a noite, o seu cabelo está livre das agressões externas do dia. 
        É o momento perfeito para a penetração intensa de nutrientes. 
        Nossa fórmula inspirada no "sono reparador" protege as cutículas do atrito com o travesseiro, 
        garantindo um despertar radiante.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. PRODUTOS (LOJA) ---
st.markdown('<div class="product-section">', unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="product-card">
        <img src="https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600" style="width:100%; margin-bottom:30px; opacity:0.9;">
        <h3 class="serif-yolu" style="font-size: 28px;">Calm Night Repair</h3>
        <p style="font-size: 12px; color: #aaa; margin: 20px 0;">SHAMPOO & TRATAMENTO</p>
        <p style="font-size: 14px; line-height: 1.8;">Para cabelos secos e indisciplinados. Foco em hidratação profunda.</p>
        <a href="#" class="btn-yolu">SAIBA MAIS</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="product-card">
        <img src="https://images.unsplash.com/photo-1556229167-73191319a992?w=600" style="width:100%; margin-bottom:30px; opacity:0.9;">
        <h3 class="serif-yolu" style="font-size: 28px;">Relax Night Repair</h3>
        <p style="font-size: 12px; color: #aaa; margin: 20px 0;">CUIDADO INTENSIVO</p>
        <p style="font-size: 14px; line-height: 1.8;">Para cabelos danificados por processos químicos. Foco em reconstrução.</p>
        <a href="#" class="btn-yolu">SAIBA MAIS</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div style="padding: 100px 6% 40px 6%; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 100px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
        <div>
            <h2 class="logo-yolu" style="margin-bottom: 20px;">YOLU</h2>
            <p style="font-size: 11px; opacity: 0.5;">© 2026 YOLU | I-ne Co., Ltd. <br> Todos os direitos reservados.</p>
        </div>
        <div style="text-align: right; font-size: 11px; letter-spacing: 2px;">
            INSTAGRAM / TWITTER / REVIEWS
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
