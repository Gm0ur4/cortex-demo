import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Icarus Medical | Custom Knee Braces",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZADO (AESTHETIC MEDICAL TECH) ---
st.markdown("""
<style>
    /* Importando fonte Roboto para visual mais clean/tech */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    /* Remover padding excessivo do topo */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    /* Header Navigation Bar simulada */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 20px;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }
    .logo-text {
        font-size: 24px;
        font-weight: 700;
        color: #2c3e50;
        letter-spacing: 1px;
    }
    .nav-links a {
        text-decoration: none;
        color: #555;
        margin-left: 20px;
        font-weight: 500;
        font-size: 14px;
    }
    .nav-links a:hover {
        color: #007bff;
    }

    /* Hero Section Styles */
    .hero-container {
        background-color: #f8f9fa;
        padding: 60px 40px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 40px;
    }
    .hero-title {
        font-size: 48px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 20px;
        color: #666;
        margin-bottom: 30px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Botões customizados estilo "Medical Blue" */
    .stButton > button {
        background-color: #0056b3;
        color: white;
        border-radius: 4px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #004494;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* Cards de Produtos */
    .product-card {
        background: white;
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s;
        height: 100%;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border-color: #0056b3;
    }
    .product-name {
        font-size: 22px;
        font-weight: 700;
        color: #222;
        margin-top: 15px;
    }
    .product-desc {
        color: #666;
        font-size: 14px;
        margin-bottom: 15px;
        line-height: 1.5;
    }

    /* Stats Section */
    .stat-box {
        text-align: center;
        padding: 20px;
    }
    .stat-number {
        font-size: 36px;
        font-weight: bold;
        color: #0056b3;
    }
    .stat-label {
        font-size: 14px;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Footer */
    .footer-section {
        background-color: #1a1a1a;
        color: #aaa;
        padding: 40px;
        margin-top: 50px;
        text-align: center;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER (HTML Puro para controle total do layout) ---
st.markdown("""
<div class="nav-container">
    <div class="logo-text">ICARUS MEDICAL</div>
    <div class="nav-links">
        <a href="#">HOME</a>
        <a href="#">PRODUCTS</a>
        <a href="#">PATIENTS</a>
        <a href="#">PROVIDERS</a>
        <a href="#">CONTACT</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
# O site original tem uma imagem grande de alguém correndo ou o produto em destaque.
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown('<div style="padding-top: 40px;">', unsafe_allow_html=True)
    st.markdown("# Relieve Knee Pain.\n# Restore Mobility.")
    st.markdown("""
    <p style="font-size: 18px; color: #555; line-height: 1.6;">
    Custom 3D-printed knee braces engineered to unload weight and reduce pain. 
    The most advanced conservative treatment for osteoarthritis.
    </p>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns([1, 2])
    with col_btn1:
        st.button("AM I A CANDIDATE?")
    with col_btn2:
        st.button("VIEW PRODUCTS", type="secondary") # Secondary style logic not native, but visually distinct via CSS if needed
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    # Imagem simulando o produto "Ascender" (High tech brace)
    st.image("https://images.unsplash.com/photo-1583947581924-860b8ed4007a?auto=format&fit=crop&w=800&q=80", caption="Engineering movement.", use_container_width=True)

st.write("---")

# --- TECH SPECS (ICARUS DIFFERENCE) ---
st.markdown("<h2 style='text-align: center; margin-bottom: 40px;'>The Science of Unloading</h2>", unsafe_allow_html=True)

stat1, stat2, stat3, stat4 = st.columns(4)
with stat1:
    st.markdown('<div class="stat-box"><div class="stat-number">40 lbs</div><div class="stat-label">Offloading Capacity</div></div>', unsafe_allow_html=True)
with stat2:
    st.markdown('<div class="stat-box"><div class="stat-number">3D</div><div class="stat-label">Custom Printed</div></div>', unsafe_allow_html=True)
with stat3:
    st.markdown('<div class="stat-box"><div class="stat-number"> < 1lb</div><div class="stat-label">Ultra Lightweight</div></div>', unsafe_allow_html=True)
with stat4:
    st.markdown('<div class="stat-box"><div class="stat-number">USA</div><div class="stat-label">Made in America</div></div>', unsafe_allow_html=True)

st.write("---")

# --- PRODUCTS SECTION ---
st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>Our Custom Solutions</h3>", unsafe_allow_html=True)

# Função helper para cards
def product_card(name, subtitle, desc, img_url):
    st.markdown(f"""
    <div class="product-card">
        <img src="{img_url}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 10px;">
        <div class="product-name">{name}</div>
        <div style="color: #0056b3; font-weight: bold; font-size: 12px; margin-bottom: 10px;">{subtitle}</div>
        <div class="product-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)
    st.button(f"Learn about {name}", key=name)

p1, p2, p3 = st.columns(3)

with p1:
    product_card(
        "Ascender", 
        "UNLOADER KNEE BRACE",
        "Our flagship custom brace designed for maximum offloading of the knee joint. Ideal for Osteoarthritis.",
        "https://images.unsplash.com/photo-1584515933487-98db75f56f24?auto=format&fit=crop&w=400&q=80" # Placeholder mechanical/tech
    )

with p2:
    product_card(
        "Adonis", 
        "LIGHTWEIGHT SUPPORT",
        "Low profile design for active users requiring medial or lateral support without the bulk.",
        "https://images.unsplash.com/photo-1519311965067-36d3e5f33d39?auto=format&fit=crop&w=400&q=80" # Placeholder active
    )

with p3:
    product_card(
        "Kronos", 
        "POST-OP RECOVERY",
        "Adjustable ROM control and protection for patients recovering from ligament reconstruction.",
        "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=400&q=80" # Placeholder medical
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# --- HOW IT WORKS (STEPS) ---
st.markdown("<div style='background-color: #f4f6f9; padding: 40px; border-radius: 10px;'>", unsafe_allow_html=True)
st.subheader("How to get your Icarus Brace")

step1, step2, step3 = st.columns(3)
with step1:
    st.info("1. Scan")
    st.write("Download our app to take a precise 3D scan of your leg using your smartphone.")
with step2:
    st.info("2. Design & Print")
    st.write("Our engineers design a custom fit brace which is then 3D printed in Charlottesville, VA.")
with step3:
    st.info("3. Delivery")
    st.write("Receive your custom brace and get back to the activities you love, pain-free.")
st.markdown("</div>", unsafe_allow_html=True)

# --- CONTACT FORM SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
col_form, col_info = st.columns([2, 1])

with col_form:
    st.subheader("Get in Touch")
    with st.form("contact_form"):
        c_name, c_email = st.columns(2)
        c_name.text_input("First Name")
        c_email.text_input("Email Address")
        st.selectbox("I am a...", ["Patient", "Physician/Provider", "Distributor"])
        st.text_area("Message / Condition Description")
        st.form_submit_button("SEND MESSAGE")

with col_info:
    st.subheader("Contact Info")
    st.markdown("""
    **Icarus Medical** Charlottesville, VA  
    USA
    
    📧 support@icarusmedical.com  
    📞 (555) 123-4567
    """)

# --- FOOTER ---
st.markdown("""
<div class="footer-section">
    <p>ICARUS MEDICAL © 2024. All Rights Reserved.</p>
    <p>Privacy Policy | Terms of Use | Returns</p>
</div>
""", unsafe_allow_html=True)
