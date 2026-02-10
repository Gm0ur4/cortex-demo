# -*- coding: utf-8 -*-
"""
Blog Pessoal Interativo em Streamlit - Aurora Style

Autor: Manus AI
Data: 10 de Fevereiro de 2026

Um blog pessoal com design único, focado em animações e interações avançadas.
Estilo "Aurora" com fundos animados, cards com efeito 3D e cursor interativo.
"""

import streamlit as st
import pandas as pd

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(
    page_title="Blog Pessoal | Aurora",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DADOS FAKE PARA POSTS ---
def get_posts():
    return pd.DataFrame([
        {
            "title": "Explorando o Universo com Python",
            "date": "2026-02-10",
            "author": "Alex Cosmos",
            "category": "Tecnologia",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNTc5fDB8MXxzZWFyY2h8Mnx8dGVjaG5vbG9neXxlbnwwfHx8fDE2Mzg3NjYyMzk&ixlib=rb-1.2.1&q=80&w=1080",
            "excerpt": "Como a linguagem Python está sendo usada para analisar dados de telescópios e desvendar os segredos do universo..."
        },
        {
            "title": "A Arte da Visualização de Dados",
            "date": "2026-01-25",
            "author": "Clara Vis",
            "category": "Design",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNTc5fDB8MXxzZWFyY2h8MXx8ZGF0YSUyMHZpc3VhbGl6YXRpb258ZW58MHx8fHwxNjM4NzY2MzA5&ixlib=rb-1.2.1&q=80&w=1080",
            "excerpt": "Transforme números em histórias. Um guia completo sobre as melhores práticas e ferramentas para criar visualizações impactantes..."
        },
        {
            "title": "Mindfulness na Era Digital",
            "date": "2026-01-15",
            "author": "Paz Interior",
            "category": "Lifestyle",
            "image": "https://images.unsplash.com/photo-1506126613408-4e0e0f7c50e0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNTc5fDB8MXxzZWFyY2h8Mnx8bWluZGZ1bG5lc3N8ZW58MHx8fHwxNjM4NzY2MzY0&ixlib=rb-1.2.1&q=80&w=1080",
            "excerpt": "Como manter o foco e a calma em um mundo hiperconectado. Técnicas e dicas para uma vida digital mais saudável..."
        },
    ])

# --- INJETAR CSS E JAVASCRIPT ---
css_js = """
<style>
    /* === AURORA BACKGROUND === */
    body::before {
        content: 
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 20%, rgba(138, 43, 226, 0.3), transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(0, 255, 255, 0.3), transparent 40%);
        animation: aurora 15s linear infinite;
        pointer-events: none;
        z-index: -2;
    }
    body::after {
        content: 
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 50% 50%, rgba(255, 105, 180, 0.2), transparent 30%);
        animation: aurora-reverse 20s linear infinite;
        pointer-events: none;
        z-index: -1;
    }
    @keyframes aurora {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes aurora-reverse {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(-360deg); }
    }

    /* === ESTILOS GERAIS === */
    body {
        background-color: #0a0a1a !important;
        color: #e0e0e0;
    }
    .main {
        background: transparent !important;
    }

    /* === CURSOR INTERATIVO === */
    #cursor-glow {
        position: fixed;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(0, 255, 255, 0.15) 0%, transparent 60%);
        border-radius: 50%;
        pointer-events: none;
        transform: translate(-50%, -50%);
        transition: background 0.2s ease;
        z-index: -1;
    }

    /* === SIDEBAR === */
    .st-emotion-cache-16txtl3 {
        background: rgba(10, 10, 26, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 255, 255, 0.2);
    }
    .st-emotion-cache-16txtl3 h1 {
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff;
    }
    .st-emotion-cache-16txtl3 .st-emotion-cache-1d05278 a {
        color: #e0e0e0;
        transition: all 0.3s ease;
        border-left: 3px solid transparent;
    }
    .st-emotion-cache-16txtl3 .st-emotion-cache-1d05278 a:hover {
        color: #00ffff;
        background: rgba(0, 255, 255, 0.1);
        border-left: 3px solid #00ffff;
    }

    /* === CARDS DE POST === */
    .post-card-container {
        perspective: 1000px;
    }
    .post-card {
        background: rgba(20, 20, 40, 0.7);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        margin-bottom: 2rem;
    }
    .post-card:hover {
        transform: rotateY(5deg) rotateX(10deg) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        border-color: rgba(0, 255, 255, 0.5);
    }
    .post-card-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 1rem;
        opacity: 0.8;
        transition: opacity 0.3s ease;
    }
    .post-card:hover .post-card-image {
        opacity: 1;
    }
    .post-card h3 {
        color: #00ffff;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .post-card-meta {
        font-size: 0.9rem;
        color: #aaa;
        margin-bottom: 1rem;
    }
    .post-card-excerpt {
        color: #ccc;
    }
    .post-card-category {
        position: absolute;
        top: 1.5rem;
        right: 1.5rem;
        background: rgba(0, 255, 255, 0.2);
        color: #00ffff;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }

</style>

<div id="cursor-glow"></div>

<script>
    const cursorGlow = document.getElementById("cursor-glow");
    document.addEventListener("mousemove", (e) => {
        requestAnimationFrame(() => {
            cursorGlow.style.left = e.clientX + "px";
            cursorGlow.style.top = e.clientY + "px";
        });
    });
</script>
"""
st.markdown(css_js, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🌌 Aurora Blog")
    st.write("Um diário de explorações no universo da tecnologia e do design.")
    
    st.markdown("### Categorias")
    st.markdown("- [Tecnologia](#)")
    st.markdown("- [Design](#)")
    st.markdown("- [Lifestyle](#)")
    
    st.markdown("### Sobre Mim")
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&h=500&fit=crop", use_column_width=True)
    st.write("Olá! Sou um entusiasta de IA e design, explorando como a tecnologia pode criar experiências mais humanas e belas.")

# --- PÁGINA PRINCIPAL ---
st.title("Últimas Publicações")
st.markdown("Bem-vindo ao meu canto no universo digital. Aqui compartilho minhas ideias, projetos e descobertas.")

st.markdown("<hr style=\"border-color: rgba(0, 255, 255, 0.2);\">", unsafe_allow_html=True)

# --- GRID DE POSTS ---
posts_df = get_posts()

for index, row in posts_df.iterrows():
    st.markdown(f"""
    <div class="post-card-container">
        <div class="post-card">
            <div class="post-card-category">{row["category"]}</div>
            <img src="{row["image"]}" class="post-card-image">
            <h3>{row["title"]}</h3>
            <div class="post-card-meta">Por {row["author"]} | {row["date"]}</div>
            <p class="post-card-excerpt">{row["excerpt"]}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<hr style=\"border-color: rgba(0, 255, 255, 0.2);\">", unsafe_allow_html=True)
st.markdown("© 2026 Aurora Blog | Feito com ❤️ e Streamlit por Manus AI")
