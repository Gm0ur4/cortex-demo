import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Glam | O maior clube de beleza da América Latina",
    page_icon="💖",
    layout="wide"
)

# --- CSS PERSONALIZADO (GLAM AESTHETIC) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #333;
    }

    /* Remover espaçamentos padrão */
    .block-container { padding: 0 !important; }

    /* Nav Bar Estilo Glam */
    .nav-glam {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 5%;
        background: white;
        border-bottom: 1px solid #f0f0f0;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .nav-links a {
        text-decoration: none;
        color: #333;
        font-weight: 500;
        font-size: 13px;
        margin-right: 20px;
    }

    /* Hero Banner Principal */
    .hero-glam {
        background-color: #fce4ec; /* Rosa bem clarinho */
        padding: 80px 8%;
        display: flex;
        align-items: center;
        margin-bottom: 50px;
    }
    .hero-title {
        font-size: 45px;
        font-weight: 700;
        color: #d81b60; /* Rosa Glam */
        line-height: 1.2;
    }

    /* Botões Arredondados */
    div.stButton > button {
        border-radius: 50px;
        padding: 12px 35px;
        background-color: #d81b60;
        color: white;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ad1457;
        transform: scale(1.02);
    }

    /* Seção de Planos */
    .plan-card {
        background: white;
        border: 2px solid #fce4ec;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: 0.3s;
    }
    .plan-card:hover {
        border-color: #d81b60;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    .price-tag {
        font-size: 32px;
        font-weight: 700;
        color: #d81b60;
    }

    /* Footer */
    .footer-glam {
        background-color: #fafafa;
        padding: 80px 8%;
        border-top: 1px solid #eee;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
<div class="nav-glam">
    <div style="font-size: 24px; font-weight: 700; letter-spacing: 2px; color: #d81b60;">GLAM</div>
    <div class="nav-links">
        <a href="#">GLAMBOX</a>
        <a href="#">GLAMSHOP</a>
        <a href="#">GLAMPASS</a>
        <a href="#">BLOG</a>
    </div>
    <div style="font-size: 12px; font-weight: 600;">ENTRAR / CADASTRE-SE</div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
with st.container():
    col_h1, col_h2 = st.columns([1, 1])
    with col_h1:
        st.markdown('<div style="padding: 100px 0 0 100px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Sua jornada de beleza começa aqui.</h1>', unsafe_allow_html=True)
        st.write("Receba mensalmente uma curadoria de produtos de beleza escolhidos para o seu perfil.")
        st.write("")
        st.button("ASSINE AGORA")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_h2:
        st.image("https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?auto=format&fit=crop&w=800&q=80")

# --- 3. COMO FUNCIONA ---
st.markdown("<br><br><h2 style='text-align:center;'>Como funciona a experiência Glam</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div style='text-align:center;'><h3>1. Perfil de Beleza</h3><p>Conte-nos seus gostos, tipo de pele e cabelo.</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div style='text-align:center;'><h3>2. Curadoria</h3><p>Nossos experts selecionam 5 a 7 produtos para você.</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div style='text-align:center;'><h3>3. Glam Box</h3><p>Receba em casa e descubra novos favoritos.</p></div>", unsafe_allow_html=True)

# --- 4. PLANOS (CARDS) ---
st.write("---")
st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>Escolha o seu plano</h2>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

def plan_box(col, title, price, benefit):
    with col:
        st.markdown(f"""
        <div class="plan-card">
            <h4 style="color:#666;">{title}</h4>
            <div class="price-tag">R$ {price}</div>
            <p style="font-size:14px; color:#888;">por mês</p>
            <hr style="border: 0.5px solid #fce4ec;">
            <p style="font-weight:500;">{benefit}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Assinar {title}", use_container_width=True)

plan_box(p1, "PLANO MENSAL", "82,90", "Flexibilidade total")
plan_box(p2, "PLANO SEMESTRAL", "72,90", "Descontos na Glam Shop")
plan_box(p3, "PLANO ANUAL", "62,90", "Brinde exclusivo + Frete Grátis")

# --- 5. MARCAS PARCEIRAS (PROVA SOCIAL) ---
st.write("")
st.markdown("<p style='text-align:center; color:#999; text-transform:uppercase; letter-spacing:2px; font-size:12px;'>Marcas que você pode receber</p>", unsafe_allow_html=True)
st.markdown("""
<div style="display:flex; justify-content:center; gap:50px; opacity:0.4; font-weight:700; font-size:18px; padding: 20px 0;">
    <span>L'ORÉAL</span> <span>VICHY</span> <span>EUDORA</span> <span>NIVEA</span> <span>PANTENE</span>
</div>
""", unsafe_allow_html=True)

# --- 6. SEÇÃO GLAM SHOP (E-COMMERCE) ---
st.write("---")
st.markdown("<h2 style='text-align:center;'>Ofertas da Glam Shop</h2>", unsafe_allow_html=True)

ps1, ps2, ps3, ps4 = st.columns(4)

def shop_item(col, img, name, price):
    with col:
        st.image(img)
        st.markdown(f"**{name}**")
        st.markdown(f"<span style='color:#d81b60; font-weight:700;'>R$ {price}</span>", unsafe_allow_html=True)
        st.button("Comprar", key=name)

shop_item(ps1, "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=300", "Batom Matte Rose", "29,90")
shop_item(ps2, "https://images.unsplash.com/photo-1612817288484-6f916006741a?w=300", "Sérum Facial Vit C", "89,00")
shop_item(ps3, "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=300", "Hidratante Corporal", "45,00")
shop_item(ps4, "https://images.unsplash.com/photo-1590156191108-33002f58ca40?w=300", "Máscara de Cílios", "34,90")

# --- 7. FOOTER ---
st.markdown("""
<div class="footer-glam">
    <div style="display:grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap:30px;">
        <div>
            <div style="font-size: 20px; font-weight: 700; color: #d81b60; margin-bottom:20px;">GLAM</div>
            <p style="font-size:12px;">A maior comunidade de beleza do país. Conectamos marcas e consumidoras através de experiências reais.</p>
        </div>
        <div>
            <h4 style="font-size:14px;">INSTITUCIONAL</h4>
            <p style="font-size:12px; line-height:2;">Sobre a Glam<br>Trabalhe Conosco<br>Seja um parceiro</p>
        </div>
        <div>
            <h4 style="font-size:14px;">DÚVIDAS</h4>
            <p style="font-size:12px; line-height:2;">Central de Ajuda<br>Trocas e Devoluções<br>Prazos de Entrega</p>
        </div>
        <div>
            <h4 style="font-size:14px;">REDES SOCIAIS</h4>
            <p style="font-size:12px; line-height:2;">Instagram<br>TikTok<br>YouTube</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
