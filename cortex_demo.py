import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="TinyTracks | Memórias da Infância",
    page_icon="🐾",
    layout="wide"
)

# --- CSS EXPANDIDO (TINYTRACKS STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&family=Quicksand:wght@400;500;700&display=swap');

    :root {
        --tiny-purple: #9d8df1;
        --tiny-blue: #a0d2eb;
        --tiny-pink: #ffafcc;
        --tiny-yellow: #ffee93;
        --tiny-bg: #fdfcf0;
    }

    .stApp {
        background-color: var(--tiny-bg);
        color: #4a4a4a;
    }

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Fredoka', sans-serif;
        color: #2d2d2d;
    }

    /* Navegação Superior */
    .nav-tiny {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 30px 8%;
        background: transparent;
    }
    .logo-tiny {
        font-family: 'Fredoka', sans-serif;
        font-size: 32px;
        color: var(--tiny-purple);
        font-weight: 600;
    }

    /* Hero Section */
    .hero-tiny {
        padding: 80px 8% 100px 8%;
        text-align: center;
    }
    .hero-h1 {
        font-size: clamp(45px, 7vw, 85px);
        line-height: 1.1;
        margin-bottom: 25px;
    }

    /* Cards e Containers Arredondados */
    .card-base {
        background: white;
        border-radius: 40px;
        padding: 40px;
        border: 2px solid #f0f0f0;
        transition: 0.3s;
    }

    /* Timeline Style */
    .timeline-item {
        border-left: 4px dashed var(--tiny-purple);
        padding-left: 30px;
        margin-left: 20px;
        position: relative;
        padding-bottom: 50px;
    }
    .timeline-circle {
        position: absolute;
        left: -14px;
        top: 0;
        width: 24px;
        height: 24px;
        background: var(--tiny-purple);
        border-radius: 50%;
        border: 4px solid white;
    }

    /* Pricing Table */
    .pricing-card {
        text-align: center;
        background: white;
        border-radius: 40px;
        padding: 50px 30px;
        border: 3px solid transparent;
        transition: 0.4s;
    }
    .pricing-card.popular {
        border-color: var(--tiny-purple);
        transform: scale(1.05);
        box-shadow: 0 20px 40px rgba(157,141,241,0.15);
    }

    /* Botões */
    div.stButton > button {
        background-color: var(--tiny-purple);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 18px 50px;
        font-family: 'Fredoka', sans-serif;
        font-size: 20px;
        font-weight: 500;
        box-shadow: 0 10px 20px rgba(157, 141, 241, 0.3);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(157, 141, 241, 0.5);
    }

    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO ---
