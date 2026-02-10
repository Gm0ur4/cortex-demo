import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Pura Vida Brackets | Estilo de Vida",
    page_icon="🌸",
    layout="wide"
)

# --- CSS PARA ESTILO LIFESTYLE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Pacifico&display=swap');

    /* Barra de Anúncio no Topo */
    .announcement-bar {
        background-color: #ffb6c1; /* Rosa claro */
        color: white;
        text-align: center;
        padding: 8px;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 1px;
        margin: -5rem -5rem 2rem -5rem;
    }

    /* Logo Centralizada */
    .logo-container {
        text-align: center;
        font-family: 'Pacifico', cursive;
        font-size: 45px;
        color: #333;
        margin-bottom: 20px;
    }

    /* Menu de Navegação */
    .nav-links {
        display: flex;
        justify-content: center;
        gap: 30px;
        border-bottom: 1px solid #eee;
        padding-bottom: 15px;
        margin-bottom: 30px;
    }
    .nav-links a {
        text-decoration: none;
        color: #555;
        font-weight: 600;
        font-size: 14px;
        text-transform: uppercase;
    }

    /* Hero Section - Imagem de fundo com texto */
    .hero-box {
        position: relative;
        text-align: center;
        color: white;
        margin-bottom: 40px;
    }
    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 5px;
        color: #333;
    }

    /* Grid de Produtos */
    .product-box {
        text-align: center;
        margin-bottom: 30px;
    }
    .product-price {
        color: #ff69b4;
        font-weight: bold;
    }
    
    /* Botões */
    div.stButton > button {
        background-color: #333;
        color: white;
        border-radius: 0px;
        padding: 10px 20px;
        width: 100%;
        border: none;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div.stButton > button:hover {
        background-color: #ffb6c1;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. BARRA DE ANÚNCIO ---
st.markdown('<div class="announcement-bar">FRETE GRÁTIS EM PEDIDOS ACIMA DE R$ 150! 🌴</div>', unsafe_allow_html=True)

# --- 2. LOGO E MENU ---
st.markdown('<div class="logo-container">pura vida</div>', unsafe_allow_html=True)
st.markdown("""
<div class="nav-links">
    <a href="#">Pulseiras</a>
    <a href="#">Joias</a>
    <a href="#">Coleções</a>
    <a href="#">Sale</a>
</div>
""", unsafe_allow_html=True)

# --- 3. HERO BANNER ---
# Usando imagem de estilo lifestyle praiano
hero_img = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1500&q=80"
st.image(hero_img, use_container_width=True)
st.markdown("""
<div style="text-align: center; padding: 40px 0;">
    <h1 style="font-family: 'Montserrat'; font-weight: 300;">VIVA O MOMENTO</h1>
    <p style="color: #777; max-width: 600px; margin: auto;">
        Nossas peças são feitas à mão por artesãos ao redor do mundo, espalhando a energia "Pura Vida".
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. GRID DE PRODUTOS ---
st.subheader("Novidades")
col1, col2, col3, col4 = st.columns(4)

def product_item(col, name, price, img_url):
    with col:
        st.image(img_url, use_container_width=True)
        st.markdown(f"**{name}**")
        st.markdown(f'<p class="product-price">R$ {price}</p>', unsafe_allow_html=True)
        st.button("Adicionar", key=name)

# Imagens simulando as pulseiras coloridas
product_item(col1, "Pack Shoreline", "45,00", "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?auto=format&fit=crop&w=400&q=80")
product_item(col2, "Ocean Blue", "32,00", "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=400&q=80")
product_item(col3, "Sunset Vibes", "38,00", "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=400&q=80")
product_item(col4, "Sand & Salt", "29,00", "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=400&q=80")

st.write("---")

# --- 5. SEÇÃO DE IMPACTO SOCIAL ---
c1, c2 = st.columns([1, 1])
with c1:
    st.image("https://images.unsplash.com/photo-1484820540004-14229fe36ca4?auto=format&fit=crop&w=800&q=80")
with c2:
    st.markdown("### Retribuindo ao Planeta")
    st.write("Cada compra ajuda a apoiar causas ambientais e artesãos locais. Já doamos mais de R$ 4 milhões para instituições de caridade através de vocês.")
    st.button("Saiba Mais", key="impacto")

# --- 6. RODAPÉ ---
st.markdown("""
<div style="background-color: #f9f9f9; padding: 50px; margin-top: 50px; text-align: center; border-top: 1px solid #eee;">
    <div style="font-family: 'Pacifico'; font-size: 24px; color: #333; margin-bottom: 20px;">pura vida</div>
    <p style="color: #999; font-size: 12px;">© 2024 Pura Vida Brackets. Siga-nos no Instagram @puravida</p>
</div>
""", unsafe_allow_html=True)
