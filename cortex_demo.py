import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Hugo Bazin | Digital Designer",
    page_icon="🕶️",
    layout="wide"
)

# --- CSS PARA DESIGN DE LUXO (HUGO BAZIN STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,400;1,400&display=swap');

    /* Reset de Background */
    .stApp {
        background-color: #f6f6f6;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1a1a1a;
    }

    /* Header Minimalista */
    .header-hugo {
        display: flex;
        justify-content: space-between;
        padding: 40px 5%;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Hero Section */
    .hero-container {
        padding: 100px 5% 150px 5%;
    }
    .hero-title {
        font-size: clamp(40px, 8vw, 120px);
        line-height: 0.9;
        font-weight: 400;
        letter-spacing: -2px;
        margin-bottom: 40px;
    }
    .hero-subtitle {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 24px;
        color: #666;
    }

    /* Grid de Projetos */
    .project-row {
        margin-bottom: 120px;
        padding: 0 5%;
    }
    .project-image {
        width: 100%;
        height: auto;
        border-radius: 4px;
        transition: opacity 0.4s;
    }
    .project-image:hover {
        opacity: 0.9;
    }
    .project-meta {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
        border-top: 1px solid #ddd;
        padding-top: 15px;
        font-size: 14px;
        font-weight: 500;
    }

    /* Seção de Texto (About) */
    .about-section {
        padding: 150px 20%;
        font-size: 28px;
        line-height: 1.4;
        text-align: left;
    }

    /* Footer */
    .footer-hugo {
        padding: 100px 5%;
        border-top: 1px solid #ddd;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        text-transform: uppercase;
        color: #999;
    }

    /* Custom Button (Invisible/Clean) */
    div.stButton > button {
        background: transparent;
        border: none;
        border-bottom: 1px solid #1a1a1a;
        color: #1a1a1a;
        border-radius: 0;
        padding: 0;
        font-weight: 600;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="header-hugo">
    <div>Hugo Bazin — Digital Designer</div>
    <div>Paris, FR — 14:52 PM</div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">CREATING DIGITAL<br>EXPERIENCES</div>
    <div class="hero-subtitle">Independent Designer & Art Director</div>
</div>
""", unsafe_allow_html=True)

# --- 3. LISTA DE PROJETOS (COMPRIDA) ---

def render_project(image_url, title, year, category):
    st.markdown(f"""
    <div class="project-row">
        <img src="{image_url}" class="project-image">
        <div class="project-meta">
            <div>{title}</div>
            <div style="color: #999;">{category} — {year}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Projeto 1
render_project(
    "https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?auto=format&fit=crop&w=1500&q=80",
    "L'Art de Vivre", "2024", "Visual Identity"
)

# Projeto 2
render_project(
    "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=1500&q=80",
    "Techno Frontier", "2023", "Product Design"
)

# Projeto 3
render_project(
    "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=1500&q=80",
    "Minimal Workspace", "2023", "CGI & Motion"
)

# Projeto 4
render_project(
    "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1500&q=80",
    "Essential Watch", "2022", "E-commerce"
)

# --- 4. ABOUT SECTION ---
st.markdown("""
<div class="about-section">
    Eu ajudo marcas a traduzirem sua essência em produtos digitais que as pessoas amam usar. Focado em simplicidade, estética e performance.
</div>
""", unsafe_allow_html=True)

# --- 5. CONTATO / LINKS ---
st.markdown('<div style="padding: 0 5% 100px 5%;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.button("EMAIL ME")
with col2:
    st.button("LINKEDIN")
with col3:
    st.button("DRIBBBLE")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div class="footer-hugo">
    <div>© 2024 Hugo Bazin</div>
    <div>Design & Development</div>
    <div>Back to Top ↑</div>
</div>
""", unsafe_allow_html=True)
