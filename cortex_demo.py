import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Daniel Aristizábal | Studio",
    page_icon="🎨",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (ARISTIZÁBAL STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&family=Inter:wght@900&display=swap');

    /* Reset Geral */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Estúdio */
    html, body, [class*="css"] {
        font-family: 'JetBrains+Mono', monospace;
    }

    /* Header Fixo e Minimalista */
    .header-daniel {
        display: flex;
        justify-content: space-between;
        padding: 30px 40px;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        background: rgba(0,0,0,0.8);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #222;
        text-transform: uppercase;
        font-size: 12px;
        letter-spacing: 2px;
    }

    /* Hero Section */
    .hero-section {
        padding: 180px 40px 100px 40px;
        text-align: left;
    }
    .hero-big-text {
        font-family: 'Inter', sans-serif;
        font-size: clamp(40px, 12vw, 160px);
        font-weight: 900;
        line-height: 0.85;
        letter-spacing: -0.05em;
        margin-bottom: 40px;
    }

    /* Grade de Projetos (Mosaic Grid) */
    .grid-wrap {
        padding: 0 40px;
        display: grid;
        grid-template-columns: repeat(12, 1fr);
        gap: 20px;
    }

    .project-item {
        position: relative;
        overflow: hidden;
        margin-bottom: 40px;
    }

    .project-img {
        width: 100%;
        height: auto;
        display: block;
        transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        filter: saturate(1.2);
    }
    
    .project-item:hover .project-img {
        transform: scale(1.03);
    }

    .project-info {
        margin-top: 15px;
        font-size: 11px;
        text-transform: uppercase;
        color: #666;
        display: flex;
        justify-content: space-between;
    }

    /* Rodapé */
    .footer-daniel {
        padding: 100px 40px;
        border-top: 1px solid #222;
        margin-top: 100px;
    }

    /* Esconder elementos do Streamlit */
    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="header-daniel">
    <div>Daniel Aristizábal</div>
    <div style="display: flex; gap: 40px;">
        <span>Index</span>
        <span>Studio</span>
        <span>Archive</span>
        <span>Shop</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown("""
<div class="hero-section">
    <div class="hero-big-text">
        DANIEL<br>ARISTI<br>ZÁBAL
    </div>
    <p style="max-width: 600px; font-size: 14px; color: #888; line-height: 1.6;">
        Digital Art Director and Motion Designer. Merging surrealism with CGI to explore new visual languages. 
        Based in Medellín, working globally.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. PROJETOS (GRID ASSIMÉTRICO) ---

def render_project(col, img_url, title, year, width="100%"):
    with col:
        st.markdown(f"""
        <div class="project-item">
            <img src="{img_url}" class="project-img" style="width: {width};">
            <div class="project-info">
                <span style="color:#fff;">{title}</span>
                <span>[{year}]</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Linha 1: Um grande e um pequeno
c1, c2 = st.columns([2, 1])
render_project(c1, "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200", "Digital Surrealism", "2024")
render_project(c2, "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=600", "Chrome Study", "2023")

# Linha 2: Três imagens menores (estilo mosaico)
c3, c4, c5 = st.columns(3)
render_project(c3, "https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=600", "Organic Forms", "2024")
render_project(c4, "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=600", "Color Theory", "2023")
render_project(c5, "https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=600", "Texture Flow", "2022")

# Linha 3: Um vertical e um horizontal
c6, c7 = st.columns([1, 2])
render_project(c6, "https://images.unsplash.com/photo-1574169208507-84376144848b?w=600", "CGI Sculpture", "2024")
render_project(c7, "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=1200", "Metaverse Landscapes", "2024")

# --- 4. SEÇÃO SOBRE (COMPRIDA) ---
st.markdown("""
<div style="padding: 150px 40px; background-color: #080808;">
    <h2 style="font-family:'Inter'; font-size: 60px; font-weight: 900; letter-spacing: -2px;">THE STUDIO</h2>
    <p style="font-size: 24px; max-width: 800px; color: #ccc; line-height: 1.2; margin-top: 30px;">
        Nós operamos na intersecção entre o design clássico e o futurismo digital. 
        Especializados em CGI, direção de arte e identidades visuais que desafiam a lógica.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div class="footer-daniel">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <p style="color: #fff; font-weight: 700;">CONNECT</p>
            <p style="color: #666; font-size: 14px; margin-top: 10px;">Instagram<br>Behance<br>LinkedIn<br>Vimeo</p>
        </div>
        <div style="text-align: right;">
            <p style="color: #fff; font-weight: 700;">NEW BUSINESS</p>
            <p style="color: #666; font-size: 14px; margin-top: 10px;">studio@aristizabal.net</p>
        </div>
    </div>
    <div style="margin-top: 80px; font-size: 10px; color: #333; letter-spacing: 2px;">
        © 2026 DANIEL ARISTIZÁBAL STUDIO — ALL RIGHTS RESERVED
    </div>
</div>
""", unsafe_allow_html=True)
