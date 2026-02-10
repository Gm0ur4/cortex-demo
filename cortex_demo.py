import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dockyard Social | Comida, Bebida & Vibe",
    page_icon="🍔",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (STREET FOOD STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=Oswald:wght@700&display=swap');

    /* Variáveis de Cor */
    :root {
        --dock-yellow: #ffcc00;
        --dock-black: #111111;
        --dock-white: #f4f4f4;
    }

    .stApp {
        background-color: var(--dock-white);
    }

    /* Tipografia Brutalista */
    h1, h2, h3, .impact-font {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: -1px;
        line-height: 0.9;
    }

    /* Header Estilo Galpão */
    .nav-dock {
        background-color: var(--dock-black);
        color: var(--dock-yellow);
        padding: 15px 5%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
        z-index: 1000;
    }

    /* Hero Section - A Grande Chamada */
    .hero-dock {
        background-color: var(--dock-yellow);
        padding: 80px 5%;
        border-bottom: 8px solid var(--dock-black);
        text-align: left;
    }

    .hero-h1 {
        font-size: clamp(60px, 12vw, 150px);
        color: var(--dock-black);
    }

    /* Cards de Eventos/Comida */
    .dock-card {
        background: var(--dock-black);
        color: white;
        padding: 0;
        border-radius: 0px;
        transition: 0.3s;
        height: 100%;
        border: 4px solid var(--dock-black);
    }
    
    .dock-card:hover {
        transform: rotate(-1deg);
        border-color: var(--dock-yellow);
    }

    .card-content {
        padding: 25px;
    }

    /* Botão Industrial */
    div.stButton > button {
        background-color: var(--dock-black);
        color: var(--dock-yellow);
        border-radius: 0;
        padding: 20px 40px;
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        border: none;
        width: 100%;
        text-transform: uppercase;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background-color: #333;
        color: white;
    }

    /* Marquee / Fita de Aviso */
    .announcement {
        background: var(--dock-black);
        color: white;
        padding: 10px;
        font-weight: bold;
        text-align: center;
        letter-spacing: 2px;
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. AVISO E NAVEGAÇÃO ---
st.markdown('<div class="announcement">ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO</div>', unsafe_allow_html=True)
st.markdown("""
<div class="nav-dock">
    <div style="font-size: 32px; font-family: 'Oswald'; font-weight: 700;">DOCKYARD SOCIAL</div>
    <div style="display: flex; gap: 30px; font-size: 14px; font-weight: bold;">
        <span>O QUE ROLA</span>
        <span>COMIDA</span>
        <span>BEBIDA</span>
        <span>RESERVAR</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown('<div class="hero-dock">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-h1">COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: 900; color: #111; margin-top: 20px;">O melhor mercado de comida de rua de Glasgow, agora na sua tela.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. GRID DE CONTEÚDO ---
st.write("")
col1, col2, col3 = st.columns(3)

def render_dock_card(col, title, subtitle, img_url):
    with col:
        st.markdown(f"""
        <div class="dock-card">
            <img src="{img_url}" style="width:100%; filter: grayscale(20%);">
            <div class="card-content">
                <h2 style="font-size: 40px; margin-bottom: 5px;">{title}</h2>
                <p style="color: var(--dock-yellow); font-weight: bold; letter-spacing: 1px;">{subtitle}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"VER {title}", key=title)

render_dock_card(col1, "COMIDA", "10+ VENDEDORES", "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600")
render_dock_card(col2, "BEBIDA", "CRAFT BEER & COCKTAILS", "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600")
render_dock_card(col3, "EVENTOS", "MÚSICA AO VIVO", "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600")

# --- 4. SEÇÃO "SOBRE" BRUTALISTA ---
st.markdown("""
<div style="background-color: #111; color: white; padding: 100px 5%; margin-top: 50px;">
    <div style="max-width: 800px;">
        <h2 style="font-size: 60px; color: var(--dock-yellow); margin-bottom: 30px;">MAIS QUE UM MERCADO.</h2>
        <p style="font-size: 24px; line-height: 1.4; font-weight: 300;">
            A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos. 
            Nós apoiamos talentos locais, reduzimos o desperdício e garantimos que a única coisa 
            quente por aqui (além da comida) seja a hospitalidade.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div style="padding: 60px 5%; background: var(--dock-yellow); color: #111;">
    <div style="display: flex; justify-content: space-between; align-items: flex-end;">
        <div>
            <h2 style="font-size: 40px;">DOCKYARD.</h2>
            <p>952 South St, Glasgow G14 0BX</p>
        </div>
        <div style="text-align: right; font-weight: bold;">
            INSTAGRAM / FACEBOOK / TIKTOK<br>
            HELLO@DOCKYARDSOCIAL.COM
        </div>
    </div>
    <div style="margin-top: 40px; border-top: 2px solid #111; padding-top: 20px; font-size: 12px; font-weight: bold;">
        © 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO.
    </div>
</div>
""", unsafe_allow_html=True)
