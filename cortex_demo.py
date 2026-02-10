import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Zajno Motion | Estúdio de Design Digital",
    page_icon="🎬",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (ZAJNO MOTION STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Reset e Fundo Profundo */
    .stApp {
        background-color: #0b0b0b;
        color: #ffffff;
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Estilo Zajno */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        -webkit-font-smoothing: antialiased;
    }

    /* Header Minimalista */
    .nav-zajno {
        display: flex;
        justify-content: space-between;
        padding: 40px 60px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        background: linear-gradient(180deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%);
    }

    /* Hero Section - A Estrela do Site */
    .hero-container {
        padding: 200px 60px 100px 60px;
    }
    
    .hero-title {
        font-size: clamp(40px, 12vw, 180px);
        font-weight: 900;
        line-height: 0.8;
        letter-spacing: -0.05em;
        text-transform: uppercase;
        margin-bottom: 60px;
    }

    /* Grid de Vídeos/Projetos */
    .project-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2px; /* Linha fina de separação */
        background-color: #1a1a1a; /* Cor da linha */
        border-top: 1px solid #1a1a1a;
        border-bottom: 1px solid #1a1a1a;
    }

    .project-item {
        background-color: #0b0b0b;
        padding: 40px;
        position: relative;
        overflow: hidden;
        aspect-ratio: 16 / 9;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }

    .project-thumb {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover;
        opacity: 0.4;
        transition: opacity 0.5s ease, transform 0.8s ease;
    }

    .project-item:hover .project-thumb {
        opacity: 0.8;
        transform: scale(1.05);
    }

    .project-meta {
        position: relative;
        z-index: 2;
    }

    .project-category {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #888;
        margin-bottom: 10px;
    }

    /* Rodapé High-Tech */
    .footer-zajno {
        padding: 100px 60px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        border-top: 1px solid #1a1a1a;
    }

    .big-footer-text {
        font-size: clamp(30px, 6vw, 80px);
        font-weight: 900;
        text-transform: uppercase;
        line-height: 0.9;
    }

    /* Botão Customizado */
    div.stButton > button {
        background: transparent;
        border: 1px solid #ffffff;
        color: #ffffff;
        border-radius: 0;
        padding: 15px 40px;
        text-transform: uppercase;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #ffffff;
        color: #0b0b0b;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-zajno">
    <div>Zajno / Motion</div>
    <div style="display: flex; gap: 40px;">
        <span>Trabalhos</span>
        <span>Estúdio</span>
        <span>Contato</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">
        MOVIMENTO<br>É A NOSSA<br>LINGUAGEM
    </div>
    <div style="max-width: 500px; color: #888; font-size: 16px; line-height: 1.6;">
        Somos um estúdio de design focado em criar experiências digitais que ganham vida através do movimento e da tecnologia de ponta.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. SHOWCASE DE PROJETOS (GRID DUPLO) ---
st.markdown('<div class="project-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")

with col1:
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800" class="project-thumb">
        <div class="project-meta">
            <p class="project-category">Motion Graphics / 2024</p>
            <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Cyber Identity</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=800" class="project-thumb">
        <div class="project-meta">
            <p class="project-category">Interface Design / 2023</p>
            <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Liquid UI</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=800" class="project-thumb">
        <div class="project-meta">
            <p class="project-category">Art Direction / 2024</p>
            <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Astro Forms</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800" class="project-thumb">
        <div class="project-meta">
            <p class="project-category">3D Animation / 2024</p>
            <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Glass Echo</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SEÇÃO DE TEXTO MANIFESTO (COMPRIDA) ---
st.markdown("""
<div style="padding: 150px 60px; border-bottom: 1px solid #1a1a1a;">
    <div style="max-width: 900px;">
        <h2 style="font-size: 50px; font-weight: 900; text-transform: uppercase; line-height: 1;">
            Nós não apenas movemos pixels. Nós contamos histórias que definem o futuro das marcas.
        </h2>
        <p style="margin-top: 40px; color: #888; font-size: 20px;">
            Trabalhamos com marcas audaciosas para transformar ideias complexas em interações digitais simples, memoráveis e impactantes.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER (CALL TO ACTION) ---
st.markdown("""
<div class="footer-zajno">
    <div>
        <p style="color: #888; text-transform: uppercase; font-size: 10px; letter-spacing: 2px; margin-bottom: 20px;">Pronto para elevar sua marca?</p>
        <div class="big-footer-text">VAMOS<br>CRIAR JUNTOS</div>
    </div>
    <div style="text-align: right;">
        <p style="margin-bottom: 30px; color: #888;">studio@zajno.com</p>
    </div>
</div>
""", unsafe_allow_html=True)

col_btn_1, col_btn_2 = st.columns([1, 4])
with col_btn_1:
    st.markdown('<div style="padding-left: 60px; padding-bottom: 100px;">', unsafe_allow_html=True)
    st.button("Iniciar Projeto")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FINALIZAÇÃO ---
st.markdown("""
<div style="padding: 40px 60px; font-size: 10px; color: #444; border-top: 1px solid #1a1a1a; text-transform: uppercase; letter-spacing: 1px;">
    © 2026 Zajno Studio — São Francisco / Remoto
</div>
""", unsafe_allow_html=True)
