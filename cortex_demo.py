import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Crehana Clone | Cursos Online",
    page_icon="🎓",
    layout="wide"
)

# --- CSS PARA ESTILO EDTECH (CREHANA STYLE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1b1c1e;
    }

    /* Header Estilo App */
    .header-crehana {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 30px;
    }
    .logo {
        font-size: 24px;
        font-weight: 800;
        color: #4b22b4; /* Roxo Crehana */
    }

    /* Hero Section */
    .hero-title {
        font-size: 42px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 20px;
    }
    .highlight {
        color: #4b22b4;
    }

    /* Botões de Ação */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
        border: none;
    }
    /* Botão Principal (Roxo) */
    div.stButton > button:first-child {
        background-color: #4b22b4;
        color: white;
    }
    
    /* Card de Curso */
    .course-card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #efefef;
        transition: transform 0.3s;
        margin-bottom: 20px;
    }
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    .category-tag {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        color: #888;
        margin-bottom: 5px;
    }
    .course-title {
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 8px;
    }
    .rating {
        color: #ffb400;
        font-size: 14px;
        font-weight: bold;
    }

    /* Barra de busca simulada */
    .search-bar {
        background-color: #f4f4f7;
        padding: 10px 20px;
        border-radius: 25px;
        border: 1px solid #e0e0e0;
        color: #777;
        width: 300px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. HEADER ---
col_l, col_m, col_r = st.columns([1, 2, 2])
with col_l:
    st.markdown('<div class="logo">crehana</div>', unsafe_allow_html=True)
with col_m:
    # Simulando links de categoria
    st.markdown("""
    <div style="display: flex; gap: 20px; padding-top: 10px;">
        <span style="font-weight:600; font-size:14px;">Categorias</span>
        <span style="font-weight:600; font-size:14px;">Para Empresas</span>
    </div>
    """, unsafe_allow_html=True)
with col_r:
    # Botões de Login
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1: st.markdown('<div class="search-bar">O que você quer aprender?</div>', unsafe_allow_html=True)
    with c2: st.button("Entrar", key="login")
    with c3: st.button("Criar conta", key="signup")

st.write("---")

# --- 2. HERO SECTION ---
c_hero1, c_hero2 = st.columns([1, 1])

with c_hero1:
    st.markdown('<p style="color:#4b22b4; font-weight:700;">MAIS DE 1000 CURSOS ONLINE</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Aumente suas <span class="highlight">oportunidades</span> profissionais</h1>', unsafe_allow_html=True)
    st.write("Aprenda com especialistas as habilidades mais demandadas no mercado digital. Do zero ao avançado.")
    st.write("")
    st.button("🎯 Explorar cursos agora", use_container_width=False)

with c_hero2:
    # Imagem de uma pessoa estudando (estilo clean)
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80", use_container_width=True)

st.write("### O que você quer estudar hoje?")

# --- 3. CURSOS (GRID) ---
def course_item(col, img, category, title, rating, students):
    with col:
        st.markdown(f"""
        <div class="course-card">
            <img src="{img}" style="width:100%; height:150px; object-fit:cover;">
            <div style="padding: 15px;">
                <div class="category-tag">{category}</div>
                <div class="course-title">{title}</div>
                <div class="rating">★ {rating} <span style="color:#888; font-weight:400; font-size:12px;">({students})</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Ver detalhes", key=title)

col1, col2, col3, col4 = st.columns(4)

course_item(col1, 
            "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80",
            "Marketing Digital", "Facebook Ads: Domine o Gerenciador", "4.8", "12k alunos")

course_item(col2, 
            "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=400&q=80",
            "Design", "Adobe Illustrator: Ilustração Vetorial", "4.9", "45k alunos")

course_item(col3, 
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=400&q=80",
            "Tecnologia", "Introdução ao Desenvolvimento Web", "4.7", "30k alunos")

course_item(col4, 
            "https://images.unsplash.com/photo-1551288049-bbbda536339a?auto=format&fit=crop&w=400&q=80",
            "Dados", "Excel para Negócios: Avançado", "4.9", "18k alunos")

# --- 4. SEÇÃO "CREHANA PARA EMPRESAS" ---
st.write("")
st.write("---")
with st.container():
    ce1, ce2 = st.columns([1, 1])
    with ce1:
        st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80", use_container_width=True)
    with ce2:
        st.markdown("## Treine sua equipe com a Crehana")
        st.write("Soluções de SaaS e conteúdo para fechar a lacuna de habilidades na sua empresa.")
        st.write("✅ Planos de aprendizado personalizados")
        st.write("✅ Painel de controle para o RH")
        st.button("🚀 Solicitar Demo", key="demo")

# --- FOOTER ---
st.markdown("""
<div style="background-color: #1b1c1e; color: white; padding: 60px 20px; margin-top: 50px; text-align: center;">
    <div style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">crehana</div>
    <div style="color: #888; font-size: 14px;">
        Transformando o futuro através da educação. <br>
        © 2024 Crehana Inc. Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
