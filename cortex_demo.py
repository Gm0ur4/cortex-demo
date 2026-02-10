import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Roeeby | Iluminação & Design de Interiores",
    page_icon="💡",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (ESTILO ROEEBY) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@300;400;600&family=Inter:wght@300;400;600&display=swap');

    /* Cores e Fundo */
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Editorial */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, .serif-roeeby {
        font-family: 'Crimson Pro', serif;
        font-weight: 300;
        letter-spacing: -0.5px;
    }

    /* Navegação Superior */
    .nav-roeeby {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 5%;
        border-bottom: 1px solid #f2f2f2;
        background: white;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    .logo-roeeby {
        font-family: 'Crimson Pro', serif;
        font-size: 32px;
        font-weight: 600;
        letter-spacing: 2px;
    }

    /* Banner Promocional */
    .promo-banner {
        background-color: #1a1a1a;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Grid de Produtos */
    .product-grid {
        padding: 60px 5%;
    }

    .product-item {
        margin-bottom: 40px;
        position: relative;
    }

    .product-img {
        width: 100%;
        height: auto;
        display: block;
        transition: opacity 0.3s ease;
    }

    .product-item:hover .product-img {
        opacity: 0.85;
    }

    .label-new {
        position: absolute;
        top: 15px;
        left: 15px;
        background: white;
        color: black;
        padding: 4px 12px;
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        border: 1px solid #eee;
    }

    .product-info {
        margin-top: 20px;
        text-align: center;
    }

    .product-name {
        font-size: 16px;
        font-weight: 400;
        margin-bottom: 5px;
    }

    .product-price {
        font-weight: 600;
        color: #555;
    }

    /* Botão Roeeby */
    div.stButton > button {
        background-color: white;
        color: #1a1a1a;
        border: 1px solid #1a1a1a;
        border-radius: 0;
        padding: 10px 30px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #1a1a1a;
        color: white;
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. BANNER E NAVEGAÇÃO ---
st.markdown('<div class="promo-banner">Frete Grátis em Pedidos acima de R$ 500 — Compre Agora</div>', unsafe_allow_html=True)
st.markdown("""
<div class="nav-roeeby">
    <div style="display: flex; gap: 30px; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">
        <span>Iluminação</span>
        <span>Móveis</span>
        <span>Decoração</span>
    </div>
    <div class="logo-roeeby">ROEEBY</div>
    <div style="display: flex; gap: 30px; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">
        <span>Busca</span>
        <span>Carrinho (0)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div style="width: 100%; height: 70vh; background-image: url('https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=1600'); background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center;">
    <div style="background: rgba(255,255,255,0.9); padding: 50px 80px; text-align: center; border: 1px solid #eee;">
        <h2 class="serif-roeeby" style="font-size: 40px; margin-bottom: 10px;">Coleção de Inverno</h2>
        <p style="font-size: 14px; letter-spacing: 2px; color: #666; text-transform: uppercase; margin-bottom: 25px;">Ilumine sua casa com sofisticação</p>
        <div style="border-bottom: 2px solid #1a1a1a; display: inline-block; padding-bottom: 5px; font-weight: 600; font-size: 12px; letter-spacing: 1px;">VER COLEÇÃO</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. GRID DE PRODUTOS ---
st.markdown('<div class="product-grid">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-roeeby" style="font-size: 32px; text-align: center; margin-bottom: 50px;">Produtos em Destaque</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

def render_roeeby_item(col, title, price, img_url, label=None):
    with col:
        label_html = f'<div class="label-new">{label}</div>' if label else ""
        st.markdown(f"""
        <div class="product-item">
            {label_html}
            <img src="{img_url}" class="product-img">
            <div class="product-info">
                <div class="product-name">{title}</div>
                <div class="product-price">R$ {price}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Comprar {title.split()[0]}", key=title)

render_roeeby_item(col1, "Luminária de Mesa Aura", "890,00", "https://images.unsplash.com/photo-1534073828943-f801091bb18c?w=600", "New")
render_roeeby_item(col2, "Pendente Minimalista Black", "1.250,00", "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600")
render_roeeby_item(col3, "Lustre Nórdico Wood", "2.100,00", "https://images.unsplash.com/photo-1543198126-a8ad8e47fb21?w=600", "Sale")
render_roeeby_item(col4, "Arandela Industrial Copper", "640,00", "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=600")

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SEÇÃO INSTITUCIONAL ---
st.markdown("""
<div style="background-color: #f9f9f9; padding: 100px 5%; display: flex; align-items: center; gap: 80px;">
    <div style="flex: 1;">
        <img src="https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=800" style="width: 100%;">
    </div>
    <div style="flex: 1;">
        <h2 class="serif-roeeby" style="font-size: 48px; margin-bottom: 30px;">Qualidade que brilha.</h2>
        <p style="font-size: 16px; line-height: 1.8; color: #444; margin-bottom: 30px;">
            Cada peça na Roeeby é selecionada para oferecer não apenas luz, mas uma experiência estética única. 
            Colaboramos com designers internacionais para trazer o que há de mais moderno em tecnologia LED 
            e materiais sustentáveis.
        </p>
        <div style="border-bottom: 2px solid #1a1a1a; display: inline-block; padding-bottom: 5px; font-weight: 600; font-size: 12px; letter-spacing: 1px;">NOSSA HISTÓRIA</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div style="padding: 80px 5% 40px 5%; border-top: 1px solid #eee;">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px;">
        <div>
            <h4 class="serif-roeeby" style="font-size: 24px; margin-bottom: 20px;">ROEEBY</h4>
            <p style="font-size: 13px; color: #888; line-height: 1.6;">Design de iluminação para lares que respiram arte e conforto.</p>
        </div>
        <div>
            <h5 style="font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px;">Menu</h5>
            <p style="font-size: 13px; color: #555; margin-bottom: 10px;">Início</p>
            <p style="font-size: 13px; color: #555; margin-bottom: 10px;">Coleções</p>
            <p style="font-size: 13px; color: #555; margin-bottom: 10px;">Outlet</p>
        </div>
        <div>
            <h5 style="font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px;">Suporte</h5>
            <p style="font-size: 13px; color: #555; margin-bottom: 10px;">Envio</p>
            <p style="font-size: 13px; color: #555; margin-bottom: 10px;">Trocas</p>
            <p style="font-size: 13px; color: #555; margin-bottom: 10px;">FAQ</p>
        </div>
        <div>
            <h5 style="font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px;">Novidades</h5>
            <input type="text" placeholder="Seu e-mail" style="width: 100%; padding: 10px; border: 1px solid #eee; margin-bottom: 10px;">
            <div style="background: black; color: white; text-align: center; padding: 10px; font-size: 12px; letter-spacing: 1px;">ASSINAR</div>
        </div>
    </div>
    <div style="margin-top: 60px; padding-top: 20px; border-top: 1px solid #f2f2f2; text-align: center; font-size: 10px; color: #aaa; letter-spacing: 1px;">
        © 2026 ROEEBY INTERIORS. TODOS OS DIREITOS RESERVADOS.
    </div>
</div>
""", unsafe_allow_html=True)
