import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Plunder & Poach | Estratégia e Design",
    page_icon="⚓",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (PLUNDER & POACH STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap');

    /* Cores e Fundo Envelhecido */
    .stApp {
        background-color: #f4f1ea; /* Papel/Creme envelhecido */
        color: #1a1a1a;
    }

    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Característica */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, .serif-poach {
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -1px;
    }

    /* Divisórias de Luxo */
    .divider {
        border-top: 1px solid #1a1a1a;
        border-bottom: 4px solid #1a1a1a;
        height: 8px;
        margin: 40px 0;
    }

    /* Navegação */
    .nav-pp {
        display: flex;
        justify-content: space-between;
        padding: 40px 6%;
        border-bottom: 1px solid #1a1a1a;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Hero Section */
    .hero-pp {
        padding: 100px 6% 80px 6%;
        text-align: center;
    }
    .hero-title {
        font-size: clamp(50px, 10vw, 130px);
        line-height: 0.9;
        margin-bottom: 30px;
    }

    /* Grid de Projetos com Bordas */
    .project-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        border-top: 1px solid #1a1a1a;
    }
    
    .project-item {
        border-right: 1px solid #1a1a1a;
        border-bottom: 1px solid #1a1a1a;
        padding: 60px;
        transition: background-color 0.4s ease;
    }
    .project-item:nth-child(even) { border-right: none; }
    .project-item:hover { background-color: #ede9e0; }

    .project-img {
        width: 100%;
        filter: sepia(0.2) contrast(1.1);
        margin-bottom: 30px;
    }

    /* Botão Estilo Selo */
    div.stButton > button {
        background-color: #1a1a1a;
        color: #f4f1ea;
        border: none;
        border-radius: 0px;
        padding: 15px 40px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #333;
        color: #f4f1ea;
    }

    /* Footer */
    .footer-pp {
        padding: 100px 6%;
        background-color: #1a1a1a;
        color: #f4f1ea;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-pp">
    <div>Plunder & Poach</div>
    <div style="display: flex; gap: 40px;">
        <span>Trabalhos</span>
        <span>Estúdio</span>
        <span>Journal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown("""
<div class="hero-pp">
    <p style="text-transform: uppercase; letter-spacing: 4px; font-size: 12px; margin-bottom: 20px;">Estratégia · Design · Rebeldia</p>
    <h1 class="hero-title">SAQUEAMOS<br>O COMUM.</h1>
    <div class="divider" style="max-width: 300px; margin: 40px auto;"></div>
    <p style="max-width: 700px; margin: 0 auto; font-size: 18px; line-height: 1.6;">
        Somos uma agência de criação para marcas que não têm medo de quebrar as regras. 
        Transformamos negócios em lendas através de um design audacioso e narrativas implacáveis.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. SHOWCASE (GRID ASSIMÉTRICO) ---
st.markdown('<div class="project-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")

with col1:
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1527067829737-402993088e6b?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Ouro Negro</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">IDENTIDADE VISUAL / CAFÉ</p>
        <p>Uma marca construída sobre a herança e o sabor intenso.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-item" style="border-bottom: none;">
        <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Bússola Norte</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">ESTRATÉGIA DIGITAL / 2024</p>
        <p>Guiando marcas em mares nunca navegados.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1560067174-c5a3a8f37060?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Alcateia Alpha</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">DIREÇÃO DE ARTE / MODA</p>
        <p>O instinto selvagem traduzido em alfaiataria premium.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-item" style="border-bottom: none;">
        <img src="https://images.unsplash.com/photo-1520004434532-668416a08753?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Armazém V</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">BRANDING / ARQUITETURA</p>
        <p>Espaços que respiram história e design industrial.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MANIFESTO (SEÇÃO ESCURA) ---
st.markdown("""
<div style="background-color: #1a1a1a; color: #f4f1ea; padding: 150px 6%; text-align: center;">
    <h2 class="serif-poach" style="font-size: 50px; margin-bottom: 40px;">VOCÊ É A PREDA OU O PREDADOR?</h2>
    <p style="max-width: 800px; margin: 0 auto; font-size: 22px; font-style: italic; opacity: 0.8;">
        "No mercado moderno, a neutralidade é o caminho mais rápido para a extinção. 
        Nós ajudamos você a afiar as garras e dominar seu território."
    </p>
    <div style="margin-top: 60px;">
        <p style="text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin-bottom: 20px;">Pronto para o ataque?</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.button("Inicie sua Jornada")

# --- 5. FOOTER ---
st.markdown("""
<div class="footer-pp">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
        <div>
            <h2 class="serif-poach" style="font-size: 28px;">Plunder & Poach.</h2>
            <p style="opacity: 0.6; font-size: 13px;">Capturando a essência do extraordinário.</p>
        </div>
        <div style="text-align: right; line-height: 2;">
            <p style="font-weight: 700;">CONTATO</p>
            <p style="opacity: 0.6;">studio@plunderpoach.com<br>Londres / Global</p>
        </div>
    </div>
    <div style="margin-top: 80px; padding-top: 20px; border-top: 1px solid rgba(244, 241, 234, 0.1); font-size: 10px; opacity: 0.4;">
        © 2026 PLUNDER & POACH — TODOS OS DIREITOS RESERVADOS.
    </div>
</div>
""", unsafe_allow_html=True)
