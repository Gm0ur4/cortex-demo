import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Qudrix | Soluções Digitais de Alta Performance",
    page_icon="⚡",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (QUDRIX TECH STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* Reset Geral */
    .stApp {
        background-color: #ffffff;
        color: #111111;
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia de Precisão */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        -webkit-font-smoothing: antialiased;
    }

    /* Header Corporativo Moderno */
    .nav-qudrix {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 25px 8%;
        border-bottom: 1px solid #f0f0f0;
        position: sticky;
        top: 0;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        z-index: 1000;
    }
    
    .logo-qudrix {
        font-weight: 800;
        font-size: 22px;
        letter-spacing: -1px;
    }

    /* Hero Section - Impacto e Engenharia */
    .hero-qudrix {
        padding: 120px 8% 80px 8%;
        text-align: left;
    }
    
    .hero-h1 {
        font-size: clamp(40px, 6vw, 80px);
        font-weight: 800;
        line-height: 1;
        letter-spacing: -0.04em;
        margin-bottom: 30px;
        color: #000;
    }

    /* Grid de Serviços/Cards */
    .service-grid {
        padding: 40px 8%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
    }

    .card-qudrix {
        background: #f9f9f9;
        border: 1px solid #eee;
        padding: 40px;
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .card-qudrix:hover {
        background: #ffffff;
        border-color: #000;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transform: translateY(-5px);
    }

    .card-icon {
        width: 40px;
        height: 40px;
        background: #000;
        border-radius: 8px;
        margin-bottom: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
    }

    /* Botão de Ação Direta */
    div.stButton > button {
        background-color: #111111;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 15px;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background-color: #333;
        transform: scale(1.02);
    }

    /* Footer Estruturado */
    .footer-qudrix {
        background: #111111;
        color: #ffffff;
        padding: 80px 8%;
        margin-top: 120px;
    }

    .footer-link {
        color: #888;
        text-decoration: none;
        font-size: 14px;
        margin-bottom: 10px;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-qudrix">
    <div class="logo-qudrix">QUDRIX</div>
    <div style="display: flex; gap: 35px; font-size: 14px; font-weight: 500;">
        <span>Serviços</span>
        <span>Tecnologias</span>
        <span>Casos</span>
        <span>Sobre</span>
    </div>
    <div style="font-weight: 600; font-size: 14px; border: 1px solid #111; padding: 8px 20px; border-radius: 6px;">
        Contato
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO ---
st.markdown('<div class="hero-qudrix">', unsafe_allow_html=True)
st.markdown('<p style="color: #666; font-weight: 600; margin-bottom: 20px;">TECNOLOGIA DE PONTA</p>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-h1">Engenharia de software<br>para líderes de mercado.</h1>', unsafe_allow_html=True)
st.markdown('<p style="max-width: 600px; font-size: 18px; color: #555; line-height: 1.6; margin-bottom: 40px;">Ajudamos empresas a escalar através de infraestrutura robusta, design centrado no usuário e soluções digitais sob medida.</p>', unsafe_allow_html=True)
st.button("Vamos conversar")
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. SERVIÇOS (GRID TÉCNICO) ---
st.markdown('<div class="service-grid">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

def render_card(col, title, desc, icon="</>"):
    with col:
        st.markdown(f"""
        <div class="card-qudrix">
            <div class="card-icon">{icon}</div>
            <h3 style="font-weight: 700; margin-bottom: 15px;">{title}</h3>
            <p style="color: #666; font-size: 14px; line-height: 1.6;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

render_card(col1, "Web Development", "Aplicações escaláveis utilizando React, Next.js e infraestruturas em nuvem modernas.")
render_card(col2, "Mobile First", "Experiências nativas e híbridas com foco total em performance e retenção de usuários.")
render_card(col3, "Cloud & DevOps", "Arquitetura de sistemas resilientes, automação de CI/CD e segurança de dados.")

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SEÇÃO DE PROVA SOCIAL / STATS ---
st.markdown("""
<div style="padding: 100px 8%; background-color: #000; color: #fff; display: flex; justify-content: space-between; align-items: center; margin-top: 50px;">
    <div>
        <h2 style="font-size: 40px; font-weight: 800; letter-spacing: -2px;">ENTREGA REAL.</h2>
        <p style="color: #888;">Resultados mensuráveis para negócios globais.</p>
    </div>
    <div style="display: flex; gap: 60px;">
        <div style="text-align: center;">
            <div style="font-size: 48px; font-weight: 800;">150+</div>
            <div style="color: #888; font-size: 12px; text-transform: uppercase;">Projetos</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 48px; font-weight: 800;">12</div>
            <div style="color: #888; font-size: 12px; text-transform: uppercase;">Países</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div class="footer-qudrix">
    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 40px;">
        <div>
            <div class="logo-qudrix" style="color: white; margin-bottom: 20px;">QUDRIX</div>
            <p style="color: #666; font-size: 14px;">Elevando o padrão do desenvolvimento de software através de metodologias ágeis e talento sênior.</p>
        </div>
        <div>
            <h4 style="font-size: 14px; margin-bottom: 20px;">EMPRESA</h4>
            <a class="footer-link">Sobre nós</a>
            <a class="footer-link">Carreiras</a>
            <a class="footer-link">Blog</a>
        </div>
        <div>
            <h4 style="font-size: 14px; margin-bottom: 20px;">LEGAL</h4>
            <a class="footer-link">Privacidade</a>
            <a class="footer-link">Termos</a>
        </div>
        <div>
            <h4 style="font-size: 14px; margin-bottom: 20px;">SOCIAL</h4>
            <a class="footer-link">LinkedIn</a>
            <a class="footer-link">GitHub</a>
            <a class="footer-link">Twitter</a>
        </div>
    </div>
    <div style="margin-top: 80px; padding-top: 20px; border-top: 1px solid #222; font-size: 12px; color: #444;">
        © 2026 QUDRIX DIGITAL SOLUTIONS. ALL RIGHTS RESERVED.
    </div>
</div>
""", unsafe_allow_html=True)
