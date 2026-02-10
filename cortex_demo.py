import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="What Is Missing? | Memorial Global",
    page_icon="🌏",
    layout="wide"
)

# --- CSS DE ALTA FIDELIDADE (ATMOSFERA MAYA LIN) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300&family=Inter:wght@200;300&display=swap');

    /* Fundo Escuro Absoluto */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }

    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia Etérea */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-weight: 200;
    }

    h1, h2, .serif-italic {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* Navegação de Cantos */
    .corner-nav {
        position: fixed;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: rgba(255,255,255,0.6);
        z-index: 1000;
        padding: 40px;
    }

    /* Hero Central */
    .hero-missing {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: radial-gradient(circle, rgba(40,40,40,1) 0%, rgba(0,0,0,1) 70%);
    }

    /* Pontos de Luz (Partículas) */
    .particle {
        position: absolute;
        background: white;
        border-radius: 50%;
        opacity: 0.4;
        filter: blur(1px);
    }

    /* Seções de Conteúdo */
    .content-block {
        padding: 150px 20%;
        line-height: 2;
        font-size: 18px;
        color: rgba(255,255,255,0.8);
    }

    .stat-number {
        font-size: 60px;
        color: #fff;
        margin-bottom: 20px;
    }

    /* Linha do Tempo de Extinção */
    .extinction-item {
        border-left: 1px solid rgba(255,255,255,0.2);
        padding-left: 30px;
        margin-bottom: 80px;
        transition: 0.5s;
    }
    .extinction-item:hover {
        border-left: 1px solid #fff;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. NAVEGAÇÃO DE CANTOS ---
st.markdown('<div class="corner-nav" style="top:0; left:0;">What is Missing?</div>', unsafe_allow_html=True)
st.markdown('<div class="corner-nav" style="top:0; right:0;">Memorial / Mapa / Ação</div>', unsafe_allow_html=True)
st.markdown('<div class="corner-nav" style="bottom:0; left:0;">Maya Lin Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="corner-nav" style="bottom:0; right:0;">Contribuir</div>', unsafe_allow_html=True)

# --- 2. HERO (O VAZIO) ---
st.markdown("""
<div class="hero-missing">
    <div class="particle" style="top:20%; left:15%; width:4px; height:4px;"></div>
    <div class="particle" style="top:60%; left:80%; width:2px; height:2px;"></div>
    <div class="particle" style="top:40%; left:50%; width:3px; height:3px; opacity:0.8;"></div>
    <h1 style="font-size: 50px; margin-bottom: 20px;">O que está desaparecendo?</h1>
    <p class="serif-italic" style="font-size: 24px; color: rgba(255,255,255,0.5);">
        Um memorial para a sexta extinção em massa.
    </p>
    <div style="margin-top: 50px; width: 1px; height: 100px; background: linear-gradient(to bottom, white, transparent);"></div>
</div>
""", unsafe_allow_html=True)

# --- 3. MANIFESTO ---
st.markdown("""
<div class="content-block">
    <h2 class="serif-italic" style="font-size: 42px; color: #fff; text-align: center; margin-bottom: 60px;">
        Nós não podemos proteger o que não lembramos.
    </h2>
    <p>
        "What Is Missing?" é um memorial permanente dedicado às espécies e habitats que já perdemos e àqueles que ainda podemos salvar. 
        Ao contrário de um memorial físico estático, ele vive no espaço digital, conectando histórias de extinção com soluções para o futuro.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. ESTATÍSTICAS SILENCIOSAS ---
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style="padding: 100px 10% 100px 20%;">
        <div class="stat-number serif-italic">70%</div>
        <p style="font-size: 14px; text-transform: uppercase; letter-spacing: 2px;">
            Da vida selvagem do planeta desapareceu nos últimos 50 anos.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding: 100px 20% 100px 10%;">
        <div class="stat-number serif-italic">1 Milhão</div>
        <p style="font-size: 14px; text-transform: uppercase; letter-spacing: 2px;">
            De espécies estão atualmente sob risco de extinção.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. LINHA DO TEMPO DE MEMÓRIAS (EXTINÇÃO) ---
st.markdown('<div class="content-block" style="padding-top: 50px;">', unsafe_allow_html=True)
st.markdown('<h3 style="margin-bottom: 100px; font-size: 12px; letter-spacing: 4px; text-align: center;">MEMÓRIAS DO QUE SE FOI</h3>', unsafe_allow_html=True)

def render_memory(year, title, desc):
    st.markdown(f"""
    <div class="extinction-item">
        <span style="font-size: 12px; opacity: 0.5;">{year}</span>
        <h3 class="serif-italic" style="font-size: 28px; margin: 10px 0;">{title}</h3>
        <p style="font-size: 15px; opacity: 0.7;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

render_memory("1900s", "O Céu Escurecido", "Relatos de quando os bandos de pombos-passageiros eram tão vastos que bloqueavam o sol por horas em sua passagem.")
render_memory("1950s", "Silêncio nos Rios", "O desaparecimento gradual do esturjão e de outras espécies migratórias que antes fervilhavam nas águas doces.")
render_memory("2024", "O Canto Solitário", "O último registro sonoro de espécies de pássaros em florestas tropicais que não encontram mais pares para acasalamento.")

st.markdown('</div>', unsafe_allow_html=True)

# --- 6. CHAMADA PARA AÇÃO (O MAPA DA ESPERANÇA) ---
st.markdown("""
<div style="background: white; color: black; padding: 150px 8%; text-align: center;">
    <h2 class="serif-italic" style="font-size: 50px; margin-bottom: 30px;">Ainda há tempo.</h2>
    <p style="max-width: 800px; margin: 0 auto 50px auto; font-size: 18px; line-height: 1.8;">
        O projeto também destaca planos de conservação e visões de um mundo onde a humanidade e a natureza coexistem em equilíbrio. 
        Proteja um habitat. Restaure uma floresta. Reduza sua pegada.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("""
<div style="padding: 100px 8%; text-align: center; color: rgba(255,255,255,0.3); font-size: 11px; letter-spacing: 2px;">
    WHAT IS MISSING? FOUNDATION © 2026 <br>
    CIÊNCIA / ARTE / ATIVISMO
</div>
""", unsafe_allow_html=True)
