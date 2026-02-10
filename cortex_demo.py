import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Breakfast | Digital Design Agency",
    page_icon="🍳",
    layout="wide"
)

# --- CSS PARA DESIGN BRUTALISTA (BREAKFAST STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Reset e Fundo */
    .stApp {
        background-color: #ffffff;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #000000;
        line-height: 1.2;
    }

    /* Header Estilo Breakfast */
    .header-bf {
        display: flex;
        justify-content: space-between;
        padding: 30px 5%;
        border-bottom: 1px solid #000;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 14px;
        letter-spacing: 1px;
    }

    /* Hero Section - Tipografia Massiva */
    .hero-bf {
        padding: 100px 5%;
        border-bottom: 1px solid #000;
    }
    .hero-text {
        font-size: clamp(40px, 10vw, 150px);
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -4px;
        line-height: 0.85;
    }

    /* Grid de Projetos */
    .project-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        border-bottom: 1px solid #000;
    }
    
    .grid-item {
        border-right: 1px solid #000;
        padding: 0;
        transition: all 0.5s ease;
    }
    
    .grid-item:last-child {
        border-right: none;
    }

    .project-info {
        padding: 20px;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 13px;
        display: flex;
        justify-content: space-between;
    }

    /* Seções de Texto (Filosofia) */
    .text-section {
        padding: 120px 5%;
        font-size: 42px;
        font-weight: 700;
        border-bottom: 1px solid #000;
    }

    /* Footer Brutalista */
    .footer-bf {
        padding: 100px 5%;
        background-color: #000;
        color: #fff;
    }

    /* Botão Invisível Customizado */
    div.stButton > button {
        background: transparent;
        border: 1px solid #000;
        color: #000;
        border-radius: 0;
        font-weight: 700;
        text-transform: uppercase;
        padding: 20px 40px;
        width: 100%;
    }
    div.stButton > button:hover {
        background: #000;
        color: #fff;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="header-bf">
    <div>Breakfast.</div>
    <div>Design & Technology</div>
    <div>Menu +</div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-bf">
    <div class="hero-text">WE DESIGN<br>DIGITAL<br>EXPERIENCES</div>
</div>
""", unsafe_allow_html=True)

# --- 3. PROJETOS (GRID COMPRIDA) ---

def breakfast_project(col, img_url, name, client):
    with col:
        st.markdown(f"""
        <div style="border-bottom: 1px solid #000;">
            <img src="{img_url}" style="width:100%; filter: grayscale(100%) contrast(1.1); display:block;">
            <div class="project-info">
                <span>{name}</span>
                <span style="color: #888;">{client}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="small")
breakfast_project(c1, "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800", "Solar System", "Editorial")
breakfast_project(c2, "https://images.unsplash.com/photo-1547658719-da2b51169166?w=800", "Neon Future", "Web Design")

c3, c4 = st.columns(2, gap="small")
breakfast_project(c3, "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "Cyber Identity", "Branding")
breakfast_project(c4, "https://images.unsplash.com/photo-1509343256512-d77a5cb3791b?w=800", "Monochrome Studio", "CGI")

# --- 4. SEÇÃO DE FILOSOFIA (TEXTO COMPRIDO) ---
st.markdown("""
<div class="text-section">
    Independent studio for strategy, design and code. We turn complex ideas into simple, functional and beautiful digital products.
</div>
""", unsafe_allow_html=True)

# --- 5. SERVIÇOS EM LISTA ---
st.markdown('<div style="padding: 80px 5%; border-bottom: 1px solid #000;">', unsafe_allow_html=True)
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.markdown("### STRATEGY")
    st.write("Product Discovery / User Research / Brand Positioning")
with col_s2:
    st.markdown("### DESIGN")
    st.write("UI/UX Design / Visual Identity / Motion Graphics")
with col_s3:
    st.markdown("### CODE")
    st.write("React / Webflow / Headless CMS / E-commerce")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. CTA / CONTATO ---
st.markdown('<div style="padding: 100px 5%;">', unsafe_allow_html=True)
st.markdown("<h2 style='font-size: 80px; font-weight: 900; margin-bottom: 40px;'>LET'S TALK?</h2>", unsafe_allow_html=True)
st.button("Start a Project")
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("""
<div class="footer-bf">
    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
        <div>
            <h2 style="font-size: 40px; margin-bottom: 20px;">Breakfast.</h2>
            <p>Rua de Trás, Porto, Portugal<br>hello@wearebreakfast.com</p>
        </div>
        <div style="text-align: right; font-size: 12px; opacity: 0.6;">
            INSTAGRAM / LINKEDIN / TWITTER<br>
            © 2024 ALL RIGHTS RESERVED
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
