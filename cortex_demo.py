import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Breakfast | Digital Design Studio",
    page_icon="🍳",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (BREAKFAST SYSTEM) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&display=swap');

    /* Reset Geral */
    .stApp { background-color: #ffffff; }
    [data-testid="stHeader"] { display: none; } /* Esconde o header do Streamlit */
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Estilo Breakfast */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #000000;
        -webkit-font-smoothing: antialiased;
    }

    /* Linhas de Grade (The Grid) */
    .grid-line-h { border-bottom: 1px solid #000; width: 100%; }
    .grid-line-v { border-right: 1px solid #000; height: 100%; }

    /* Header Fixo/Nav */
    .nav-container {
        display: flex;
        justify-content: space-between;
        padding: 25px 40px;
        border-bottom: 1px solid #000;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Hero Section - A tipografia é o centro */
    .hero-wrap {
        padding: 120px 40px;
        border-bottom: 1px solid #000;
    }
    .hero-main-text {
        font-size: clamp(50px, 14vw, 220px);
        font-weight: 900;
        line-height: 0.8;
        letter-spacing: -0.05em;
        text-transform: uppercase;
    }

    /* Project Section */
    .project-block {
        display: grid;
        grid-template-columns: 1fr 1fr; /* Duas colunas perfeitas */
        border-bottom: 1px solid #000;
    }
    .project-cell {
        border-right: 1px solid #000;
        position: relative;
        overflow: hidden;
    }
    .project-cell:last-child { border-right: none; }
    
    .project-img {
        width: 100%;
        aspect-ratio: 1 / 1;
        object-fit: cover;
        display: block;
        transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .project-img:hover { transform: scale(1.05); }

    .project-label {
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        font-weight: 700;
        font-size: 11px;
        text-transform: uppercase;
        border-top: 1px solid #000;
    }

    /* Big Text / Philosophy Section */
    .philosophy-section {
        padding: 150px 40px;
        font-size: clamp(24px, 5vw, 64px);
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -0.02em;
        border-bottom: 1px solid #000;
    }

    /* Footer */
    .footer-container {
        padding: 80px 40px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
    }
    .footer-logo { font-size: 100px; font-weight: 900; letter-spacing: -5px; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-container">
    <div>Breakfast.</div>
    <div style="display: flex; gap: 40px;">
        <span>Work</span>
        <span>Studio</span>
        <span>Contact</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown("""
<div class="hero-wrap">
    <div class="hero-main-text">
        DIGITAL<br>CRAFT<br>STUDIO
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. PROJETOS (GRID 2x2) ---
# Projeto 1 e 2
st.markdown('<div class="project-block">', unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown("""
    <div class="project-cell">
        <img src="https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=800" class="project-img">
        <div class="project-label"><span>Nova Identity</span><span>2024</span></div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="project-cell" style="border-right:none;">
        <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800" class="project-img">
        <div class="project-label"><span>Tech Frontier</span><span>Branding</span></div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Projeto 3 e 4
st.markdown('<div class="project-block">', unsafe_allow_html=True)
col3, col4 = st.columns(2, gap="small")
with col3:
    st.markdown("""
    <div class="project-cell">
        <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800" class="project-img">
        <div class="project-label"><span>Abstract Forms</span><span>CGI</span></div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="project-cell" style="border-right:none;">
        <img src="https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?w=800" class="project-img">
        <div class="project-label"><span>L'Aube</span><span>Web Design</span></div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PHILOSOPHY SECTION ---
st.markdown("""
<div class="philosophy-section">
    We believe in the power of simple, functional, and unapologetic design. 
    Creating meaningful connections through digital interfaces that stand out 
    in a crowded world.
</div>
""", unsafe_allow_html=True)

# --- 5. SERVICES (GRID FINO) ---
st.markdown("""
<div class="project-block" style="padding: 60px 40px; font-weight: 700; text-transform: uppercase; font-size: 14px;">
    <div>
        <p style="color: #888; margin-bottom: 20px;">Capabilites</p>
        <p>Strategy / UX Design / UI Design / Web Development / Branding / Motion</p>
    </div>
    <div style="border-left: 1px solid #000; padding-left: 40px;">
        <p style="color: #888; margin-bottom: 20px;">Clientele</p>
        <p>Apple / Nike / Google / Local startups / International Brands</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div class="footer-container">
    <div class="footer-logo">B.</div>
    <div style="text-align: right; font-weight: 700; text-transform: uppercase; font-size: 12px; line-height: 2;">
        Let's work together<br>
        <span style="text-decoration: underline;">hello@wearebreakfast.com</span><br><br>
        Instagram / LinkedIn / Twitter
    </div>
</div>
<div style="padding: 20px 40px; border-top: 1px solid #000; font-size: 10px; font-weight: 700; text-transform: uppercase;">
    © 2026 Breakfast Studio — Crafted with precision.
</div>
""", unsafe_allow_html=True)
