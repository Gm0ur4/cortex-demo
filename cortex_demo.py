import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Begg | Creative Portfolio",
    page_icon="🕊️",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (BEGG AESTHETIC) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=Inter:wght@300;400;500&display=swap');

    /* Cores e Background */
    .stApp {
        background-color: #fcfcfc; /* Off-white característico */
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #2c2c2c;
    }

    h1, h2, h3, .serif {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 300;
        font-style: italic;
    }

    /* Header Flutuante */
    .nav-begg {
        display: flex;
        justify-content: space-between;
        padding: 40px 8%;
        font-size: 13px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Hero Section */
    .hero-begg {
        padding: 100px 8% 150px 8%;
        text-align: center;
    }
    .hero-title {
        font-size: clamp(50px, 8vw, 100px);
        line-height: 1;
        margin-bottom: 20px;
    }

    /* Project Image System */
    .project-container {
        padding: 0 8% 100px 8%;
    }
    .img-wrap {
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 25px;
        background-color: #eee;
        transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .img-wrap:hover {
        transform: scale(0.98);
    }
    .img-wrap img {
        width: 100%;
        display: block;
    }

    .project-label {
        font-family: 'Cormorant Garamond', serif;
        font-size: 32px;
        font-style: italic;
        margin-bottom: 5px;
    }
    .project-category {
        font-size: 12px;
        text-transform: uppercase;
        color: #888;
        letter-spacing: 2px;
    }

    /* Seção de Texto Centralizada */
    .about-text {
        max-width: 800px;
        margin: 150px auto;
        text-align: center;
        font-family: 'Cormorant Garamond', serif;
        font-size: 42px;
        line-height: 1.2;
        font-style: italic;
    }

    /* Footer */
    .footer-begg {
        padding: 100px 8% 50px 8%;
        border-top: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #999;
    }

    /* Botão Customizado */
    div.stButton > button {
        background: transparent;
        border: 1px solid #2c2c2c;
        border-radius: 50px;
        padding: 10px 30px;
        font-size: 12px;
        text-transform: uppercase;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #2c2c2c;
        color: #fff;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. NAV BAR ---
st.markdown("""
<div class="nav-begg">
    <div>Begg. Portfolio</div>
    <div style="display: flex; gap: 30px;">
        <span>Works</span>
        <span>About</span>
        <span>Contact</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown("""
<div class="hero-begg">
    <h1 class="hero-title">Selected Works<br>2023 — 2026</h1>
</div>
""", unsafe_allow_html=True)

# --- 3. PROJETOS (LAYOUT ASSIMÉTRICO) ---
# Projeto 1 (Grande)
st.markdown("""
<div class="project-container">
    <div class="img-wrap">
        <img src="https://images.unsplash.com/photo-1549490349-8643362247b5?w=1600">
    </div>
    <div class="project-label">Velvet Horizon</div>
    <div class="project-category">Brand Identity</div>
</div>
""", unsafe_allow_html=True)

# Projetos 2 e 3 (Lado a Lado)
col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown("""
    <div class="project-container" style="padding-left:0; padding-right:0;">
        <div class="img-wrap">
            <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800">
        </div>
        <div class="project-label">The Essentialist</div>
        <div class="project-category">Product Design</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-container" style="padding-left:0; padding-right:0; margin-top: 80px;">
        <div class="img-wrap">
            <img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=800">
        </div>
        <div class="project-label">Silent Studio</div>
        <div class="project-category">Art Direction</div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. PHILOSOPHY SECTION ---
st.markdown("""
<div class="about-text">
    "Design is not just what it looks like and feels like. Design is how it works."
</div>
""", unsafe_allow_html=True)

# --- 5. PROJETO FINAL ---
st.markdown("""
<div class="project-container">
    <div class="img-wrap">
        <img src="https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?w=1600">
    </div>
    <div class="project-label">Nordic Solitude</div>
    <div class="project-category">Photography</div>
</div>
""", unsafe_allow_html=True)

# --- 6. CTA ---
st.markdown("<div style='text-align:center; padding: 100px 0;'>", unsafe_allow_html=True)
st.markdown("<h2 class='serif' style='font-size: 60px;'>Interested in working together?</h2>", unsafe_allow_html=True)
st.button("Get in touch")
st.markdown("</div>", unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("""
<div class="footer-begg">
    <div>© 2026 BEGG STUDIO</div>
    <div style="display: flex; gap: 40px;">
        <span>Instagram</span>
        <span>Behance</span>
        <span>LinkedIn</span>
    </div>
</div>
""", unsafe_allow_html=True)
