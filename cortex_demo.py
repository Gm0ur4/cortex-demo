# -*- coding: utf-8 -*-
"""
Blog Pessoal Ultra Sofisticado - Cosmic Flare

Autor: Manus AI
Data: 10 de Fevereiro de 2026

Uma versão ultra sofisticada com design rico, paleta de cores vibrantes (laranja, amarelo, lilás),
e animações e interações de nível profissional para uma experiência imersiva.
"""

import streamlit as st
import pandas as pd

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(
    page_title="Blog | Cosmic Flare",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DADOS FAKE PARA POSTS ---
def get_posts():
    return pd.DataFrame([
        {"title": "A Nova Era da Computação Quântica", "date": "2026-02-10", "author": "Dr. Evelyn Reed", "category": "Futurismo", "image": "https://images.unsplash.com/photo-1532187863486-abf9db5a92b1?w=800", "read_time": 8, "excerpt": "Explore como os computadores quânticos estão revolucionando a forma como processamos informações e resolvemos problemas complexos."},
        {"title": "Design Biofílico: Conectando Arquitetura e Natureza", "date": "2026-01-28", "author": "Elena Verde", "category": "Design", "image": "https://images.unsplash.com/photo-1462536943532-57a629292d3a?w=800", "read_time": 6, "excerpt": "Descubra como integrar elementos naturais no design de espaços para criar ambientes mais saudáveis e inspiradores."},
        {"title": "Desvendando os Segredos do Deep Learning", "date": "2026-01-15", "author": "Alex Turing", "category": "IA", "image": "https://images.unsplash.com/photo-1611193310522-26d5a5c51482?w=800", "read_time": 12, "excerpt": "Uma jornada profunda pelas redes neurais, algoritmos e as aplicações práticas que estão transformando a IA."},
        {"title": "A Psicologia das Cores no Branding Moderno", "date": "2025-12-20", "author": "Iris Cromia", "category": "Marketing", "image": "https://images.unsplash.com/photo-1558637845-c8b7ead71a3e?w=800", "read_time": 7, "excerpt": "Entenda como as cores influenciam a percepção do consumidor e criam identidades visuais memoráveis."},
    ])

# --- CSS E JAVASCRIPT ---
css_js = """
<style>
    :root {
        --orange: #ff8c00;
        --yellow: #ffd700;
        --lilac: #c8a2c8;
        --dark-bg: #120c18;
        --card-bg: rgba(25, 18, 35, 0.7);
        --text-light: #f0e6f6;
        --text-muted: #a999b3;
    }

    body {
        background-color: var(--dark-bg) !important;
        color: var(--text-light);
        overflow-x: hidden;
    }

    .main { background: transparent !important; }

    /* --- Fundo Animado --- */
    #bg-animation {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        z-index: -2; pointer-events: none;
    }

    /* --- Header --- */
    .main-header {
        text-align: center; padding: 4rem 2rem; border-bottom: 1px solid rgba(200, 162, 200, 0.2);
        position: relative;
    }
    .main-header h1 {
        font-size: 4rem; font-weight: 900;
        background: linear-gradient(135deg, var(--orange), var(--yellow), var(--lilac));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        animation: text-glow 3s ease-in-out infinite;
    }
    @keyframes text-glow {
        0%, 100% { text-shadow: 0 0 15px var(--lilac), 0 0 30px var(--orange); }
        50% { text-shadow: 0 0 30px var(--yellow), 0 0 60px var(--lilac); }
    }

    /* --- Sidebar --- */
    .st-emotion-cache-16txtl3 {
        background: rgba(18, 12, 24, 0.8); backdrop-filter: blur(15px);
        border-right: 1px solid rgba(200, 162, 200, 0.3);
    }

    /* --- Cards de Post --- */
    .post-card {
        display: flex; gap: 1.5rem; background: var(--card-bg);
        border: 1px solid rgba(200, 162, 200, 0.2); border-radius: 15px;
        margin-bottom: 2rem; padding: 1.5rem; transition: all 0.4s ease;
        position: relative; overflow: hidden; backdrop-filter: blur(10px);
        opacity: 0; transform: translateY(50px); animation: fade-in 0.5s forwards;
    }
    @keyframes fade-in {
        to { opacity: 1; transform: translateY(0); }
    }
    .post-card:hover {
        transform: scale(1.03); border-color: var(--lilac);
        box-shadow: 0 10px 40px rgba(200, 162, 200, 0.2);
    }
    .post-image-container {
        flex-shrink: 0; width: 250px; height: 180px; border-radius: 10px; overflow: hidden;
    }
    .post-image {
        width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;
    }
    .post-card:hover .post-image { transform: scale(1.1); }
    .post-content h3 { font-size: 1.8rem; color: var(--text-light); margin-bottom: 0.5rem; }
    .post-meta { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1rem; }
    .post-excerpt { color: var(--text-light); }
    .post-category {
        position: absolute; top: 1.5rem; right: 1.5rem; background: var(--orange);
        color: var(--dark-bg); padding: 0.3rem 0.8rem; border-radius: 20px;
        font-size: 0.8rem; font-weight: 700;
    }

</style>

<canvas id="bg-animation"></canvas>

<script>
    const canvas = document.getElementById('bg-animation');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particles = [];
    const colors = ['#ff8c00', '#ffd700', '#c8a2c8'];

    class Particle {
        constructor(x, y) {
            this.x = x; this.y = y;
            this.size = Math.random() * 3 + 1;
            this.speedX = Math.random() * 1 - 0.5;
            this.speedY = Math.random() * 1 - 0.5;
            this.color = colors[Math.floor(Math.random() * colors.length)];
        }
        update() {
            this.x += this.speedX; this.y += this.speedY;
            if (this.size > 0.1) this.size -= 0.02;
        }
        draw() {
            ctx.fillStyle = this.color; ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function handleParticles() {
        for (let i = 0; i < particles.length; i++) {
            particles[i].update(); particles[i].draw();
            if (particles[i].size <= 0.1) { particles.splice(i, 1); i--; }
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        handleParticles();
        requestAnimationFrame(animate);
    }

    window.addEventListener('mousemove', (e) => {
        for (let i = 0; i < 3; i++) {
            particles.push(new Particle(e.x, e.y));
        }
    });
    animate();
</script>
"""
st.markdown(css_js, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="main-header">
    <h1>Cosmic Flare</h1>
    <p style="color: var(--text-muted); font-size: 1.2rem;">Navegando pelas intersecções de tecnologia, arte e futuro.</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("Busca")
    st.text_input("Procurar no blog...", label_visibility="collapsed")
    st.header("Categorias")
    st.button("Futurismo", use_container_width=True)
    st.button("Design", use_container_width=True)
    st.button("IA", use_container_width=True)
    st.button("Marketing", use_container_width=True)

# --- GRID DE POSTS ---
posts_df = get_posts()

for i, row in posts_df.iterrows():
    st.markdown(f"""
    <div class="post-card" style="animation-delay: {i * 0.1}s">
        <div class="post-image-container">
            <img src="{row['image']}" class="post-image">
        </div>
        <div class="post-content">
            <div class="post-category">{row['category']}</div>
            <h3>{row['title']}</h3>
            <div class="post-meta">✍️ {row['author']} | 🕒 {row['read_time']} min de leitura</div>
            <p class="post-excerpt">{row['excerpt'][:150]}...</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<hr style='border-color: rgba(200, 162, 200, 0.2);'>", unsafe_allow_html=True)
st.markdown("© 2026 Cosmic Flare | Criado com paixão por Manus AI.")
