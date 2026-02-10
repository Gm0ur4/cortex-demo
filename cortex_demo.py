import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Memphis Zoo | Experience the Wild",
    page_icon="🦁",
    layout="wide"
)

# --- CSS PERSONALIZADO (MEMPHIS ZOO STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* Remove padding padrão do Streamlit */
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Overlay Header */
    .zoo-header {
        position: absolute;
        top: 0;
        width: 100%;
        z-index: 1000;
        padding: 20px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(0,0,0,0.2);
    }
    
    .logo-zoo {
        color: white;
        font-weight: 900;
        font-size: 32px;
        letter-spacing: -1px;
    }

    /* Hero Banner */
    .hero-video-bg {
        height: 100vh;
        background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
    }

    /* Floating Action Buttons */
    .action-bar {
        display: flex;
        gap: 10px;
        margin-top: 30px;
    }
    
    /* Estilo dos Botões do Zoo */
    div.stButton > button {
        border-radius: 0px;
        font-weight: 700;
        text-transform: uppercase;
        padding: 15px 30px;
        border: none;
        letter-spacing: 1px;
    }
    
    /* Botão Laranja (Tickets) */
    .ticket-btn > div > button {
        background-color: #f37021 !important;
        color: white !important;
    }
    
    /* Seções de Conteúdo */
    .info-section {
        padding: 80px 10%;
        text-align: center;
    }
    
    .green-bg { background-color: #004a26; color: white; }
    .sand-bg { background-color: #f9f7f2; color: #333; }

    /* Cards de Animais */
    .animal-card {
        background: white;
        border-radius: 0px;
        overflow: hidden;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .animal-card img { width: 100%; height: 250px; object-fit: cover; }
    .animal-info { padding: 20px; text-align: left; }
    
    /* Footer */
    .footer-zoo {
        background-color: #1a1a1a;
        color: white;
        padding: 60px 10%;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER & HERO ---
st.markdown("""
<div class="zoo-header">
    <div class="logo-zoo">MEMPHIS ZOO</div>
    <div style="display: flex; gap: 20px; color: white; font-weight: 700; font-size: 14px;">
        <span>ANIMALS</span>
        <span>EXHIBITS</span>
        <span>EDUCATION</span>
        <span>CONSERVATION</span>
    </div>
</div>
<div class="hero-video-bg">
    <h1 style="font-size: 80px; font-weight: 900; margin-bottom: 0;">ADVENTURE AWAITS</h1>
    <p style="font-size: 24px; font-weight: 400;">Explore o mundo selvagem no coração de Memphis.</p>
</div>
""", unsafe_allow_html=True)

# --- 2. BARRA DE BOTÕES RÁPIDOS ---
c_btn1, c_btn2, c_btn3 = st.columns(3)
with c_btn1:
    st.markdown('<div class="ticket-btn">', unsafe_allow_html=True)
    st.button("BUY TICKETS", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with c_btn2:
    st.button("BECOME A MEMBER", use_container_width=True)
with c_btn3:
    st.button("DONATE TODAY", use_container_width=True)

# --- 3. SEÇÃO: PROGRAME SUA VISITA ---
st.markdown('<div class="info-section sand-bg">', unsafe_allow_html=True)
st.markdown("<h2 style='font-weight:900; color:#004a26;'>PLANEJE SUA VISITA</h2>", unsafe_allow_html=True)
st.write("Estamos abertos diariamente das 9h às 17h. Venha ver nossos novos filhotes!")

col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    st.markdown("### 🕒 Horários")
    st.write("Seg - Dom: 09:00 - 17:00")
with col_v2:
    st.markdown("### 📍 Localização")
    st.write("2000 Prentiss Pl, Memphis, TN")
with col_v3:
    st.markdown("### 🗺️ Mapa do Zoo")
    st.button("BAIXAR MAPA")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SEÇÃO: NOSSOS ANIMAIS (CARDS) ---
st.markdown('<div class="info-section">', unsafe_allow_html=True)
st.markdown("<h2 style='font-weight:900; margin-bottom:40px;'>CONHEÇA OS RESIDENTES</h2>", unsafe_allow_html=True)

def animal_card(col, img, name, category):
    with col:
        st.markdown(f"""
        <div class="animal-card">
            <img src="{img}">
            <div class="animal-info">
                <span style="color:#f37021; font-weight:700; font-size:12px;">{category}</span>
                <h3 style="margin:5px 0;">{name}</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Saber mais sobre {name}", key=name)

ca1, ca2, ca3 = st.columns(3)
animal_card(ca1, "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?w=500", "Leão Africano", "FELINOS")
animal_card(ca2, "https://images.unsplash.com/photo-1544860707-c352cc5a92e3?w=500", "Panda Gigante", "ÁSIA")
animal_card(ca3, "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd?w=500", "Girafa Reticulada", "SAVANA")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. SEÇÃO: CONSERVAÇÃO (GREEN BG) ---
st.markdown('<div class="info-section green-bg">', unsafe_allow_html=True)
st.markdown("""
    <h2 style='font-weight:900;'>SALVANDO ESPÉCIES NO MUNDO TODO</h2>
    <p style='max-width:800px; margin: 20px auto; font-size:18px;'>
        O Memphis Zoo é líder em pesquisa e conservação. Desde a reintrodução de sapos raros até a proteção de habitats na África, seu ingresso faz a diferença.
    </p>
""", unsafe_allow_html=True)
st.button("VEJA NOSSO IMPACTO", key="impact")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. EVENTOS E NOTÍCIAS ---
st.markdown('<div class="info-section sand-bg">', unsafe_allow_html=True)
col_e1, col_e2 = st.columns(2)
with col_e1:
    st.image("https://images.unsplash.com/photo-1502675135487-e971002a6adb?w=600")
with col_e2:
    st.markdown("<div style='text-align:left; padding-top:20px;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-weight:900;'>NOITE NO ZOO</h2>", unsafe_allow_html=True)
    st.write("Participe de nossos eventos noturnos exclusivos para famílias. Jantares temáticos, tours guiados sob o luar e muito mais.")
    st.button("VER CALENDÁRIO DE EVENTOS")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("""
<div class="footer-zoo">
    <div style="display:grid; grid-template-columns: 2fr 1fr 1fr; gap:50px;">
        <div>
            <h2 style="font-weight:900;">MEMPHIS ZOO</h2>
            <p>Conectando pessoas aos animais através de experiências memoráveis.</p>
        </div>
        <div>
            <h4>EXPLORE</h4>
            <p style="font-size:13px; line-height:2;">Animais<br>Experiências<br>Membros</p>
        </div>
        <div>
            <h4>SUPORTE</h4>
            <p style="font-size:13px; line-height:2;">Doar<br>Voluntários<br>Trabalhe Conosco</p>
        </div>
    </div>
    <div style="text-align:center; margin-top:50px; border-top: 1px solid #444; padding-top:20px; font-size:12px; color:#888;">
        © 2024 Memphis Zoo. Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