st.markdown("""
<div class="nav-tiny">
    <div class="logo-tiny">🐾 tinytracks</div>
    <div style="display: flex; gap: 40px; font-weight: 700; color: #666; font-size: 15px;">
        <span>O App</span>
        <span>Funcionalidades</span>
        <span>Preços</span>
        <span style="color: var(--tiny-purple);">Login</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown('<div class="hero-tiny">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-h1">Guardar memórias <br><span style="color: #9d8df1;">nunca foi tão doce.</span></h1>', unsafe_allow_html=True)
st.markdown('<p style="max-width: 700px; font-size: 20px; color: #777; margin: 0 auto 40px auto; line-height: 1.6;">O diário digital inteligente que organiza os momentos mais preciosos dos seus filhos, para que você possa focar no que realmente importa: viver cada um deles.</p>', unsafe_allow_html=True)
st.button("Criar Minha Conta Grátis")
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. SEÇÃO DE FUNCIONALIDADES (CARDS) ---
st.markdown('<div style="padding: 0 8% 100px 8%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; margin-bottom: 60px; font-size: 42px;">Tudo o que você precisa</h2>', unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns(3, gap="large")

with f_col1:
    st.markdown("""
    <div class="card-base">
        <div style="font-size: 40px; margin-bottom: 20px;">📸</div>
        <h3>Organização Mágica</h3>
        <p style="color: #888; font-size: 16px;">Fotos e vídeos são organizados automaticamente por data e fase do crescimento.</p>
    </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.markdown("""
    <div class="card-base">
        <div style="font-size: 40px; margin-bottom: 20px;">👨‍👩‍👧‍👦</div>
        <h3>Círculo da Família</h3>
        <p style="color: #888; font-size: 16px;">Compartilhe momentos com avós e tios em um ambiente privado e seguro.</p>
    </div>
    """, unsafe_allow_html=True)

with f_col3:
    st.markdown("""
    <div class="card-base">
        <div style="font-size: 40px; margin-bottom: 20px;">🎨</div>
        <h3>Livros de Memórias</h3>
        <p style="color: #888; font-size: 16px;">Transforme seu diário digital em um álbum físico impresso com apenas um clique.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. SEÇÃO "TIMELINE" (SIMULAÇÃO DO APP) ---
st.markdown("""
<div style="background-color: white; padding: 100px 8%; border-radius: 80px 80px 0 0;">
    <div style="display: flex; align-items: center; gap: 80px; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px;">
            <h2 style="font-size: 48px; margin-bottom: 30px;">Uma linha do tempo da vida deles</h2>
            <div class="timeline-item">
                <div class="timeline-circle"></div>
                <h4 style="color: var(--tiny-purple);">Hoje - 2 Anos e 3 Meses</h4>
                <p>O primeiro dia na escolinha! Nenhuma lágrima (pelo menos não do Leo).</p>
            </div>
            <div class="timeline-item">
                <div class="timeline-circle"></div>
                <h4 style="color: #666;">Há 6 meses</h4>
                <p>Primeiros passos no jardim. Foram 4 passos inteiros!</p>
            </div>
            <div class="timeline-item" style="border: none;">
                <div class="timeline-circle"></div>
                <h4 style="color: #666;">O Nascimento</h4>
                <p>O começo da trilha mais linda de nossas vidas.</p>
            </div>
        </div>
        <div style="flex: 1; min-width: 300px;">
            <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800" style="width: 100%; border-radius: 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.1);">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. SEÇÃO DE DEPOIMENTOS ---
st.markdown("""
<div style="background-color: #a0d2eb; padding: 120px 8%; text-align: center;">
    <h2 style="color: white; font-size: 42px; margin-bottom: 60px;">Amado por mais de 50.000 famílias</h2>
    <div style="display: flex; gap: 30px; justify-content: center; flex-wrap: wrap;">
        <div style="background: white; padding: 40px; border-radius: 30px; max-width: 350px;">
            <p style="font-style: italic; color: #555;">"O TinyTracks mudou a forma como guardo as fotos da minha filha. É tão fácil de usar e as sugestões de marcos são incríveis!"</p>
            <p style="margin-top: 20px; font-weight: 700;">— Mariana S., Mãe da Alice</p>
        </div>
        <div style="background: white; padding: 40px; border-radius: 30px; max-width: 350px;">
            <p style="font-style: italic; color: #555;">"Finalmente um lugar seguro para compartilhar fotos com a família sem precisar das redes sociais abertas."</p>
            <p style="margin-top: 20px; font-weight: 700;">— Ricardo T., Pai do Bento</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. SEÇÃO DE PREÇOS (PRICING) ---
st.markdown('<div style="padding: 120px 8%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; margin-bottom: 20px; font-size: 42px;">Escolha o seu plano</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #888; margin-bottom: 60px;">Sem taxas escondidas. Cancele quando quiser.</p>', unsafe_allow_html=True)

p_col1, p_col2, p_col3 = st.columns(3, gap="large")

with p_col1:
    st.markdown("""
    <div class="pricing-card">
        <h3>Básico</h3>
        <h2 style="font-size: 48px; margin: 20px 0;">Grátis</h2>
        <p style="color: #888;">Para começar a trilha</p>
        <ul style="text-align: left; margin: 30px 0; font-size: 14px; line-height: 2;">
            <li>✓ Até 500 fotos</li>
            <li>✓ 1 Perfil de criança</li>
            <li>✓ Álbum digital básico</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("Escolher Básico", key="btn_base")

with p_col2:
    st.markdown("""
    <div class="pricing-card popular">
        <span style="background: var(--tiny-purple); color: white; padding: 5px 15px; border-radius: 20px; font-size: 12px; font-weight: 700;">MAIS POPULAR</span>
        <h3 style="margin-top: 20px;">Premium</h3>
        <h2 style="font-size: 48px; margin: 20px 0;">R$ 19<span style="font-size: 18px;">/mês</span></h2>
        <p style="color: #888;">Para memórias infinitas</p>
        <ul style="text-align: left; margin: 30px 0; font-size: 14px; line-height: 2;">
            <li>✓ Armazenamento Ilimitado</li>
            <li>✓ Vídeos em 4K</li>
            <li>✓ Compartilhamento ilimitado</li>
            <li>✓ Backup automático</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("Assinar Premium", key="btn_prem")

with p_col3:
    st.markdown("""
    <div class="pricing-card">
        <h3>Família</h3>
        <h2 style="font-size: 48px; margin: 20px 0;">R$ 35<span style="font-size: 18px;">/mês</span></h2>
        <p style="color: #888;">Para toda a árvore genealógica</p>
        <ul style="text-align: left; margin: 30px 0; font-size: 14px; line-height: 2;">
            <li>✓ Tudo do Premium</li>
            <li>✓ Até 5 perfis de crianças</li>
            <li>✓ Acesso de Admin para 4 pessoas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("Escolher Família", key="btn_fam")
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. SEÇÃO FAQ ---
st.markdown('<div style="background: #f0f9ff; padding: 100px 20%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; margin-bottom: 50px;">Dúvidas Frequentes</h2>', unsafe_allow_html=True)

with st.expander("Meus dados estão seguros?"):
    st.write("Sim! Utilizamos criptografia de nível bancário e seus dados nunca são vendidos para terceiros.")

with st.expander("Posso imprimir os álbuns no Brasil?"):
    st.write("Sim, temos parceiros de impressão locais que entregam em todo o território nacional com acabamento premium.")

with st.expander("Como convido os avós?"):
    st.write("Basta enviar um link mágico pelo WhatsApp ou e-mail. Eles não precisam criar senhas complicadas.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FOOTER ---
st.markdown("""
<div style="padding: 100px 8% 50px 8%; text-align: center;">
    <div class="logo-tiny" style="margin-bottom: 30px;">🐾 tinytracks</div>
    <div style="display: flex; justify-content: center; gap: 50px; margin-bottom: 40px; font-weight: 600; color: #777;">
        <span>Instagram</span>
        <span>Facebook</span>
        <span>Blog</span>
        <span>Termos de Uso</span>
    </div>
    <p style="color: #bbb; font-size: 13px;">© 2026 TinyTracks. Criado com ❤️ para as futuras gerações.</p>
</div>
""", unsafe_allow_html=True)
