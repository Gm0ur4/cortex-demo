import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Lemonade Giveback | Seguro com Propósito",
    page_icon="🍋",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (LEMONADE BRANDING) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');

    /* Variáveis de Cor */
    :root {
        --lemonade-pink: #ff0083;
        --lemonade-black: #222;
    }

    .stApp {
        background-color: #ffffff;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--lemonade-black);
    }

    /* Header Estilo App */
    .nav-lemonade {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 10%;
        background: white;
        position: sticky;
        top: 0;
        z-index: 1000;
        border-bottom: 1px solid #f0f0f0;
    }
    
    .logo-pink {
        color: #ff0083;
        font-weight: 800;
        font-size: 24px;
        letter-spacing: -1px;
    }

    /* Hero Section - Impacto Total */
    .hero-lemonade {
        padding: 100px 10%;
        text-align: center;
        background-color: #fff;
    }
    
    .giveback-counter {
        color: #ff0083;
        font-size: 80px;
        font-weight: 800;
        margin: 20px 0;
    }

    .hero-h1 {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.1;
        max-width: 800px;
        margin: 0 auto;
    }

    /* Botão Lemonade Clássico */
    div.stButton > button {
        background-color: #ff0083;
        color: white;
        border-radius: 50px;
        padding: 18px 45px;
        font-weight: 700;
        font-size: 16px;
        border: none;
        transition: 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    div.stButton > button:hover {
        background-color: #d6006e;
        transform: scale(1.05);
        color: white;
    }

    /* Seções de Explicação */
    .section-wrap {
        padding: 100px 10%;
    }
    
    .bg-soft-pink { background-color: #fff5f9; }

    /* Cards de Caridade */
    .charity-card {
        background: white;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        border: 1px solid #eee;
        transition: 0.3s;
    }
    .charity-card:hover {
        box-shadow: 0 15px 30px rgba(255, 0, 131, 0.1);
    }

    /* Ilustrações Circulares */
    .circle-icon {
        width: 80px;
        height: 80px;
        background-color: #ff0083;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto 20px auto;
        color: white;
        font-size: 30px;
    }

    /* Footer */
    .footer-lemonade {
        padding: 80px 10%;
        background-color: #222;
        color: #fff;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="nav-lemonade">
    <div class="logo-pink">Lemonade</div>
    <div style="display: flex; gap: 30px; font-weight: 600; font-size: 14px;">
        <span>Seguros</span>
        <span>Giveback</span>
        <span>Sobre</span>
    </div>
    <div style="font-weight: 700;">Login</div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO (O GIVEBACK) ---
st.markdown('<div class="hero-lemonade">', unsafe_allow_html=True)
st.markdown('<p style="text-transform: uppercase; letter-spacing: 2px; font-weight: 700; color: #888;">Impacto Total do Giveback</p>', unsafe_allow_html=True)
st.markdown('<div class="giveback-counter">$8,231,044</div>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-h1">Transformamos o lucro não utilizado em doações.</h1>', unsafe_allow_html=True)
st.write("")
st.button("Verifique nossos preços")
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. COMO FUNCIONA (ILUSTRAÇÕES) ---
st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; font-size:36px; margin-bottom:60px;'>Como o Giveback funciona</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="circle-icon">1</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Você escolhe</h3>", unsafe_allow_html=True)
    st.write("Ao contratar o seguro, você escolhe uma causa em que acredita — como meio ambiente ou direitos humanos.")

with col2:
    st.markdown('<div class="circle-icon">2</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Nós cuidamos</h3>", unsafe_allow_html=True)
    st.write("Usamos seu prêmio para pagar sinistros. Somos uma seguradora B-Corp, focada em transparência.")

with col3:
    st.markdown('<div class="circle-icon">3</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>O resto é doado</h3>", unsafe_allow_html=True)
    st.write("O dinheiro que sobra no final do ano não vira bônus para executivos. Ele vai direto para a sua causa escolhida.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SEÇÃO DE CAUSAS (ESTILO GRID) ---
st.markdown('<div class="section-wrap bg-soft-pink">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>Algumas das causas que você apoia</h2>", unsafe_allow_html=True)

c_col1, c_col2, c_col3, c_col4 = st.columns(4)

def cause_box(col, title, img_emoji):
    with col:
        st.markdown(f"""
        <div class="charity-card">
            <div style="font-size:40px; margin-bottom:15px;">{img_emoji}</div>
            <div style="font-weight:700; font-size:14px; text-transform:uppercase;">{title}</div>
        </div>
        """, unsafe_allow_html=True)

cause_box(c_col1, "American Red Cross", "🏥")
cause_box(c_col2, "Malala Fund", "🎓")
cause_box(c_col3, "Charity: Water", "💧")
cause_box(c_col4, "The Trevor Project", "🌈")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. SEÇÃO DE CONFIANÇA (COMPRIDA) ---
st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
col_text, col_img = st.columns([1, 1])
with col_text:
    st.markdown("<h2 style='font-size:40px;'>Seguro para o século 21.</h2>", unsafe_allow_html=True)
    st.write("""
    A Lemonade foi construída de forma diferente. Ao recebermos uma taxa fixa e doarmos o restante, 
    eliminamos o conflito de interesses entre a seguradora e o cliente. 
    Nós queremos pagar seus sinistros rapidamente porque não lucramos ao negá-los.
    """)
    st.write("**B-Corp Certificada. Focada no Bem Social.**")
with col_img:
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=800")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div class="footer-lemonade">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px;">
        <div>
            <div style="color:#ff0083; font-weight:800; font-size:20px; margin-bottom:20px;">Lemonade</div>
            <p style="font-size:12px; opacity:0.7;">Seguros de casa, inquilino, pet e vida. Tudo em um só app.</p>
        </div>
        <div>
            <h4 style="font-size:14px;">PRODUTOS</h4>
            <p style="font-size:12px; opacity:0.7;">Inquilinos<br>Proprietários<br>Vida<br>Pet</p>
        </div>
        <div>
            <h4 style="font-size:14px;">EMPRESA</h4>
            <p style="font-size:12px; opacity:0.7;">Sobre nós<br>Giveback<br>Carreiras</p>
        </div>
        <div>
            <h4 style="font-size:14px;">SIGA-NOS</h4>
            <p style="font-size:12px; opacity:0.7;">Instagram<br>Twitter<br>TikTok</p>
        </div>
    </div>
    <div style="text-align:center; margin-top:80px; font-size:11px; opacity:0.5; border-top:1px solid #444; padding-top:20px;">
        © 2026 Lemonade Inc. Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
