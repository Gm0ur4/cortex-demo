import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Justine Soulié | Diretora de Arte & Designer",
    page_icon="✨",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (ESTILO JUSTINE SOULIÉ) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Montserrat:wght@300;400;600&display=swap');

    /* Fundo suave e cores base */
    .stApp {
        background-color: #f2efea; /* Creme característico */
        color: #2c2c2c;
    }

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        font-weight: 300;
    }

    h1, h2, h3, .serif-italic {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-weight: 300;
    }

    /* Header Minimalista */
    .nav-justine {
        display: flex;
        justify-content: space-between;
        padding: 40px 6%;
        font-size: 11px;
        letter-spacing: 2px;
        text-transform: uppercase;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        background: rgba(242, 239, 234, 0.8);
        backdrop-filter: blur(5px);
    }

    /* Hero Section */
    .hero-container {
        padding: 200px 6% 100px 6%;
        text-align: left;
    }
    .hero-title {
        font-size: clamp(40px, 7vw, 90px);
        line-height: 1.1;
        margin-bottom: 20px;
    }

    /* Galeria de Projetos (Layout Editorial) */
    .project-wrapper {
        padding: 0 6% 150px 6%;
    }

    .project-card {
        margin-bottom: 150px;
        position: relative;
    }

    .project-image {
        width: 100%;
        height: auto;
        transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        display: block;
    }
    
    .project-card:hover .project-image {
        transform: scale(1.02);
    }

    .project-meta {
        margin-top: 20px;
        display: flex;
        justify-content: space-between;
        align-items: baseline;
    }

    .project-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 38px;
        font-style: italic;
    }

    .project-tag {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #888;
    }

    /* Seção de Texto (Sobre) */
    .about-section {
        padding: 150px 20%;
        text-align: center;
        background-color: #e8e4de; /* Tom um pouco mais escuro */
    }

    .about-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 46px;
        font-style: italic;
        line-height: 1.3;
    }

    /* Footer */
    .footer-justine {
        padding: 100px 6% 40px 6%;
        display: flex;
        justify-content: space-between;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-top: 1px solid #dcd7cf;
    }

    /* Custom Hide Streamlit */
    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-justine">
    <div>Justine Soulié — Designer Independente</div>
    <div style="display: flex; gap: 40px;">
        <span>Projetos</span>
        <span>Estúdio</span>
        <span>Contato</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">
        Direção de Arte & <br>
        Identidades Digitais 
        <span class="serif-italic" style="color: #888;">Elegantes.</span>
    </h1>
</div>
""", unsafe_allow_html=True)

# --- 3. PROJETOS (LAYOUT FLUIDO) ---

def render_project(col, img_url, title, tag, padding_top="0px"):
    with col:
        st.markdown(f"""
        <div class="project-card" style="padding-top: {padding_top};">
            <img src="{img_url}" class="project-image">
            <div class="project-meta">
                <div class="project-name">{title}</div>
                <div class="project-tag">{tag}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Layout alternado (um maior, um menor com recuo)
c1, c2 = st.columns([1.5, 1])
render_project(c1, "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=1000", "L'Art de Vivre", "Identidade Visual")
render_project(c2, "https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?w=800", "Essência Pura", "Fotografia", padding_top="100px")

# Layout de coluna única para impacto
st.markdown('<div class="project-wrapper">', unsafe_allow_html=True)
st.markdown("""
<div class="project-card">
    <img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1600" class="project-image">
    <div class="project-meta">
        <div class="project-name">Coleção Outono</div>
        <div class="project-tag">Direção de Arte / 2024</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Mais dois projetos lado a lado
c3, c4 = st.columns([1, 1.2])
render_project(c3, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800", "Objeto Mínimo", "Design de Produto", padding_top="50px")
render_project(c4, "https://images.unsplash.com/photo-1509343256512-d77a5cb3791b?w=1000", "Estúdio de Luz", "Branding")

# --- 4. SOBRE (SOB MEDIDA) ---
st.markdown("""
<div class="about-section">
    <div class="about-text">
        "Acredito que a beleza reside na simplicidade e no equilíbrio entre o espaço vazio e a tipografia clássica."
    </div>
    <p style="margin-top: 40px; text-transform: uppercase; font-size: 11px; letter-spacing: 2px;">Sobre Justine</p>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div class="footer-justine">
    <div>Disponível para novos projetos — 2026</div>
    <div style="text-align: right;">
        Instagram / Behance / LinkedIn <br>
        justine@soulie.fr
    </div>
</div>
""", unsafe_allow_html=True)
