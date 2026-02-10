import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Nubank - Finalmente você no controle",
    page_icon="💜",
    layout="wide"
)

# --- CSS PARA ESTILO NUBANK ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #111;
    }

    /* Barra de Navegação */
    .nav-nu {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 8%;
        background: white;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .logo-nu {
        font-weight: 700;
        font-size: 26px;
        color: #820ad1; /* Roxo Nubank */
    }

    /* Hero Section */
    .hero-nu {
        padding: 80px 8%;
        background-color: #820ad1;
        color: white;
        display: flex;
        align-items: center;
        margin-bottom: 50px;
        min-height: 500px;
    }
    .hero-title {
        font-size: 56px;
        font-weight: 700;
        line-height: 1.1;
    }

    /* Botões Pill-Shaped */
    div.stButton > button {
        border-radius: 50px;
        padding: 15px 35px;
        background-color: #820ad1;
        color: white;
        border: none;
        font-weight: 600;
        font-size: 16px;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background-color: #9b37e0;
        color: white;
    }

    /* Seção Branca de Produtos */
    .section-white {
        padding: 80px 8%;
        background-color: white;
    }
    
    .card-nu {
        background-color: #f5f5f5;
        border-radius: 16px;
        padding: 30px;
        height: 100%;
        transition: 0.3s;
        border: 1px solid transparent;
    }
    .card-nu:hover {
        border-color: #820ad1;
    }

    /* Footer Nubank Style */
    .footer-nu {
        background-color: #111;
        color: #fff;
        padding: 80px 8% 40px 8%;
        margin-top: 50px;
    }
    .footer-links {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
    }
    .footer-links h4 { color: #820ad1; margin-bottom: 20px; }
    .footer-links p { font-size: 14px; color: #999; }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="nav-nu">
    <div class="logo-nu">nubank</div>
    <div style="display: flex; gap: 30px; font-weight: 600; font-size: 14px;">
        <span>Página Inicial</span>
        <span>Para você</span>
        <span>Para seu negócio</span>
        <span>O Nu</span>
    </div>
    <div style="color: #820ad1; font-weight: 600; cursor: pointer;">Login</div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
with st.container():
    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.markdown("""
        <div style="padding: 100px 0 0 100px;">
            <h1 style="font-size: 52px; font-weight: 700; color: #820ad1;">Finalmente você no controle do seu dinheiro.</h1>
            <p style="font-size: 20px; margin: 30px 0; color: #444;">O futuro é roxo. Uma conta digital completa, sem tarifas e um cartão de crédito que você manda.</p>
        </div>
        """, unsafe_allow_html=True)
        # Input simulado de CPF que o Nu usa no Hero
        st.text_input("Digite seu CPF", placeholder="000.000.000-00")
        st.button("Continuar")
    with c2:
        st.image("https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800", use_container_width=True)

# --- 3. SEÇÃO DE PRODUTOS (CARDS) ---
st.markdown("<div class='section-white'>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size: 32px; margin-bottom: 40px;'>Um mundo de possibilidades</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

def nu_card(col, icon, title, text):
    with col:
        st.markdown(f"""
        <div class="card-nu">
            <div style="font-size: 30px; margin-bottom: 15px;">{icon}</div>
            <h3 style="font-size: 20px;">{title}</h3>
            <p style="color: #666; font-size: 15px;">{text}</p>
        </div>
        """, unsafe_allow_html=True)

nu_card(col1, "💳", "Cartão de Crédito", "O roxinho que você conhece, sem anuidade e com cashback.")
nu_card(col2, "💰", "Conta Digital", "Seu dinheiro rende mais que a poupança e você tem liquidez diária.")
nu_card(col3, "📉", "Investimentos", "Invista em bolsa, fundos e CDBs a partir de R$ 1.")

st.markdown("</div>", unsafe_allow_html=True)

# --- 4. SEÇÃO "O NU" (COMPRIDA) ---
st.write("---")
with st.container():
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://images.unsplash.com/photo-1556742044-3c52d6e88c62?w=600")
    with col_txt:
        st.markdown("""
        <div style="padding: 50px;">
            <h2 style="color: #820ad1;">Nu México e Colômbia</h2>
            <p>O Nubank já é o maior banco digital do mundo fora da Ásia. Estamos revolucionando a vida financeira de milhões de pessoas na América Latina.</p>
            <a href="#" style="color: #820ad1; font-weight: 600;">Conheça nossa expansão →</a>
        </div>
        """, unsafe_allow_html=True)

# --- 5. SEÇÃO NEWSLETTER / CTA ---
st.markdown("""
<div style="background-color: #f5f5f5; padding: 100px 8%; text-align: center;">
    <h2 style="font-size: 40px; font-weight: 700;">Pronto para ser Nu?</h2>
    <p style="margin-bottom: 40px;">Abra sua conta agora e experimente a liberdade.</p>
</div>
""", unsafe_allow_html=True)
st.button("QUERO SER NUBANK", key="cta_bottom")

# --- 6. FOOTER ---
st.markdown("""
<div class="footer-nu">
    <div class="footer-links">
        <div>
            <h4>Nubank</h4>
            <p>Sobre nós</p>
            <p>Carreiras</p>
            <p>Perguntas frequentes</p>
        </div>
        <div>
            <h4>Produtos</h4>
            <p>Conta digital</p>
            <p>Cartão de crédito</p>
            <p>Seguros</p>
        </div>
        <div>
            <h4>Fale com a gente</h4>
            <p>0800 608 6236</p>
            <p>meajuda@nubank.com.br</p>
            <p>Atendimento 24h</p>
        </div>
        <div>
            <h4>Baixe o app</h4>
            <p>App Store</p>
            <p>Google Play</p>
        </div>
    </div>
    <div style="text-align: center; margin-top: 60px; border-top: 1px solid #333; padding-top: 20px; font-size: 12px; color: #555;">
        Nu Pagamentos S.A. - Instituição de Pagamento. CNPJ 18.236.120/0001-58 <br>
        Rua Capote Valente, 39 - São Paulo, SP - 05409-000
    </div>
</div>
""", unsafe_allow_html=True)
