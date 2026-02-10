import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Moooi | A Life Extraordinary",
    page_icon="✨",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (MOOOI LUXURY STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Inter:wght@200;300;400&display=swap');

    /* Reset Geral */
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Moooi */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: 0.5px;
    }

    h1, h2, h3, .serif-moooi {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    /* Navigation Bar */
    .nav-moooi {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px 50px;
        background: white;
        border-bottom: 1px solid #f2f2f2;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .logo-moooi {
        font-family: 'Cormorant Garamond', serif;
        font-size: 32px;
        font-weight: 500;
        letter-spacing: 8px;
        text-transform: uppercase;
    }

    /* Hero Section Imersivo */
    .hero-moooi {
        position: relative;
        height: 90vh;
        background-image: url('https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
    }
    
    .hero-overlay {
        background: rgba(0,0,0,0.1);
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    /* Botões Estilo Ghost */
    div.stButton > button {
        background-color: transparent;
        color: #000;
        border: 1px solid #000;
        border-radius: 0px;
        padding: 12px 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        background-color: #000;
        color: #fff;
        border: 1px solid #000;
    }

    /* Seções de Grade de Produto */
    .product-grid-section {
        padding: 100px 50px;
    }

    .product-card {
        text-align: center;
        margin-bottom: 50px;
    }
    .product-img {
        width: 100%;
        height: 500px;
        object-fit: cover;
        margin-bottom: 20px;
        transition: transform 0.6s ease;
    }
    .product-img:hover {
        transform: scale(1.02);
    }

    /* Footer Elegante */
    .footer-moooi {
        background-color: #fafafa;
        padding: 100px 50px;
        border-top: 1px solid #eee;
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="nav-moooi">
    <div style="display: flex; gap: 30px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">
        <span>Coleção</span>
        <span>Estilo de Vida</span>
        <span>Histórias</span>
    </div>
    <div class="logo-moooi">Moooi</div>
    <div style="display: flex; gap: 30px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">
        <span>Lojas</span>
        <span>Pesquisar</span>
        <span>Login</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-moooi">
    <div class="hero-overlay">
        <h2 style="font-size: 14px; letter-spacing: 5px; margin-bottom: 20px;">LANÇAMENTO DE COLEÇÃO</h2>
        <h1 class="serif-moooi" style="font-size: 60px; color: white;">A Life Extraordinary</h1>
        <div style="margin-top: 30px;">
             <a href="#" style="color: white; text-decoration: underline; font-size: 12px; letter-spacing: 2px;">DESCUBRA O NOVO</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. INTRODUÇÃO ---
st.markdown("""
<div style="padding: 120px 20%; text-align: center;">
    <h2 class="serif-moooi" style="font-size: 32px; margin-bottom: 30px;">Inspirando o Mundo desde 2001</h2>
    <p style="font-size: 16px; line-height: 1.8; color: #555;">
        A Moooi sempre foi sinônimo de um estilo de vida que é ao mesmo tempo lúdico e refinado. 
        Nossas criações desafiam a gravidade, a luz e a imaginação, transformando espaços cotidianos 
        em experiências extraordinárias.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. GRID DE PRODUTOS (LAYOUT ASSIMÉTRICO) ---
st.markdown('<div class="product-grid-section">', unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="product-card">
        <img src="https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800" class="product-img">
        <h3 class="serif-moooi" style="font-size: 20px;">Luminária Knotted</h3>
        <p style="font-size: 12px; color: #888; margin-top: 10px;">DESIGN POR MARCEL WANDERS</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Ver Detalhes", key="btn1")

with col2:
    st.markdown("""
    <div class="product-card" style="margin-top: 80px;">
        <img src="https://images.unsplash.com/photo-1567016432779-094069958ea5?w=800" class="product-img">
        <h3 class="serif-moooi" style="font-size: 20px;">Sofá Cloud</h3>
        <p style="font-size: 12px; color: #888; margin-top: 10px;">SENTANDO NAS NUVENS</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Ver Detalhes", key="btn2")

st.markdown('</div>', unsafe_allow_html=True)

# --- 5. SEÇÃO DE BANNER LARGO ---
st.markdown("""
<div style="width: 100%; height: 600px; background-image: url('https://images.unsplash.com/photo-1534349762230-e0cadf78f5db?w=1600'); background-size: cover; background-position: center;">
</div>
<div style="padding: 80px 50px; text-align: left; background-color: #000; color: #fff;">
    <h2 class="serif-moooi" style="font-size: 40px; color: #fff;">Paredes que Contam Histórias</h2>
    <p style="max-width: 600px; margin-top: 20px; font-weight: 200;">Explore nossa coleção exclusiva de papéis de parede inspirados em animais extintos e mundos fantásticos.</p>
</div>
""", unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div class="footer-moooi">
    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 50px;">
        <div>
            <h3 class="serif-moooi" style="font-size: 24px; margin-bottom: 20px;">Moooi</h3>
            <p style="font-size: 12px; line-height: 2;">A Life Extraordinary.<br>Subscreva para receber inspiração semanal.</p>
        </div>
        <div>
            <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase;">Produtos</h4>
            <p style="font-size: 12px; line-height: 2; margin-top: 20px;">Iluminação<br>Móveis<br>Acessórios<br>Tapetes</p>
        </div>
        <div>
            <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase;">Serviços</h4>
            <p style="font-size: 12px; line-height: 2; margin-top: 20px;">Localizador de Lojas<br>Atendimento<br>Downloads 3D</p>
        </div>
        <div>
            <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase;">Social</h4>
            <p style="font-size: 12px; line-height: 2; margin-top: 20px;">Instagram<br>Pinterest<br>LinkedIn</p>
        </div>
    </div>
    <div style="margin-top: 100px; padding-top: 20px; border-top: 1px solid #eee; font-size: 10px; color: #aaa; text-align: center;">
        © 2026 MOOOI B.V. TODOS OS DIREITOS RESERVADOS.
    </div>
</div>
""", unsafe_allow_html=True)
