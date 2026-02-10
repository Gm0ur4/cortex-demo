import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(
    page_title="Biscoitos Premium",
    page_icon="🍪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado para design premium
css_code = """
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    :root {
        --primary: #FF3B30;
        --secondary: #00FF41;
        --dark: #0a0a0a;
        --light: #f5f5f5;
        --accent: #FFD700;
    }

    html, body {
        background-color: var(--dark);
        color: var(--light);
        font-family: 'Poppins', sans-serif;
    }

    /* Hide streamlit elements */
    #MainMenu {display: none;}
    footer {display: none;}
    header {display: none;}

    /* Custom styling */
    .main {
        background-color: var(--dark);
    }

    .stApp {
        background-color: var(--dark);
    }

    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, var(--dark) 0%, #1a1a1a 100%);
        padding: 100px 40px;
        text-align: center;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        animation: fadeIn 0.8s ease-out;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    .hero-title {
        font-size: 72px;
        font-weight: 900;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: -2px;
        line-height: 1.2;
        animation: slideInDown 0.8s ease-out;
    }

    @keyframes slideInDown {
        from {
            opacity: 0;
            transform: translateY(-50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .hero-highlight {
        color: var(--primary);
        display: block;
    }

    .hero-highlight-secondary {
        color: var(--secondary);
        display: block;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #aaa;
        margin-bottom: 40px;
        max-width: 500px;
        line-height: 1.6;
        animation: fadeInUp 0.8s ease-out 0.3s both;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .cookie-circle {
        width: 300px;
        height: 300px;
        background: radial-gradient(circle at 30% 30%, #FFD700, #FF8C00, #8B4513);
        border-radius: 50%;
        margin: 40px auto;
        box-shadow: 0 20px 60px rgba(255, 59, 48, 0.3), inset -20px -20px 40px rgba(0, 0, 0, 0.3);
        animation: spin 20s linear infinite;
    }

    @keyframes spin {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }

    /* Section styling */
    .section {
        padding: 80px 40px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .section-title {
        font-size: 56px;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 60px;
        text-align: center;
    }

    .section-title-main {
        color: var(--light);
    }

    .section-title-highlight {
        color: var(--primary);
        display: block;
    }

    .section-title-highlight-secondary {
        color: var(--secondary);
        display: block;
    }

    /* Apresentação Section */
    .apresentacao-section {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
    }

    /* Produtos Section */
    .produtos-section {
        background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
    }

    /* Depoimentos Section */
    .depoimentos-section {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
    }

    /* Cards */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 20px;
    }

    .card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.1);
        border-color: var(--secondary);
        box-shadow: 0 20px 40px rgba(0, 255, 65, 0.2);
    }

    .card-icon {
        font-size: 50px;
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 20px;
        margin-bottom: 15px;
        color: var(--light);
        text-transform: uppercase;
        font-weight: 700;
    }

    .card-description {
        font-size: 14px;
        color: #aaa;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .card-price {
        font-size: 24px;
        font-weight: 700;
        color: var(--secondary);
        margin-bottom: 20px;
    }

    /* CTA Button */
    .cta-button {
        background: var(--primary);
        color: white;
        padding: 18px 50px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(255, 59, 48, 0.3);
        border: 2px solid var(--primary);
        display: inline-block;
        margin-top: 20px;
        cursor: pointer;
    }

    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(255, 59, 48, 0.5);
        background: transparent;
        color: var(--primary);
    }

    /* CTA Final Section */
    .cta-final-section {
        background: linear-gradient(135deg, var(--primary) 0%, #FF6B5B 100%);
        min-height: 80vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 100px 40px;
    }

    .cta-final-title {
        font-size: 56px;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 30px;
        color: white;
    }

    .cta-final-text {
        font-size: 20px;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 50px;
        max-width: 600px;
    }

    .cta-final-button {
        background: white;
        color: var(--primary);
        padding: 20px 60px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        border: 2px solid white;
        display: inline-block;
        cursor: pointer;
    }

    .cta-final-button:hover {
        transform: scale(1.05);
        background: transparent;
        color: white;
    }

    /* Footer */
    .footer {
        background: var(--dark);
        padding: 60px 40px;
        text-align: center;
        border-top: 2px solid var(--secondary);
    }

    .footer-text {
        color: #aaa;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 48px;
        }

        .section-title {
            font-size: 40px;
        }

        .cookie-circle {
            width: 200px;
            height: 200px;
        }

        .section {
            padding: 60px 20px;
        }

        .hero-section {
            padding: 60px 20px;
        }
    }

    /* Streamlit specific overrides */
    .stButton button {
        background: var(--primary) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 12px 30px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(255, 59, 48, 0.3) !important;
        border: 2px solid var(--primary) !important;
    }

    .stButton button:hover {
        background: transparent !important;
        color: var(--primary) !important;
        transform: scale(1.05) !important;
    }

    .stMarkdown {
        color: var(--light) !important;
    }

    .stMetric {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
</style>
"""

# Injetar CSS
st.markdown(css_code, unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">
        Aqui Tem<br>
        <span class="hero-highlight">O Sabor</span><br>
        <span class="hero-highlight-secondary">Queridinho</span>
    </h1>
    <p class="hero-subtitle">
        Biscoitos premium feitos com ingredientes selecionados e muito amor. 
        A melhor experiência de sabor que você já teve.
    </p>
    <div class="cookie-circle"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# APRESENTAÇÃO SECTION
st.markdown("""
<div class="apresentacao-section section">
    <h2 class="section-title">
        <span class="section-title-main">Biscoito,</span><br>
        <span class="section-title-highlight-secondary">Vamos nos Apresentar</span>
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="padding: 40px;">
        <p style="font-size: 18px; color: #aaa; line-height: 1.8; margin-bottom: 20px;">
            Somos uma marca que nasceu do amor pela qualidade e pela excelência. 
            Cada biscoito é feito com ingredientes premium, selecionados com cuidado 
            para garantir o melhor sabor.
        </p>
        <p style="font-size: 18px; color: #aaa; line-height: 1.8;">
            Nossa missão é transformar cada momento em uma experiência inesquecível. 
            Porque você merece o melhor.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF3B30, #00FF41); 
                border-radius: 20px; padding: 100px 40px; text-align: center;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);">
        <p style="color: white; font-size: 16px;">Sua Foto/Vídeo Aqui</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# PRODUTOS SECTION
st.markdown("""
<div class="produtos-section section">
    <h2 class="section-title">
        <span class="section-title-main">Nossos</span><br>
        <span class="section-title-highlight">Sabores Especiais</span>
    </h2>
</div>
""", unsafe_allow_html=True)

produtos = [
    {"nome": "Chocolate Premium", "icon": "🍫", "desc": "Biscoito com chocolate belga de alta qualidade. Irresistível.", "preco": "R$ 29,90"},
    {"nome": "Amendoim Crocante", "icon": "🥜", "desc": "Biscoito com amendoim selecionado. Crocância garantida.", "preco": "R$ 27,90"},
    {"nome": "Morango Delicado", "icon": "🍓", "desc": "Biscoito com morango fresco. Doce e refrescante.", "preco": "R$ 31,90"},
    {"nome": "Coco Tropical", "icon": "🥥", "desc": "Biscoito com coco ralado. Sabor que transporta.", "preco": "R$ 28,90"},
    {"nome": "Limão Siciliano", "icon": "🍋", "desc": "Biscoito com limão fresco. Acidez perfeita.", "preco": "R$ 26,90"},
    {"nome": "Mel e Canela", "icon": "🍯", "desc": "Biscoito com mel puro. Aconchego em cada mordida.", "preco": "R$ 30,90"},
]

cols = st.columns(3)
for idx, produto in enumerate(produtos):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">{produto['icon']}</div>
            <h3 class="card-title">{produto['nome']}</h3>
            <p class="card-description">{produto['desc']}</p>
            <div class="card-price">{produto['preco']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Quero Conhecer", key=f"btn_{idx}")

st.markdown("---")

# DEPOIMENTOS SECTION
st.markdown("""
<div class="depoimentos-section section">
    <h2 class="section-title">
        <span class="section-title-main">O Que Nossos</span><br>
        <span class="section-title-highlight">Clientes Dizem</span>
    </h2>
</div>
""", unsafe_allow_html=True)

depoimentos = [
    {"texto": "Melhor biscoito que já comi na vida! A qualidade é incomparável. Recomendo para todos!", "autor": "Maria Silva"},
    {"texto": "Comprei para presentear e meus amigos amaram! Vão virar clientes também.", "autor": "João Santos"},
    {"texto": "A experiência de compra foi perfeita. Entrega rápida e produto impecável!", "autor": "Ana Costa"},
]

cols = st.columns(3)
for idx, depo in enumerate(depoimentos):
    with cols[idx]:
        st.markdown(f"""
        <div class="card">
            <div style="color: #FFD700; font-size: 18px; margin-bottom: 15px;">⭐⭐⭐⭐⭐</div>
            <p style="font-size: 16px; color: #aaa; line-height: 1.8; margin-bottom: 20px; font-style: italic;">
                "{depo['texto']}"
            </p>
            <p style="font-weight: 700; color: var(--light); font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">
                — {depo['autor']}
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# CTA FINAL SECTION
st.markdown("""
<div class="cta-final-section">
    <h2 class="cta-final-title">Pronto Para Experimentar?</h2>
    <p class="cta-final-text">
        Não perca a oportunidade de viver a melhor experiência de sabor. 
        Peça agora e receba em casa com todo cuidado.
    </p>
</div>
""", unsafe_allow_html=True)

st.button("🛒 Fazer Pedido Agora", key="cta_final", use_container_width=True)

st.markdown("---")

# FOOTER
st.markdown("""
<div class="footer">
    <p class="footer-text">&copy; 2024 Biscoitos Premium. Todos os direitos reservados.</p>
    <p class="footer-text">Feito com ❤️ para você.</p>
</div>
""", unsafe_allow_html=True)
