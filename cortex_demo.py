import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Fundable | Plataforma de Crowdfunding",
    page_icon="🚀",
    layout="wide"
)

# --- CSS PARA ESTILO FUNDABLE (BUSINESS & FUNDING) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Open Sans', sans-serif;
    }

    /* Header com Degradê */
    .header-fundable {
        background: linear-gradient(90deg, #1a2a3a 0%, #2c3e50 100%);
        padding: 20px 5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: -5rem -5rem 2rem -5rem;
        color: white;
    }
    
    .logo {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -1px;
    }
    .logo span { color: #00a8ff; }

    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 60px 0;
        background-color: #f8f9fa;
        border-bottom: 1px solid #dee2e6;
        margin-bottom: 40px;
    }

    /* Cards de Projetos */
    .project-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 0px;
        margin-bottom: 20px;
    }
    .project-content {
        padding: 20px;
    }
    .project-title {
        font-size: 18px;
        font-weight: 700;
        color: #333;
    }
    .project-location {
        font-size: 12px;
        color: #888;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    /* Barra de Progresso Customizada */
    .progress-bg {
        background-color: #eee;
        height: 8px;
        border-radius: 4px;
        margin: 15px 0;
    }
    .progress-fill {
        background-color: #00a8ff;
        height: 8px;
        border-radius: 4px;
    }

    /* Labels de Investimento */
    .fund-label {
        font-size: 13px;
        color: #666;
    }
    .fund-value {
        font-weight: 700;
        color: #333;
    }

    /* Botões do Fundable */
    div.stButton > button {
        border-radius: 3px;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .btn-invest > div > button {
        background-color: #00a8ff !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="header-fundable">
    <div class="logo">FUND<span>ABLE</span></div>
    <div style="display: flex; gap: 30px; font-size: 14px; font-weight: 600;">
        <span>COMO FUNCIONA</span>
        <span>BROWSE STARTUPS</span>
        <span>LOGIN</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <h1 style="font-size: 48px; color: #1a2a3a;">Levante capital para o seu negócio</h1>
    <p style="font-size: 20px; color: #555; max-width: 700px; margin: 20px auto;">
        A maior rede de financiamento para empresas. Conectamos fundadores a investidores para lançar grandes ideias.
    </p>
</div>
""", unsafe_allow_html=True)

col_h1, col_h2 = st.columns(2)
with col_h1:
    st.markdown('<div style="text-align: right; padding-right: 20px;">', unsafe_allow_html=True)
    st.button("QUERO CAPTAR RECURSOS", use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)
with col_h2:
    st.markdown('<div class="btn-invest">', unsafe_allow_html=True)
    st.button("QUERO INVESTIR", use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- 3. STARTUPS EM DESTAQUE ---
st.subheader("Startups em Destaque")

def startup_card(col, img, title, loc, desc, percent, raised):
    with col:
        st.markdown(f"""
        <div class="project-card">
            <img src="{img}" style="width:100%; height:200px; object-fit:cover;">
            <div class="project-content">
                <div class="project-location">{loc}</div>
                <div class="project-title">{title}</div>
                <p style="font-size: 14px; color: #666; height: 60px;">{desc}</p>
                <div class="progress-bg"><div class="progress-fill" style="width: {percent}%;"></div></div>
                <div style="display: flex; justify-content: space-between;">
                    <div class="fund-label">Arrecadado<br><span class="fund-value">R$ {raised}</span></div>
                    <div class="fund-label" style="text-align: right;">Meta<br><span class="fund-value">{percent}%</span></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Ver Projeto: {title}", key=title)

c1, c2, c3 = st.columns(3)

startup_card(c1, 
             "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=500&q=80",
             "EcoTech Solutions", "SÃO PAULO, SP", 
             "Tecnologia de reciclagem modular para condomínios residenciais.", 65, "1.2M")

startup_card(c2, 
             "https://images.unsplash.com/photo-1551288049-bbbda536339a?auto=format&fit=crop&w=500&q=80",
             "DataFlow AI", "CURITIBA, PR", 
             "Análise preditiva para pequenos varejistas usando inteligência artificial.", 40, "450k")

startup_card(c3, 
             "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=500&q=80",
             "HealthTrack Wear", "FLORIANÓPOLIS, SC", 
             "Dispositivo vestível focado no monitoramento cardíaco de idosos.", 90, "2.8M")

# --- 4. STATS BAR ---
st.write("")
st.write("---")
st.markdown("""
<div style="display: flex; justify-content: space-around; text-align: center; padding: 40px 0;">
    <div><h2 style="margin:0;">R$ 600M+</h2><p style="color:#888;">CAPITAL ARRECADADO</p></div>
    <div><h2 style="margin:0;">20,000+</h2><p style="color:#888;">INVESTIDORES ATIVOS</p></div>
    <div><h2 style="margin:0;">1,500+</h2><p style="color:#888;">EMPRESAS FINANCIADAS</p></div>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="background-color: #1a2a3a; color: #ccc; padding: 50px; text-align: center; font-size: 14px;">
    <div style="font-weight: 700; color: white; margin-bottom: 20px;">FUNDABLE</div>
    <p>A Fundable faz parte da plataforma Startups.com. <br> © 2024 Fundable LLC. Todos os direitos reservados.</p>
</div>
""", unsafe_allow_html=True)
