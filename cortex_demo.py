import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Feastables | O Chocolate do MrBeast",
    page_icon="🍫",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (FEASTABLES VIBE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Inter:wght@700;900&display=swap');

    /* Cores de Marca */
    :root {
        --feast-blue: #0047ff;
        --feast-pink: #ff00ff;
        --feast-yellow: #ffff00;
    }

    .stApp {
        background-color: var(--feast-blue);
    }

    /* Tipografia */
    h1, h2, .font-heavy {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        color: white;
        letter-spacing: -2px;
    }

    /* Banner Corrediço (Marquee) */
    .marquee {
        background: var(--feast-yellow);
        color: black;
        padding: 10px 0;
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        white-space: nowrap;
        overflow: hidden;
        display: flex;
        font-size: 20px;
        border-bottom: 4px solid black;
    }

    /* Hero Section */
    .hero-feast {
        padding: 60px 5%;
        text-align: center;
    }

    /* Cards de Produto */
    .product-card {
        background: white;
        border: 4px solid black;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s;
        box-shadow: 8px 8px 0px 0px rgba(0,0,0,1);
        margin-bottom: 30px;
    }
    .product-card:hover {
        transform: translate(-4px, -4px);
        box-shadow: 12px 12px 0px 0px rgba(255, 0, 255, 0.8);
    }

    .price-tag {
        background: var(--feast-pink);
        color: white;
        padding: 5px 15px;
        border-radius: 50px;
        display: inline-block;
        font-weight: 900;
        margin-top: 10px;
    }

    /* Botão Feastables */
    div.stButton > button {
        background-color: var(--feast-yellow);
        color: black;
        border: 4px solid black;
        border-radius: 12px;
        font-weight: 900;
        font-size: 24px;
        padding: 20px 40px;
        box-shadow: 6px 6px 0px 0px rgba(0,0,0,1);
        transition: 0.1s;
        width: 100%;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: var(--feast-pink);
        color: white;
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0px 0px rgba(0,0,0,1);
    }

    /* Footer */
    .footer-feast {
        background: black;
        color: white;
        padding: 60px 5%;
        margin-top: 100px;
    }
    
    [data-testid="stHeader"] { display: none; }
</style>

<div class="marquee">
    <div style="display: flex; animation: marquee 20s linear infinite;">
        <span style="margin-right: 50px;">MELHOR QUE O SEU CHOCOLATE ATUAL 🔥</span>
        <span style="margin-right: 50px;">INGREDIENTES REAIS 🔥</span>
        <span style="margin-right: 50px;">DO MR BEAST 🔥</span>
        <span style="margin-right: 50px;">PROVE A DIFERENÇA 🔥</span>
        <span style="margin-right: 50px;">MELHOR QUE O SEU CHOCOLATE ATUAL 🔥</span>
    </div>
</div>

<style>
@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER / LOGO ---
st.markdown("""
<div style="text-align: center; padding: 40px 0;">
    <h1 style="font-size: 80px; text-shadow: 4px 4px 0px #ff00ff;">FEASTABLES</h1>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO IMAGE & CTA ---
col_hero_1, col_hero_2 = st.columns([1, 1])
with col_hero_1:
    st.markdown("""
    <div style="padding-top: 50px;">
        <h2 style="font-size: 60px;">O CHOCOLATE<br>QUE DETONA.</h2>
        <p style="color: white; font-size: 20px; font-weight: 700;">Zero porcaria. Apenas sabor épico.</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("COMPRE AGORA")

with col_hero_2:
    # Imagem simulando a nova embalagem vibrante
    st.image("https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=800", use_container_width=True)

# --- 3. PRODUTOS (LOJA) ---
st.markdown("<br><br><h2 style='text-align: center; font-size: 45px;'>ESCOLHA SEU TIME</h2>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

def feast_card(col, title, flavor, img_url, price):
    with col:
        st.markdown(f"""
        <div class="product-card">
            <img src="{img_url}" style="width:100%; border-radius:10px;">
            <h3 style="color: black; margin-top: 15px; font-weight: 900; font-size: 24px;">{title}</h3>
            <p style="color: #555; font-weight: 700;">{flavor}</p>
            <div class="price-tag">R$ {price}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"ADICIONAR {title}", key=title)

feast_card(p1, "MILK CRUNCH", "Com Arroz Crocante", "https://images.unsplash.com/photo-1548907040-4baa42d10919?w=400", "19,90")
feast_card(p2, "ORIGINAL MILK", "Clássico e Cremoso", "https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=400", "18,90")
feast_card(p3, "PEANUT BUTTER", "Manteiga de Amendoim", "https://images.unsplash.com/photo-1581798459219-318e76aecc7b?w=400", "22,90")

# --- 4. SEÇÃO "POR QUE NÓS?" (LONG FORM) ---
st.markdown("""
<div style="background-color: #ff00ff; padding: 100px 10%; margin-top: 80px; border-top: 5px solid black; border-bottom: 5px solid black;">
    <h2 style="color: white; font-size: 50px; text-align: center;">O QUE TEM DENTRO IMPORTA.</h2>
    <div style="display: flex; justify-content: space-around; margin-top: 50px; text-align: center; flex-wrap: wrap;">
        <div style="max-width: 250px;">
            <h1 style="font-size: 60px;">🌾</h1>
            <h3 style="color: white;">SEM GLÚTEN</h3>
        </div>
        <div style="max-width: 250px;">
            <h1 style="font-size: 60px;">🌱</h1>
            <h3 style="color: white;">INGREDIENTES SIMPLES</h3>
        </div>
        <div style="max-width: 250px;">
            <h1 style="font-size: 60px;">👅</h1>
            <h3 style="color: white;">SABOR INCRÍVEL</h3>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("""
<div class="footer-feast">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
        <div>
            <h2 style="font-size: 32px; text-shadow: 2px 2px 0px #ff00ff;">FEASTABLES</h2>
            <p style="color: #aaa;">Inspirado pelo MrBeast.</p>
        </div>
        <div style="line-height: 2;">
            <p><strong>RECURSOS</strong></p>
            <p>Onde Comprar</p>
            <p>Perguntas Frequentes</p>
            <p>Termos de Uso</p>
        </div>
        <div>
            <p><strong>NOS SIGA</strong></p>
            <p>TikTok / Instagram / YouTube</p>
        </div>
    </div>
    <div style="margin-top: 50px; border-top: 1px solid #333; padding-top: 20px; font-size: 12px; color: #666; text-align: center;">
        © 2026 FEASTABLES INC. TODOS OS DIREITOS RESERVADOS.
    </div>
</div>
""", unsafe_allow_html=True)
