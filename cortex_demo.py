import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Icarus Medical | Órteses Personalizadas",
    page_icon="🦿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZADO (FIXO E MELHORADO) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    /* Remover margem do topo para o menu ficar colado */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    /* HEADER / MENU - Estilo Clean */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0px;
        background-color: white;
        border-bottom: 1px solid #eee;
        margin-bottom: 40px;
    }
    .logo-text {
        font-size: 26px;
        font-weight: 900;
        color: #0f2b4c; /* Azul escuro Icarus */
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .nav-links a {
        text-decoration: none;
        color: #555;
        margin-left: 25px;
        font-weight: 500;
        font-size: 14px;
        transition: color 0.3s;
    }
    .nav-links a:hover {
        color: #0056b3;
    }

    /* HERO SECTION TEXTOS */
    h1 {
        color: #1a1a1a;
        font-weight: 800 !important;
        font-size: 3.5rem !important;
        line-height: 1.2 !important;
    }
    .hero-desc {
        font-size: 18px;
        color: #555;
        margin-top: 20px;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* BOTÕES AZUIS */
    div.stButton > button {
        background-color: #0056b3;
        color: white;
        border-radius: 4px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        border: none;
        text-transform: uppercase;
        font-size: 14px;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #003d80;
    }

    /* CARDS DE PRODUTOS */
    .product-card {
        background: white;
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        height: 100%;
    }
    .product-title {
        font-weight: 700;
        font-size: 20px;
        margin-top: 15px;
        color: #222;
    }
    .product-sub {
        color: #0056b3;
        font-weight: bold;
        font-size: 12px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    /* RODAPÉ */
    .footer {
        background-color: #111;
        color: #888;
        padding: 40px;
        text-align: center;
        font-size: 13px;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER (MENU SUPERIOR) ---
st.markdown("""
<div class="nav-container">
    <div class="logo-text">ICARUS MEDICAL</div>
    <div class="nav-links">
        <a href="#">INÍCIO</a>
        <a href="#">PRODUTOS</a>
        <a href="#">PACIENTES</a>
        <a href="#">MÉDICOS</a>
        <a href="#">CONTATO</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION (CORRIGIDA) ---
col_text, col_img = st.columns([1, 1], gap="large")

with col_text:
    st.write("") # Espaço vazio para alinhar melhor verticalmente
    st.write("") 
    st.markdown("# Alivie a Dor no Joelho.")
    st.markdown("# Restaure a Mobilidade.")
    
    st.markdown("""
    <p class="hero-desc">
    Órteses de joelho impressas em 3D sob medida, projetadas para remover o peso e reduzir a dor.
    O tratamento conservador mais avançado para osteoartrite.
    </p>
    """, unsafe_allow_html=True)
    
    # Botões lado a lado
    b1, b2 = st.columns([1, 1])
    with b1:
        st.button("SOU UM CANDIDATO?")
    with b2:
        st.button("VER PRODUTOS")

with col_img:
    # URL de imagem mais estável e genérica de tecnologia/saúde
    # Se esta falhar, o 'caption' ainda explica
    img_url = "https://images.unsplash.com/photo-1519311965067-36d3e5f33d39?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"
    st.image(img_url, caption="Engenharia do Movimento.", use_container_width=True)

st.write("---")

# --- SEÇÃO DE DADOS (STATS) ---
st.markdown("<h3 style='text-align: center; color: #333;'>A Ciência do Alívio de Carga</h3>", unsafe_allow_html=True)
st.write("")

s1, s2, s3, s4 = st.columns(4)

def stat_card(number, label):
    st.markdown(f"""
    <div style="text-align: center;">
        <div style="font-size: 32px; font-weight: bold; color: #0056b3;">{number}</div>
        <div style="font-size: 13px; color: #666; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
    </div>
    """, unsafe_allow_html=True)

with s1: stat_card("18 kg", "Capacidade de Alívio")
with s2: stat_card("3D", "Impressão Personalizada")
with s3: stat_card("< 450g", "Ultra Leve")
with s4: stat_card("EUA", "Feito na América")

st.write("---")

# --- PRODUTOS ---
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Nossas Soluções Personalizadas</h2>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

def produto_html(img, titulo, sub, desc):
    st.markdown(f"""
    <div class="product-card">
        <img src="{img}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 15px;">
        <div class="product-title">{titulo}</div>
        <div class="product-sub">{sub}</div>
        <p style="color: #666; font-size: 14px;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# URLs de imagens genéricas para evitar link quebrado
img_knee1 = "https://images.unsplash.com/photo-1584515933487-98db75f56f24?auto=format&fit=crop&w=500&q=80"
img_knee2 = "https://images.unsplash.com/photo-1552674605-5d2178b85608?auto=format&fit=crop&w=500&q=80"
img_knee3 = "https://images.unsplash.com/photo-1595079676339-1534801fafde?auto=format&fit=crop&w=500&q=80"

with p1:
    produto_html(img_knee1, "Ascender", "Órtese de Alívio", "Nossa principal órtese personalizada para alívio máximo da articulação do joelho. Ideal para Osteoartrite.")
    st.button("Ver Ascender", key="btn_p1")

with p2:
    produto_html(img_knee2, "Adonis", "Suporte Leve", "Design de baixo perfil para usuários ativos que precisam de suporte medial ou lateral sem volume extra.")
    st.button("Ver Adonis", key="btn_p2")

with p3:
    produto_html(img_knee3, "Kronos", "Recuperação Pós-Op", "Controle de amplitude de movimento ajustável e proteção para pacientes em recuperação de ligamentos.")
    st.button("Ver Kronos", key="btn_p3")

st.write("")
st.write("")

# --- COMO FUNCIONA (STEPS) ---
st.markdown("""
<div style="background-color: #f8f9fa; padding: 40px; border-radius: 10px; margin-top: 20px;">
    <h3 style="text-align: center;">Como obter sua Órtese Icarus</h3>
    <br>
""", unsafe_allow_html=True)

c_step1, c_step2, c_step3 = st.columns(3)
with c_step1:
    st.info("📱 1. Escanear")
    st.write("Baixe nosso app para fazer um escaneamento 3D preciso da sua perna usando seu smartphone.")
with c_step2:
    st.info("⚙️ 2. Projetar & Imprimir")
    st.write("Nossos engenheiros projetam uma órtese sob medida que é impressa em 3D com alta precisão.")
with c_step3:
    st.info("📦 3. Entrega")
    st.write("Receba sua órtese personalizada em casa e volte às atividades que você ama, sem dor.")

st.markdown("</div>", unsafe_allow_html=True)

# --- FORMULÁRIO DE CONTATO RÁPIDO ---
st.write("---")
st.subheader("Entre em contato")

col_form, col_info = st.columns([2, 1])

with col_form:
    with st.form("form_contato"):
        c1, c2 = st.columns(2)
        c1.text_input("Nome")
        c2.text_input("Email")
        st.selectbox("Eu sou...", ["Paciente", "Médico/Fisioterapeuta", "Distribuidor"])
        st.text_area("Mensagem ou Dúvida")
        st.form_submit_button("ENVIAR MENSAGEM")

with col_info:
    st.markdown("""
    **Icarus Medical Brasil** São Paulo, SP
    
    📧 contato@icarusmedical.com.br  
    📞 (11) 99999-9999
    """)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <p>ICARUS MEDICAL © 2024. Todos os direitos reservados.</p>
    <p>Política de Privacidade | Termos de Uso</p>
</div>
""", unsafe_allow_html=True)
