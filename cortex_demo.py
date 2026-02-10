import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="TinyTracks | Memórias Felizes para Crianças",
    page_icon="👶",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (TINYTRACKS STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Quicksand:wght@400;700&display=swap');

    /* Cores e Fundo */
    :root {
        --tiny-purple: #9d8df1;
        --tiny-blue: #a0d2eb;
        --tiny-pink: #ffafcc;
        --tiny-yellow: #ffee93;
        --tiny-bg: #fdfcf0;
    }

    .stApp {
        background-color: var(--tiny-bg);
        color: #4a4a4a;
    }

    /* Tipografia Arredondada */
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Fredoka', sans-serif;
        color: #2d2d2d;
    }

    /* Navegação Soft */
    .nav-tiny {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 8%;
        background: transparent;
    }
    .logo-tiny {
        font-family: 'Fredoka', sans-serif;
        font-size: 28px;
        color: var(--tiny-purple);
        font-weight: 600;
    }

    /* Hero Section - Acolhedor */
    .hero-tiny {
        padding: 60px 8%;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .hero-h1 {
        font-size: clamp(40px, 6vw, 70px);
        line-height: 1.1;
        margin-bottom: 25px;
    }

    /* Botão Bolha */
    div.stButton > button {
        background-color: var(--tiny-purple);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-family: 'Fredoka', sans-serif;
        font-size: 18px;
        box-shadow: 0 4px 15px rgba(157, 141, 241, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #8a7ae0;
        box-shadow: 0 6px 20px rgba(157, 141, 241, 0.6);
    }

    /* Cards de Recursos */
    .feature-card {
        background: white;
        border-radius: 30px;
        padding: 30px;
        text-align: center;
        border: 2px solid #f0f0f0;
        transition: 0.3s;
        height: 100%;
    }
    .feature-card:hover {
        border-color: var(--tiny-blue);
        transform: translateY(-5px);
    }

    .icon-box {
        width: 60px;
        height: 60px;
        border-radius: 20px;
        margin: 0 auto 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-tiny">
    <div class="logo-tiny">🐾 tinytracks</div>
    <div style="display: flex; gap: 30px; font-weight: 700; color: #666; font-size: 14px;">
        <span>Como funciona</span>
        <span>Preços</span>
        <span>Login</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown('<div class="hero-tiny">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-h1">Capture cada passo <br><span style="color: #9d8df1;">da jornada deles.</span></h1>', unsafe_allow_html=True)
st.markdown('<p style="max-width: 600px; font-size: 18px; color: #777; margin-bottom: 40px;">O TinyTracks ajuda você a organizar fotos, vídeos e marcos do crescimento dos seus filhos em um diário digital seguro e privado.</p>', unsafe_allow_html=True)
st.button("Começar Grátis")
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. ILUSTRAÇÃO HERO (SIMULADA COM IMAGEM SOFT) ---
st.image("https://images.unsplash.com/photo-1510333300262-213217d29407?w=1200", use_container_width=True)

# --- 4. GRID DE RECURSOS ---
st.markdown('<div style="padding: 100px 8%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; margin-bottom: 60px; font-size: 36px;">Feito para pais ocupados</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

def render_feature(col, icon, title, desc, color):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="icon-box" style="background-color: {color};">{icon}</div>
            <h3 style="margin-bottom: 15px;">{title}</h3>
            <p style="color: #888; font-size: 15px; line-height: 1.6;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

render_feature(col1, "📸", "Upload Inteligente", "Organize fotos automaticamente por idade e data.", "#e0f2fe")
render_feature(col2, "🔒", "Privacidade Total", "Seu diário é criptografado e só você decide quem pode ver.", "#fef3c7")
render_feature(col3, "📅", "Marcos Importantes", "Nunca esqueça a primeira palavra ou o primeiro passo.", "#fce7f3")

st.markdown('</div>', unsafe_allow_html=True)

# --- 5. SEÇÃO DE FECHAMENTO ---
st.markdown("""
<div style="background-color: #9d8df1; padding: 80px 8%; text-align: center; border-radius: 50px; margin: 0 8% 100px 8%; color: white;">
    <h2 style="color: white; font-size: 40px; margin-bottom: 20px;">Pronto para criar sua primeira trilha?</h2>
    <p style="margin-bottom: 40px; opacity: 0.9;">Junte-se a mais de 50.000 famílias que guardam suas memórias conosco.</p>
</div>
""", unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div style="padding: 60px 8% 40px 8%; border-top: 2px solid #f0f0f0; text-align: center;">
    <div style="font-family: 'Fredoka'; font-size: 24px; color: #9d8df1; margin-bottom: 20px;">tinytracks</div>
    <div style="display: flex; justify-content: center; gap: 40px; font-size: 14px; color: #999;">
        <span>Instagram</span>
        <span>Privacidade</span>
        <span>Suporte</span>
    </div>
    <p style="margin-top: 40px; font-size: 12px; color: #ccc;">© 2026 TinyTracks App. Feito com amor para famílias.</p>
</div>
""", unsafe_allow_html=True)
