import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="LITIGUARD | Excellence in Legal Services",
    page_icon="⚖️",
    layout="wide"
)

# --- CSS PARA ESTILO JURÍDICO EUROPEU (LITIGUARD) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');

    /* Reset e Cores Base */
    .stApp {
        background-color: #ffffff;
    }
    
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #1a2b3c; /* Azul Marinho Profundo */
    }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
    }

    /* Top Bar e Header */
    .top-bar {
        background-color: #1a2b3c;
        color: #c5a059; /* Dourado Litiguard */
        padding: 10px 8%;
        font-size: 12px;
        display: flex;
        justify-content: space-between;
        margin: -5rem -5rem 0 -5rem;
    }

    .nav-litiguard {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px 8%;
        background: white;
        border-bottom: 1px solid #eee;
        margin: 0 -5rem 0 -5rem;
    }

    /* Hero Section */
    .hero-litiguard {
        height: 600px;
        background-image: linear-gradient(rgba(26, 43, 60, 0.7), rgba(26, 43, 60, 0.7)), 
                          url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
        margin: 0 -5rem 80px -5rem;
    }

    /* Cards de Serviços */
    .service-card {
        padding: 40px;
        border: 1px solid #eee;
        transition: all 0.3s ease;
        height: 100%;
    }
    .service-card:hover {
        background-color: #1a2b3c;
        color: white;
        border-color: #1a2b3c;
    }
    .service-icon {
        color: #c5a059;
        font-size: 40px;
        margin-bottom: 20px;
    }

    /* Seções de Texto Compridas */
    .section-box {
        padding: 100px 15%;
        border-bottom: 1px solid #eee;
    }

    /* Botões */
    div.stButton > button {
        background-color: #c5a059;
        color: white;
        border-radius: 0;
        border: none;
        padding: 15px 40px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. TOP BAR & NAV ---
st.markdown("""
<div class="top-bar">
    <div>LITIGATION & ADVISORY SERVICES</div>
    <div>EN | FR | DE</div>
</div>
<div class="nav-litiguard">
    <div style="font-size: 28px; font-weight: 700; letter-spacing: 3px;">LITIGUARD</div>
    <div style="display: flex; gap: 40px; font-size: 13px; font-weight: 600;">
        <span>ABOUT</span>
        <span>SERVICES</span>
        <span>NETWORK</span>
        <span>CONTACT</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-litiguard">
    <h1 style="font-size: 60px; margin-bottom: 20px;">Protecting Your Interests</h1>
    <p style="font-size: 20px; max-width: 700px; font-weight: 300;">
        A global network of legal experts dedicated to complex litigation and strategic advisory.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. ABOUT (SECTION 1) ---
st.markdown('<div class="section-box">', unsafe_allow_html=True)
c_about1, c_about2 = st.columns([1, 1])
with c_about1:
    st.markdown("<h2 style='font-size: 40px;'>Strategic Legal<br>Representation</h2>", unsafe_allow_html=True)
with c_about2:
    st.write("""
    Litiguard provides comprehensive support in cross-border disputes. 
    Our approach combines local expertise with a global perspective to ensure 
    the best possible outcome for institutional and private clients.
    """)
    st.button("Discover Our Vision")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SERVICES (GRID) ---
st.markdown('<div class="section-box" style="background-color: #fcfcfc;">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 60px;'>Our Expertise</h2>", unsafe_allow_html=True)

def service_box(col, icon, title, text):
    with col:
        st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon}</div>
            <h3 style="margin-bottom: 15px;">{title}</h3>
            <p style="font-size: 14px; opacity: 0.8;">{text}</p>
        </div>
        """, unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
service_box(s1, "⚖️", "Commercial Litigation", "Resolving complex business disputes with precision and strategic foresight.")
service_box(s2, "🌍", "Cross-Border Claims", "Navigating multiple jurisdictions to protect assets and enforce rights worldwide.")
service_box(s3, "🤝", "Arbitration", "Expert representation in international arbitration proceedings and alternative dispute resolution.")

st.markdown("<br>", unsafe_allow_html=True)

s4, s5, s6 = st.columns(3)
service_box(s4, "🛡️", "Asset Recovery", "Tracing and recovering assets across global financial centers and tax havens.")
service_box(s5, "📈", "Investment Disputes", "Protecting investors' rights under bilateral treaties and international law.")
service_box(s6, "📜", "Corporate Advisory", "Proactive legal strategies to mitigate risk and ensure regulatory compliance.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. NETWORK SECTION (BANNER COMPRIDO) ---
st.markdown("""
<div style="background-color: #1a2b3c; color: white; padding: 120px 8%; text-align: center; margin: 0 -5rem;">
    <h2 style="font-size: 45px; margin-bottom: 30px;">A Truly Global Presence</h2>
    <p style="max-width: 800px; margin: 0 auto 40px auto; font-size: 18px; opacity: 0.8;">
        Our network spans over 40 countries, providing seamless legal support 
        whenever and wherever our clients need it most.
    </p>
    <div style="display: flex; justify-content: center; gap: 80px; font-weight: 700; color: #c5a059;">
        <div>LONDON</div>
        <div>BRUSSELS</div>
        <div>ZURICH</div>
        <div>DUBAI</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("""
<div style="background-color: #f4f4f4; padding: 80px 8% 40px 8%; margin: 0 -5rem -5rem -5rem; border-top: 5px solid #c5a059;">
    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 100px;">
        <div>
            <h3 style="letter-spacing: 2px;">LITIGUARD</h3>
            <p style="font-size: 13px; margin-top: 20px;">International Litigation & Advisory Support Network.</p>
        </div>
        <div>
            <h4 style="font-size: 14px; color: #1a2b3c;">OFFICES</h4>
            <p style="font-size: 12px; line-height: 2;">Brussels, Belgium<br>Geneva, Switzerland<br>London, UK</p>
        </div>
        <div>
            <h4 style="font-size: 14px; color: #1a2b3c;">LEGAL</h4>
            <p style="font-size: 12px; line-height: 2;">Privacy Policy<br>Terms of Service<br>Cookies</p>
        </div>
    </div>
    <div style="text-align: center; margin-top: 60px; font-size: 11px; color: #999;">
        © 2026 LITIGUARD. ALL RIGHTS RESERVED.
    </div>
</div>
""", unsafe_allow_html=True)
