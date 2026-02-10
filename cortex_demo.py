import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Fundable | Plataforma de Equity Crowdfunding",
    page_icon="💰",
    layout="wide"
)

# --- CSS AVANÇADO (FUNDABLE DESIGN SYSTEM) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Open Sans', sans-serif;
        color: #333;
    }

    /* Header Superior */
    .main-header {
        background-color: #1a2b3c;
        padding: 15px 8%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: -5rem -5rem 0rem -5rem;
    }
    .nav-links a {
        color: #99abbd;
        text-decoration: none;
        margin-left: 25px;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
    }
    .nav-links a:hover { color: white; }

    /* Hero Section Gigante */
    .hero-bg {
        background: linear-gradient(135deg, #1e3a5f 0%, #2c3e50 100%);
        padding: 100px 10%;
        text-align: center;
        color: white;
        margin: 0rem -5rem 40px -5rem;
    }
    .hero-title { font-size: 52px; font-weight: 800; margin-bottom: 15px; }
    .hero-subtitle { font-size: 22px; font-weight: 300; opacity: 0.9; margin-bottom: 40px; }

    /* Seção de Logos (Prova Social) */
    .trust-bar {
        text-align: center;
        padding: 20px 0;
        background-color: #f4f7f9;
        margin-top: -40px;
        margin-bottom: 50px;
        border-bottom: 1px solid #e1e8ed;
    }

    /* Cards de Startups */
    .st_card {
        background: white;
        border: 1px solid #e1e8ed;
        border-radius: 6px;
        transition: 0.3s;
        margin-bottom: 30px;
    }
    .st_card:hover { box-shadow: 0 15px 35px rgba(0,0,0,0.1); }
    .card-img { width: 100%; height: 220px; object-fit: cover; border-radius: 6px 6px 0 0; }
    .card-body { padding: 25px; }
    .card-tag { color: #00a8ff; font-weight: 700; font-size: 11px; text-transform: uppercase; }
    .card-title { font-size: 20px; font-weight: 700; margin: 10px 0; }
    
    /* Barra de Progresso */
    .p-bar-bg { background: #eee; height: 10px; border-radius: 5px; margin: 20px 0 10px 0; }
    .p-bar-fill { background: #00a8ff; height: 10px; border-radius: 5px; }

    /* Footer Multinível */
    .footer-container {
        background-color: #1a2b3c;
        color: #99abbd;
        padding: 60px 10% 30px 10%;
        margin: 50px -5rem -5rem -5rem;
    }
    .footer-col h4 { color: white; margin-bottom: 20px; font-size: 16px; }
    .footer-col p { font-size: 13px; line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAV BAR ---
st.markdown("""
<div class="main-header">
    <div style="font-size: 24px; font-weight: 800; color: white;">FUND<span style="color:#00a8ff">ABLE</span></div>
    <div class="nav-links">
        <a href="#">Como Funciona</a>
        <a href="#">Explorar Startups</a>
        <a href="#">Sucesso</a>
        <a href="#">Entrar</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-bg">
    <div class="hero-title">Onde as Startups Arrecadam Capital</div>
    <div class="hero-subtitle">Junte-se a maior rede de financiamento do mundo para lançar e crescer seu negócio.</div>
</div>
""", unsafe_allow_html=True)

# Botões de Chamada (Call to Action)
c_cta1, c_cta2 = st.columns(2)
with c_cta1:
    st.markdown('<div style="text-align:right">', unsafe_allow_html=True)
    if st.button("QUERO CAPTAR PARA MINHA EMPRESA", key="main_fund"):
        st.info("Iniciando processo de captação...")
    st.markdown('</div>', unsafe_allow_html=True)

with c_cta2:
    st.markdown('<style>div.stButton > button { background-color: #00a8ff !important; color: white !important; border: none; padding: 15px 30px; font-weight: 700; }</style>', unsafe_allow_html=True)
    if st.button("QUERO INVESTIR EM STARTUPS", key="main_invest"):
        st.balloons()

# --- 3. PROVA SOCIAL ---
st.markdown("""
<div class="trust-bar">
    <p style="color:#7f8c8d; font-size:12px; font-weight:700; margin-bottom:15px;">VISTO EM</p>
    <div style="display:flex; justify-content:center; gap:50px; opacity:0.5; font-weight:800; font-size:20px; color:#2c3e50;">
        <span>Forbes</span> <span>Wired</span> <span>TechCrunch</span> <span>The Wall Street Journal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 4. SEÇÃO "DUAS ESCOLHAS" ---
st.write("")
col_a, col_b = st.columns(2, gap="large")

with col_a:
    st.image("https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=600&q=80", caption="Para Empreendedores")
    st.subheader("Levante Capital")
    st.write("Criamos perfis de captação que atraem investidores anjos e fundos de VC. Ferramentas completas para gerenciar sua rodada de investimentos.")
    st.button("Saiba mais sobre Captação", key="info_fund")

with col_b:
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80", caption="Para Investidores")
    st.subheader("Invista cedo")
    st.write("Acesse oportunidades exclusivas em startups pré-filtradas. Invista em empresas com alto potencial de crescimento antes de chegarem ao mercado público.")
    st.button("Ver Oportunidades de Investimento", key="info_invest")

st.write("---")

# --- 5. GRID DE STARTUPS (BROWSE) ---
st.header("Startups em Captação")

def draw_card(col, img, tag, title, desc, progress, goal):
    with col:
        st.markdown(f"""
        <div class="st_card">
            <img src="{img}" class="card-img">
            <div class="card-body">
                <div class="card-tag">{tag}</div>
                <div class="card-title">{title}</div>
                <p style="font-size:14px; color:#555;">{desc}</p>
                <div class="p-bar-bg"><div class="p-bar-fill" style="width:{progress}%"></div></div>
                <div style="display:flex; justify-content:space-between; font-size:13px;">
                    <b>{progress}% Arrecadado</b>
                    <span style="color:#888">Meta: {goal}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Analisar {title}", use_container_width=True)

c1, c2, c3 = st.columns(3)
draw_card(c1, "https://images.unsplash.com/photo-1551288049-bbbda536339a?w=400", "FINTECH", "NeoBank Pro", "A conta digital focada 100% em pequenas empresas e MEI.", 78, "R$ 5M")
draw_card(c2, "https://images.unsplash.com/photo-1532187878418-9f110f9902de?w=400", "BIOTECH", "GenomeX", "Sequenciamento genético acessível para medicina preventiva.", 45, "R$ 12M")
draw_card(c3, "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=400", "SAAS", "CloudFlow", "Automação de fluxo de trabalho para agências de marketing.", 92, "R$ 1.5M")

# --- 6. FOOTER COMPLETO ---
st.markdown("""
<div class="footer-container">
    <div style="display:grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap:40px;">
        <div class="footer-col">
            <div style="font-size: 20px; font-weight: 800; color: white; margin-bottom:20px;">FUNDABLE</div>
            <p>A Fundable é a plataforma líder para startups levantarem capital, conectando fundadores a uma rede global de investidores.</p>
        </div>
        <div class="footer-col">
            <h4>PLATAFORMA</h4>
            <p>Como Funciona<br>Explorar<br>Educação<br>Equipe</p>
        </div>
        <div class="footer-col">
            <h4>RECURSOS</h4>
            <p>Blog<br>Ajuda/FAQ<br>Termos de Uso<br>Privacidade</p>
        </div>
        <div class="footer-col">
            <h4>CONTATO</h4>
            <p>Suporte<br>Imprensa<br>Parcerias</p>
        </div>
    </div>
    <div style="text-align:center; border-top:1px solid #2c3e50; margin-top:40px; padding-top:20px; font-size:12px;">
        © 2024 Fundable LLC - Uma empresa Startups.com
    </div>
</div>
""", unsafe_allow_html=True)
