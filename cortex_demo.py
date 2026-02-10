import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Site Pro | Templates de Alta Conversão",
    page_icon="🚀",
    layout="wide"
)

# --- CSS MASTER (HÍBRIDO DE TODOS OS ESTILOS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&family=Playfair+Display:ital,wght@0,900;1,900&display=swap');

    :root {
        --primary: #0066ff; /* Azul Tech de Conversão */
        --dark: #0a0a0a;
        --light: #f8f9fa;
    }

    .stApp { background-color: white; color: var(--dark); }
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; }

    /* Tipografia */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    h1, h2, .impact-text { font-family: 'Inter', sans-serif; font-weight: 800; letter-spacing: -0.04em; }

    /* 1 & 2. HERO SECTION */
    .hero-container {
        padding: 120px 8% 80px 8%;
        text-align: center;
        background: radial-gradient(circle at top right, #f0f7ff 0%, white 50%);
    }
    .hero-h1 { font-size: clamp(45px, 6vw, 85px); line-height: 1; margin-bottom: 30px; color: var(--dark); }
    .hero-sub { font-size: clamp(18px, 2vw, 24px); color: #555; max-width: 800px; margin: 0 auto 40px auto; line-height: 1.5; }

    /* 3 & 4. CARROSSEL DE TEMPLATES */
    .template-card {
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #eee;
        transition: 0.4s;
        margin-bottom: 20px;
    }
    .template-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); border-color: var(--primary); }
    
    /* 5. PROVA SOCIAL */
    .client-avatar {
        width: 60px; height: 60px; border-radius: 50%; border: 3px solid white; margin-left: -15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    /* 6. "É PARA VOCÊ QUE" */
    .for-you-box {
        background: var(--dark);
        color: white;
        padding: 80px 8%;
        border-radius: 40px;
        margin: 50px 5%;
    }
    .check-item { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; font-size: 18px; }

    /* 7. PASSO A PASSO (ROEEBY STYLE) */
    .step-number { font-size: 60px; font-weight: 800; color: rgba(0,102,255,0.1); position: absolute; top: -20px; left: 0; z-index: -1; }
    .step-container { position: relative; padding-top: 20px; }

    /* 8. PREÇOS (QUDRIX STYLE) */
    .price-card {
        padding: 50px 30px; border-radius: 20px; border: 1px solid #eee; text-align: center; transition: 0.3s;
    }
    .price-card.featured { background: var(--dark); color: white; border: none; transform: scale(1.05); }

    /* Botão Master */
    div.stButton > button {
        background: var(--primary); color: white; border: none; padding: 20px 45px; border-radius: 10px; font-weight: 800; font-size: 18px; width: 100%; transition: 0.3s;
    }
    div.stButton > button:hover { background: #0052cc; transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- 1 & 2. HERO SECTION ---
st.markdown(f"""
<div class="hero-container">
    <p style="color: var(--primary); font-weight: 700; letter-spacing: 2px; margin-bottom: 20px;">LANÇAMENTO 2026</p>
    <h1 class="hero-h1">Tenha um site de elite.<br>Sem escrever uma linha de código.</h1>
    <p class="hero-sub">Escolha entre templates validados por designers internacionais. Customize em minutos, economize milhares de reais e coloque seu negócio no mapa hoje.</p>
</div>
""", unsafe_allow_html=True)

col_hero_btn, _ = st.columns([1, 2])
with col_hero_btn:
    st.button("QUERO MEU SITE AGORA →")

# --- 3 & 4. CARROSSEL DE TEMPLATES ---
st.markdown("""
<div style="padding: 100px 8% 50px 8%;">
    <h2 style="font-size: 42px;">Conheça nossos templates</h2>
    <p style="color: #666;">Designs de alta performance para cada nicho de mercado.</p>
</div>
""", unsafe_allow_html=True)

# Simulando o Carrossel com Colunas (Pode ser expansível)
t_col1, t_col2, t_col3 = st.columns(3)

def template_item(col, name, category, img_url):
    with col:
        st.markdown(f"""
        <div class="template-card">
            <img src="{img_url}" style="width:100%; height: 250px; object-fit: cover;">
            <div style="padding: 20px;">
                <p style="font-size: 12px; color: var(--primary); font-weight: 700;">{category}</p>
                <h4 style="margin: 5px 0 15px 0;">{name}</h4>
                <div style="font-size: 13px; font-weight: 600; border-bottom: 2px solid #eee; display: inline-block;">VER DEMONSTRAÇÃO</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# INSIRA AS URLs DAS IMAGENS DOS SEUS TEMPLATES AQUI
template_item(t_col1, "The Rogue Botanical", "EDITORIAL / FLORAL", "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?w=800")
template_item(t_col2, "Qudrix Tech Suite", "SAAS / SOFTWARE", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800")
template_item(t_col3, "Roeeby Luxury", "E-COMMERCE / DESIGN", "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=800")

# --- 5. CONFIE EM QUEM JÁ USA ---
st.markdown("""
<div style="padding: 80px 8%; text-align: center; background: #fafafa; border-radius: 50px; margin: 0 5%;">
    <h3 style="margin-bottom: 30px;">Centenas de clientes já lançaram seus sites</h3>
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="https://randomuser.me/api/portraits/women/1.jpg" class="client-avatar">
        <img src="https://randomuser.me/api/portraits/men/2.jpg" class="client-avatar">
        <img src="https://randomuser.me/api/portraits/women/3.jpg" class="client-avatar">
        <img src="https://randomuser.me/api/portraits/men/4.jpg" class="client-avatar">
        <img src="https://randomuser.me/api/portraits/women/5.jpg" class="client-avatar">
    </div>
    <p style="font-weight: 600; color: #555;">+1.200 projetos publicados com sucesso em todo o Brasil.</p>
</div>
""", unsafe_allow_html=True)

# --- 6. É PARA VOCÊ QUE ---
st.markdown("""
<div class="for-you-box">
    <h2 style="font-size: 42px; margin-bottom: 50px;">Este é o seu próximo passo se você:</h2>
    <div class="check-item">✅ Quer um site profissional em minutos pelo menor preço do mercado.</div>
    <div class="check-item">✅ Deseja lucrar vendendo sites de alta qualidade para seus clientes.</div>
    <div class="check-item">✅ Precisa aumentar a conversão do seu produto digital ou serviço imediatamente.</div>
</div>
""", unsafe_allow_html=True)

# --- 7. PASSO A PASSO ---
st.markdown('<div style="padding: 100px 8%;">', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 42px; margin-bottom: 80px; text-align: center;">Do zero ao site no ar em 4 passos</h2>', unsafe_allow_html=True)

s_col1, s_col2, s_col3, s_col4 = st.columns(4)

steps = [
    ("Acesso Instantâneo", "Após a compra, todos os templates são liberados imediatamente."),
    ("Escolha & Estilo", "Escolha o design que mais combina com seu negócio e copie o código."),
    ("Configuração Express", "Te ensinamos a configurar sua URL própria em menos de 5 minutos."),
    ("Pronto para Lucrar", "Seu site está vivo! Edite o que quiser quando quiser de forma simples.")
]

for i, (col, (title, desc)) in enumerate(zip([s_col1, s_col2, s_col3, s_col4], steps)):
    with col:
        st.markdown(f"""
        <div class="step-container">
            <div class="step-number">0{i+1}</div>
            <h4 style="margin-bottom: 15px;">{title}</h4>
            <p style="font-size: 14px; color: #666; line-height: 1.6;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. PREÇOS ---
st.markdown('<div style="padding: 100px 8%; background: #fdfdfd;">', unsafe_allow_html=True)
p_col1, p_col2, p_col3 = st.columns(3, gap="large")

with p_col1:
    st.markdown("""
    <div class="price-card">
        <h3>Starter</h3>
        <h2 style="font-size: 45px; margin: 20px 0;">R$ 97</h2>
        <p style="color: #666; margin-bottom: 30px;">Ideal para iniciantes</p>
        <p>✓ 1 Template à escolha</p>
        <p>✓ Tutorial de Instalação</p>
        <p>✓ Suporte via E-mail</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Assinar Starter", key="p1")

with p_col2:
    st.markdown("""
    <div class="price-card featured">
        <p style="color: var(--primary); font-weight: 800; font-size: 12px; margin-bottom: 10px;">MAIS VENDIDO</p>
        <h3>Pro Bundle</h3>
        <h2 style="font-size: 45px; margin: 20px 0;">R$ 197</h2>
        <p style="color: #aaa; margin-bottom: 30px;">Para quem quer escalar</p>
        <p>✓ Todos os Templates</p>
        <p>✓ Curso: Venda sites por R$ 2k</p>
        <p>✓ Suporte VIP WhatsApp</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("QUERO O PRO BUNDLE", key="p2")

with p_col3:
    st.markdown("""
    <div class="price-card">
        <h3>Agency</h3>
        <h2 style="font-size: 45px; margin: 20px 0;">R$ 497</h2>
        <p style="color: #666; margin-bottom: 30px;">Domine o mercado</p>
        <p>✓ Acesso Vitalício</p>
        <p>✓ Templates Exclusivos Mensais</p>
        <p>✓ Consultoria de Negócios</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Assinar Agency", key="p3")
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FAQ ---
st.markdown('<div style="padding: 100px 20%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; margin-bottom: 50px;">Dúvidas Frequentes</h2>', unsafe_allow_html=True)

with st.expander("Preciso saber programar?"):
    st.write("De jeito nenhum. Nosso método é baseado em copiar e colar o código no lugar certo. Nós te mostramos exatamente onde clicar.")

with st.expander("O site é meu para sempre?"):
    st.write("Sim! Uma vez adquirido o template e configurado no seu repositório, o site é de sua total propriedade.")

with st.expander("Consigo colocar meu próprio domínio (.com.br)?"):
    st.write("Com certeza. Te ensinamos a configurar seu domínio personalizado em poucos segundos.")
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="padding: 80px 8% 40px 8%; background: var(--dark); color: white; text-align: center;">
    <h2 style="margin-bottom: 20px;">SITE PRO</h2>
    <p style="opacity: 0.5; font-size: 13px;">A revolução do desenvolvimento sem código.</p>
    <p style="margin-top: 40px; opacity: 0.3; font-size: 11px;">© 2026 Todos os direitos reservados.</p>
</div>
""", unsafe_allow_html=True)
