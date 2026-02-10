import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Klabin | Valor que se renova",
    page_icon="🌲",
    layout="wide"
)

# --- CSS PERSONALIZADO (KLABIN IDENTITY) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #333;
    }

    /* Header */
    .header-klabin {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 8%;
        background-color: white;
        border-bottom: 2px solid #005a31; /* Verde Klabin */
        margin: -5rem -5rem 0rem -5rem;
    }

    /* Hero Section */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        height: 550px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
        margin: 0 -5rem 50px -5rem;
    }
    .hero-title { font-size: 56px; font-weight: 800; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); }

    /* Seções de Conteúdo */
    .section-padding { padding: 80px 10%; }
    .section-title { color: #005a31; font-weight: 800; font-size: 32px; margin-bottom: 30px; border-left: 5px solid #005a31; padding-left: 15px; }

    /* Card de Negócios */
    .business-card {
        background: #f8f9fa;
        border-radius: 10px;
        overflow: hidden;
        border-bottom: 4px solid #005a31;
        transition: 0.3s;
    }
    .business-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
    .card-label { padding: 25px; }

    /* Stats Section */
    .stats-bg { background-color: #005a31; color: white; padding: 60px 10%; text-align: center; margin: 50px -5rem; }
    .stat-number { font-size: 48px; font-weight: 800; color: #8ec641; } /* Verde limão Klabin */
    .stat-desc { font-size: 14px; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; }

    /* Rodapé Industrial */
    .footer-klabin {
        background-color: #222;
        color: #ccc;
        padding: 80px 10% 40px 10%;
        margin: 50px -5rem -5rem -5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. BARRA DE NAVEGAÇÃO ---
st.markdown("""
<div class="header-klabin">
    <div style="font-size: 30px; font-weight: 800; color: #005a31; letter-spacing: -1px;">KLABIN</div>
    <div style="display: flex; gap: 30px; font-size: 13px; font-weight: 700; color: #555;">
        <span>A KLABIN</span>
        <span>NOSSOS NEGÓCIOS</span>
        <span>SUSTENTABILIDADE</span>
        <span>INVESTIDORES</span>
        <span>PRODUTOS</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO BANNER ---
st.markdown("""
<div class="hero-section">
    <div class="hero-title">O FUTURO É RENOVÁVEL</div>
    <p style="font-size: 20px; font-weight: 400; max-width: 800px; margin-top: 20px;">
        Líder na produção de papéis e cartões para embalagens, embalagens de papelão ondulado e sacos industriais.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. QUEM SOMOS ---
st.markdown('<div class="section-padding">', unsafe_allow_html=True)
c_text, c_img = st.columns([1, 1], gap="large")

with c_text:
    st.markdown('<div class="section-title">Sobre a Klabin</div>', unsafe_allow_html=True)
    st.write("""
    Com 125 anos de história, somos a maior produtora e exportadora de papéis para embalagens e soluções sustentáveis do Brasil. 
    Nossa atuação é baseada no desenvolvimento sustentável, com florestas 100% plantadas e certificadas.
    """)
    st.button("CONHEÇA NOSSA HISTÓRIA")

with c_img:
    st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80", caption="Gestão Florestal Responsável")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. NÚMEROS DE IMPACTO (STATS) ---
st.markdown('<div class="stats-bg">', unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-number">22</div><div class="stat-desc">Fábricas no Brasil e Argentina</div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-number">125</div><div class="stat-desc">Anos de Inovação</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-number">719k</div><div class="stat-desc">Hectares de Florestas</div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-number">25k</div><div class="stat-desc">Colaboradores</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. NOSSOS NEGÓCIOS (GRID DE CARDS) ---
st.markdown('<div class="section-padding" style="padding-top: 20px;">', unsafe_allow_html=True)
st.markdown('<div class="section-title" style="text-align: center; border-left: none;">Nossas Frentes de Atuação</div>', unsafe_allow_html=True)

def business_item(col, img, title, desc):
    with col:
        st.markdown(f"""
        <div class="business-card">
            <img src="{img}" style="width:100%; height:200px; object-fit:cover;">
            <div class="card-label">
                <h4 style="color:#005a31; margin-bottom:10px;">{title}</h4>
                <p style="font-size:14px; color:#666;">{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Saber mais sobre {title}", use_container_width=True)

cb1, cb2, cb3 = st.columns(3)
business_item(cb1, "https://images.unsplash.com/photo-1603484477859-abe6a73f9366?w=500", "Celulose", "Fibra curta, fibra longa e celulose fluff para diversas aplicações.")
business_item(cb2, "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=500", "Embalagens", "Soluções inteligentes em papelão ondulado e sacos industriais.")
business_item(cb3, "https://images.unsplash.com/photo-1532153322601-045a1d39eb14?w=500", "Papéis", "Papel-cartão e Kraftliner de alta performance para o mercado.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. SUSTENTABILIDADE (FULL WIDTH INFO) ---
st.write("---")
with st.container():
    st.markdown('<div class="section-padding">', unsafe_allow_html=True)
    sc1, sc2 = st.columns([2, 3])
    with sc1:
        st.markdown('<div class="section-title">KODS - Objetivos Klabin para o Desenvolvimento Sustentável</div>', unsafe_allow_html=True)
        st.write("Nossa agenda de sustentabilidade está alinhada aos ODS da ONU, com metas claras até 2030 para biodiversidade, clima e impacto social.")
    with sc2:
        # Simulação de ícones de sustentabilidade
        st.info("🌳 Conservação da Biodiversidade")
        st.success("♻️ Economia Circular e Resíduo Zero")
        st.warning("💧 Gestão Eficiente de Recursos Hídricos")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. INVESTIDORES E GOVERNANÇA ---
st.write("---")
st.markdown('<div style="background-color:#f4f7f9; padding: 60px 10%;">', unsafe_allow_html=True)
st.subheader("Relações com Investidores")
col_ri1, col_ri2, col_ri3 = st.columns(3)

with col_ri1:
    st.metric(label="KLBN11 (Units)", value="R$ 22,45", delta="+1.20%")
with col_ri2:
    st.write("**Central de Resultados**")
    st.caption("Acesse os relatórios do 4T25 e demonstrações financeiras.")
    st.button("Acessar Central")
with col_ri3:
    st.write("**Governança Corporativa**")
    st.caption("Transparência e ética em todos os níveis da companhia.")
    st.button("Ver Diretoria")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FOOTER COMPLETO ---
st.markdown("""
<div class="footer-klabin">
    <div style="display:grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap:50px;">
        <div>
            <div style="font-size:24px; font-weight:800; color:white; margin-bottom:20px;">KLABIN</div>
            <p style="font-size:13px;">Líder no mercado de papéis e embalagens, focada na inovação e na sustentabilidade do ciclo da floresta ao consumidor final.</p>
        </div>
        <div>
            <h4 style="color:white; margin-bottom:15px;">NOSSOS SITES</h4>
            <p style="font-size:12px; line-height:2;">Relações com Investidores<br>Klabin ForYou<br>Blog Klabin</p>
        </div>
        <div>
            <h4 style="color:white; margin-bottom:15px;">CONTATO</h4>
            <p style="font-size:12px; line-height:2;">Fale Conosco<br>Imprensa<br>Trabalhe Conosco</p>
        </div>
        <div>
            <h4 style="color:white; margin-bottom:15px;">REDES SOCIAIS</h4>
            <p style="font-size:12px; line-height:2;">LinkedIn<br>Instagram<br>YouTube</p>
        </div>
    </div>
    <div style="text-align:center; border-top:1px solid #444; margin-top:50px; padding-top:20px; font-size:11px;">
        © 2024 Klabin S.A. | Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
