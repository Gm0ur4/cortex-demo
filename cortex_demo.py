import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Site Pro Elite | Templates Fora de Série",
    page_icon="💎",
    layout="wide"
)

# --- CSS RADICAL (PLUNDER + DOCKYARD + QUDRIX) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&family=Oswald:wght@700&display=swap');

    :root {
        --accent: #7b2cbf; /* Roxo Profundo */
        --gold: #d4af37;
        --dark: #050505;
        --glass: rgba(255, 255, 255, 0.03);
    }

    .stApp {
        background-color: var(--dark);
        color: #ffffff;
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia de Impacto Brutalista */
    h1, h2 {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -3px;
        line-height: 0.85;
    }

    .serif-heavy {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        text-transform: none;
        letter-spacing: -1px;
    }

    /* 1 & 2. HERO RADICAL */
    .hero-section {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 8%;
        background: radial-gradient(circle at 80% 20%, #5800AB 0%, #050505 50%);
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .hero-h1 { font-size: clamp(60px, 15vw, 180px); margin-bottom: 40px; }
    .hero-sub { 
        font-size: 24px; 
        max-width: 600px; 
        line-height: 1.4; 
        color: rgba(255,255,255,0.7);
        border-left: 4px solid var(--accent);
        padding-left: 20px;
    }

    /* 3 & 4. TEMPLATES SHOWCASE (ASSIMÉTRICO) */
    .template-box {
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
        background: var(--glass);
        transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        cursor: crosshair;
    }
    .template-box:hover {
        background: rgba(255,255,255,0.07);
        border-color: var(--gold);
        transform: translateY(-10px);
    }
    .template-label {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Oswald', sans-serif;
        font-size: 30px;
    }

    /* 5. CLIENTS (FLOATING AVATARS) */
    .client-section {
        padding: 100px 8%;
        background: #0a0a0a;
        display: flex;
        align-items: center;
        gap: 50px;
    }

    /* 6. É PARA VOCÊ QUE (CARDS NEO-BRUTALISTAS) */
    .target-card {
        padding: 50px;
        background: white;
        color: black;
        border: 5px solid var(--accent);
        box-shadow: 15px 15px 0px var(--accent);
        height: 100%;
    }

    /* 7. PASSO A PASSO (VERTICAL & BOLD) */
    .step-row {
        display: flex;
        gap: 30px;
        margin-bottom: 60px;
        align-items: flex-start;
    }
    .step-num {
        font-size: 100px;
        font-weight: 900;
        color: transparent;
        -webkit-text-stroke: 1px rgba(255,255,255,0.3);
        line-height: 0.7;
    }

    /* 8. PREÇOS (GLASSMORPHISM) */
    .pricing-glass {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 60px 40px;
        border-radius: 2px;
        text-align: center;
    }
    .pricing-glass:hover {
        border-color: var(--accent);
    }

    /* Botão de Alta Conversão */
    div.stButton > button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd);
        color: white;
        border: none;
        padding: 25px 60px;
        font-weight: 900;
        font-size: 22px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 0;
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0% 100%);
        transition: 0.4s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(123, 44, 191, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# --- 1 & 2. HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-h1">Crie seu site profissional em minutos<br><span class="serif-heavy" style="color:var(--gold)">Apenas editando templates prontos.</span></h1>
    <p class="hero-sub">A solução ideal para quem precisa de um site rápido, profissional e editável sem depender de agências ou programadores.</p>
    <div style="margin-top: 50px; width: 300px;">
""", unsafe_allow_html=True)
st.button("CONHEÇA NOSSOS TEMPLATES ↓")
st.markdown("</div></div>", unsafe_allow_html=True)

# --- 3 & 4. SHOWCASE DE TEMPLATES (GRID ASSIMÉTRICO) ---
st.markdown('<div style="padding: 120px 8%;">', unsafe_allow_html=True)
st.markdown('<h2>ENCONTRE O DESIGN QUE MELHOR DEFINE <span class="serif-heavy">seu negócio.</span></h2><br><br>', unsafe_allow_html=True)

col_t1, col_t2 = st.columns([2, 1])

with col_t1:
    st.markdown("""
    <div class="template-box" style="height: 600px;">
        <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200" style="width:100%; height:100%; object-fit:cover; opacity: 0.6;">
        <div class="template-label">01. THE ULTIMATE SAAS <br><span style="font-size: 14px; letter-spacing: 3px; color: var(--gold);">ESTILO QUDRIX</span></div>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div class="template-box" style="height: 285px; margin-bottom: 30px;">
        <img src="https://images.unsplash.com/photo-1558655146-d09347e92766?w=600" style="width:100%; height:100%; object-fit:cover; opacity: 0.4;">
        <div class="template-label" style="font-size: 20px;">02. LUXURY DECOR</div>
    </div>
    <div class="template-box" style="height: 285px;">
        <img src="https://images.unsplash.com/photo-1549490349-8643362247b5?w=600" style="width:100%; height:100%; object-fit:cover; opacity: 0.4;">
        <div class="template-label" style="font-size: 20px;">03. MODERN VINTAGE</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- NOVO: SHOWCASE SIMÉTRICO COM SCROLL (USANDO STREAMLIT COMPONENTS) ---
st.markdown('<div style="padding: 120px 8%; background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 100%);"><h2 style="text-align: center; font-size: 48px; font-family: \'Inter\', sans-serif; color: #ffffff; margin-bottom: 80px; font-weight: 900; text-transform: uppercase; letter-spacing: -2px;">Veja Nossos Templates em Ação</h2>', unsafe_allow_html=True)

# Template 1
col1_img, col1_text = st.columns([1.2, 1], gap="large")

with col1_img:
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800", use_container_width=True)

with col1_text:
    st.markdown('<p style="color: #d4af37; font-weight: 900; text-transform: uppercase; letter-spacing: 3px; font-size: 14px;">Template 01</p>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-size: 42px; font-family: \'Inter\', sans-serif; color: #ffffff; margin: 15px 0; font-weight: 900; text-transform: uppercase; letter-spacing: -2px;">The Ultimate SaaS</h3>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 18px; color: rgba(255,255,255,0.7); line-height: 1.8; margin-bottom: 30px;">Uma visualização elegante e poderosa para apresentar sua solução SaaS. Design moderno com foco em conversão e experiência do usuário de alto nível.</p>', unsafe_allow_html=True)
    
    st.markdown('<div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 30px;">', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Seções otimizadas para conversão</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Responsivo em todos os dispositivos</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Integração com ferramentas de CRM</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Análise de performance incluída</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.button("Explorar Template", key="btn_template_1", use_container_width=False)

st.markdown('<div style="margin: 80px 0;"></div>', unsafe_allow_html=True)

# Template 2
col2_text, col2_img = st.columns([1, 1.2], gap="large")

with col2_text:
    st.markdown('<p style="color: #d4af37; font-weight: 900; text-transform: uppercase; letter-spacing: 3px; font-size: 14px;">Template 02</p>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-size: 42px; font-family: \'Inter\', sans-serif; color: #ffffff; margin: 15px 0; font-weight: 900; text-transform: uppercase; letter-spacing: -2px;">Luxury Decor</h3>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 18px; color: rgba(255,255,255,0.7); line-height: 1.8; margin-bottom: 30px;">Design premium para marcas de luxo e decoração. Elegância, sofisticação e um toque de exclusividade em cada detalhe visual.</p>', unsafe_allow_html=True)
    
    st.markdown('<div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 30px;">', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Galeria de produtos em alta resolução</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Efeitos visuais premium</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Carrinho de compras integrado</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Sistema de avaliações e reviews</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.button("Explorar Template", key="btn_template_2", use_container_width=False)

with col2_img:
    st.image("https://images.unsplash.com/photo-1558655146-d09347e92766?w=800", use_container_width=True)

st.markdown('<div style="margin: 80px 0;"></div>', unsafe_allow_html=True)

# Template 3
col3_img, col3_text = st.columns([1.2, 1], gap="large")

with col3_img:
    st.image("https://images.unsplash.com/photo-1549490349-8643362247b5?w=800", use_container_width=True)

with col3_text:
    st.markdown('<p style="color: #d4af37; font-weight: 900; text-transform: uppercase; letter-spacing: 3px; font-size: 14px;">Template 03</p>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-size: 42px; font-family: \'Inter\', sans-serif; color: #ffffff; margin: 15px 0; font-weight: 900; text-transform: uppercase; letter-spacing: -2px;">Modern Vintage</h3>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 18px; color: rgba(255,255,255,0.7); line-height: 1.8; margin-bottom: 30px;">Fusão perfeita entre o clássico e o contemporâneo. Ideal para negócios que buscam transmitir tradição com uma abordagem moderna e inovadora.</p>', unsafe_allow_html=True)
    
    st.markdown('<div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 30px;">', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Timeline de histórias e marcos</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Blog integrado com SEO otimizado</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Formulários de contato avançados</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 16px;"><span style="color: #d4af37; font-weight: 900; font-size: 20px;">✓</span> Integração com redes sociais</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.button("Explorar Template", key="btn_template_3", use_container_width=False)

st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PROVA SOCIAL (AVATARES FLOATING) ---
st.markdown("""
<div class="client-section">
    <h2 style="font-size: 30px; letter-spacing: 0px;">CONFIE EM QUEM<br>JÁ DOMINA.</h2>
    <div style="display: flex;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/7.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/8.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/6.jpg" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <img src="https://raw.githubusercontent.com/Gm0ur4/cortex-checkout/main/17.png" style="width:80px; height:80px; border-radius:50%; border: 2px solid var(--accent); margin-left: -20px;">
        <div style="width:80px; height:80px; border-radius:50%; background: var(--accent); margin-left: -20px; display:flex; align-items:center; justify-content:center; font-weight:900;">+500</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. É PARA VOCÊ QUE ---
st.markdown('<div style="padding: 120px 8%;">', unsafe_allow_html=True)
col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.markdown("""
    <div class="target-card">
        <h3>Proprietários de negócios</h3>
        <p>Que busca colocar sua empresa na internet com o menor custo do mercado, garantindo sua presença digital em minutos.</p>
    </div>
    """, unsafe_allow_html=True)

with col_u2:
    st.markdown("""
    <div class="target-card" style="background: var(--accent); color: white; box-shadow: 15px 15px 0px white;">
        <h3>Infoprodutores/ prestadores de serviço</h3>
        <p>Temos estruturas otimizadas para converter visitantes em compradores reais. Destaque seus serviços com um design que transmite autoridade e confiança.</p>
    </div>
    """, unsafe_allow_html=True)

with col_u3:
    st.markdown("""
    <div class="target-card">
        <h3>Freelancer</h3>
        <p>Venda nossos sites para seus clientes sem precisar programar do zero e fature com isso, aumentando sua margem de lucro entregando em tempo recorde.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. PASSO A PASSO (INDUSTRIAL) ---
st.markdown('<div style="padding: 100px 8%; background: #050505;">', unsafe_allow_html=True)
st.markdown('<h2>PROCESSO <span class="serif-heavy">sem falhas.</span></h2><br><br>', unsafe_allow_html=True)

steps = [
    ("SELECIONE O MODELO IDEAL", "Escolha entre mais de 30 modelos validados o que mais combina com a identidade do seu negócio."),
    ("CUSTOMIZAÇÃO RÁPIDA", "Utilize nosso passo a passo detalhado para implementar o código e personalizar cada detalhe sem complicações."),
    ("SETUP TÉCNICO GRATUITO", "Te ensinamos onde hospedar seu site em segundos, como aplicar técnicas de SEO e configurar seu domínio personalizado sem custo adicional e de forma rápida."),
    ("LANÇAMENTO IMEDIATO", "Site no ar, otimizado e pronto para escalar seu negócio com uma estrutura de alta performance.")
]

for i, (title, desc) in enumerate(steps):
    st.markdown(f"""
    <div class="step-row">
        <div class="step-num">0{i+1}</div>
        <div>
            <h3 style="color: var(--gold);">{title}</h3>
            <p style="max-width: 400px; opacity: 0.6;">{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. PREÇOS (ELITE) ---
st.markdown('<div style="padding: 120px 8%; text-align:center;">', unsafe_allow_html=True)
st.markdown('<h2>INVISTA NA SUA <span class="serif-heavy">Presença.</span></h2><br><br>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p2: # Featured
    st.markdown("""
    <div class="pricing-glass" style="border-top: 5px solid var(--accent);">
        <p style="color: var(--gold); letter-spacing: 3px; font-weight: 900;">PROFESSIONAL</p>
        <h1 style="font-size: 80px; margin: 30px 0;">R$ 197</h1>
        <p>✓ Acesso vitalício aos templates atuais</p>
        <p>✓ 02 consultorias mensais para customização</p>
        <p>✓ Pagamento mensal</p>
        <p>✓ Manual completo de customização e setup</p>
        <p>✓ Suporte técnico ágil via e-mail</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Atualizações de novos templates inclusas</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("QUERO O ELITE BUNDLE", key="main_p")

with p1:
    st.markdown("""
    <div class="pricing-glass">
        <p>STARTER</p>
        <h1 style="font-size: 60px; margin: 30px 0;">R$ 67</h1>
        <p>✓ Acesso vitalício aos templates atuais</p>
        <p>✓ Pagamento único</p>
        <p>✓ Manual completo de customização e setup</p>
        <p>✓ Suporte técnico ágil via e-mail</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Atualizações de novos templates inclusas</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("INICIAR", key="p1")

with p3:
    st.markdown("""
    <div class="pricing-glass">
        <p>BUSINESS</p>
        <h1 style="font-size: 60px; margin: 30px 0;">R$ 297</h1>
        <p>✓ Acesso vitalício aos templates atuais</p>
        <p>✓ Pagamento mensal</p>
        <p>✓ Licença comercial para revenda ilimitada</p>
        <p>✓ Selo de parceiro desenvolvedor</p>
        <p>✓ Manual completo de customização e setup</p>
        <p>✓ Suporte técnico ágil via e-mail</p>
        <p>✓ Acesso imediato</p>
        <p>✓ Atualizações de novos templates inclusas</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("SER VITALÍCIO", key="p3")
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FAQ ---
st.markdown('<div style="padding: 100px 20%; background: #080808;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center; font-size: 40px;">FAQ / <span class="serif-heavy">Respostas.</span></h2><br>', unsafe_allow_html=True)

faq = {
    "Preciso saber programação para usar os templates?": "Não é preciso. O código é entregue pronto e você segue o nosso guia detalhado para personalizar os textos, cores, imagens e o que precisar.",
    "É seguro realizar a compra?": "Sim! Toda a compra é processada pela Eduzz, uma das plataformas de pagamentos e educação mais seguras e reconhecidas do Brasil. Nenhum dado sensível passa por nós, tudo ocorre diretamente no ambiente da Eduzz, com criptografia, certificados de segurança e antifraude.",
    "Existe algum tipo de suporte?": "Com certeza. Todos os planos incluem suporte humano ágil via e-mail e com o plano professional você tem direito a 2 consultorias mensais para customização.",
    "Por onde acesso os templates?": "O acesso é 100% digital e imediato. Após a confirmação do pagamento, você receberá um e-mail da Eduzz com seus dados de acesso à área de membros. Lá, você encontrará os arquivos de todos os templates, além dos guias de setup e explicações organizados por módulos.",
    "A hospedagem é mesmo gratuita?": "Sim. Nosso método utiliza infraestruturas globais de alta performance que permitem manter sites profissionais online sem mensalidades de hospedagem. No passo a passo, ensinamos como configurar essa estrutura gratuita de forma segura, garantindo que você tenha um site rápido e estável sem custos fixos recorrentes.",
    "Posso vender os sites para clientes?": "Com o plano Business, você tem licença comercial completa para lucrar com nossos designs."
}

for q, a in faq.items():
    with st.expander(q):
        st.markdown(f"<p style='color: #ccc;'>{a}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="padding: 60px 8%; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; font-size: 10px; opacity: 0.4; letter-spacing: 5px;">
    SITE PRO ELITE // DOMINANDO A WEB EM 2026
</div>
""", unsafe_allow_html=True)
