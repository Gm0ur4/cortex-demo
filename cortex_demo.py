import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="PAIX | Estúdio de Design e Arquitetura",
    page_icon="🏛️",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (PAIX AESTHETIC) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Inter:wght@200;400&display=swap');

    /* Reset e Cores Base */
    .stApp {
        background-color: #f7f7f7; /* Tom de pedra suave */
        color: #1a1a1a;
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia PAIX */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 0.05em;
    }

    h1, h2, .serif-light {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 300;
        font-size: 48px;
        line-height: 1.1;
    }

    /* Navegação Estilo PAIX */
    .nav-paix {
        display: flex;
        justify-content: space-between;
        padding: 50px 5%;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    /* Hero Section */
    .hero-paix {
        padding: 100px 5% 150px 5%;
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 100px;
    }

    /* Grid de Projetos */
    .project-section {
        padding: 0 5% 200px 5%;
    }

    .project-card {
        margin-bottom: 250px;
        transition: opacity 0.6s ease;
    }
    
    .project-img {
        width: 100%;
        filter: grayscale(10%) contrast(1.05);
        margin-bottom: 25px;
    }

    .project-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 32px;
        border-bottom: 1px solid #ddd;
        padding-bottom: 15px;
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .project-year {
        font-size: 10px;
        font-family: 'Inter', sans-serif;
        letter-spacing: 2px;
        color: #888;
    }

    /* Footer */
    .footer-paix {
        padding: 100px 5%;
        border-top: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        font-size: 10px;
        letter-spacing: 2px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-paix">
    <div style="font-weight: 400;">PAIX DESIGN</div>
    <div style="display: flex; gap: 50px;">
        <span>Projetos</span>
        <span>Escritório</span>
        <span>Contato</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-paix">
    <div>
        <p style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #888; margin-bottom: 30px;">
            Arquitetura & Design de Interiores
        </p>
        <h1 class="serif-light">
            A beleza reside na <br>
            intenção e na calma.
        </h1>
    </div>
    <div style="font-size: 16px; line-height: 1.8; padding-top: 10px; color: #555;">
        PAIX é um estúdio de design focado na criação de espaços que transcendem o tempo. 
        Nossa abordagem é guiada pela pureza dos materiais e pela harmonia entre a luz natural e a forma construída.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. PROJETOS (LAYOUT LARGO) ---

def render_paix_project(title, location, year, img_url, alignment="left"):
    # Alterna o layout das colunas dependendo do alinhamento desejado
    col_size = [1, 2] if alignment == "left" else [2, 1]
    
    st.markdown(f"""
    <div class="project-section">
        <div class="project-card">
            <img src="{img_url}" class="project-img">
            <div class="project-title">
                <span>{title} — {location}</span>
                <span class="project-year">{year}</span>
            </div>
            <p style="font-size: 12px; color: #999; text-transform: uppercase; letter-spacing: 1px;">
                Residencial / Design de Mobiliário
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Projeto 01
render_paix_project(
    "Casa Minimalista", 
    "Sintra", 
    "2024", 
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600"
)

# Projeto 02
render_paix_project(
    "Apartamento Galeria", 
    "Porto", 
    "2023", 
    "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600"
)

# --- 4. SEÇÃO SOBRE (TRANSICIONAL) ---
st.markdown("""
<div style="padding: 150px 20% 250px 20%; text-align: center;">
    <h2 class="serif-light" style="font-size: 56px; margin-bottom: 40px;">Atmosferas Tangíveis</h2>
    <p style="color: #666; line-height: 2;">
        Trabalhamos em estreita colaboração com artesãos locais para garantir que cada detalhe, 
        desde a textura da parede até o encaixe da madeira, conte uma história de autenticidade e respeito ao ambiente.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div class="footer-paix">
    <div>
        PAIX DESIGN STUDIO<br>
        AVENIDA DA LIBERDADE, LISBOA
    </div>
    <div style="text-align: right;">
        INSTAGRAM / BEHANCE / LINKEDIN<br>
        HELLO@PAIX-DESIGN.COM
    </div>
</div>
<div style="padding: 30px 5%; font-size: 9px; color: #bbb; letter-spacing: 1px;">
    © 2026 PAIX DESIGN. TODOS OS DIREITOS RESERVADOS.
</div>
""", unsafe_allow_html=True)
