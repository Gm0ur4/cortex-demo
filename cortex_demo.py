# -*- coding: utf-8 -*-
"""
Landing Page ÉPICA de Geração de Leads - "Quantum Leap"

Autor: Manus AI
Data: 10 de Fevereiro de 2026

Versão ultra-premium com animações avançadas, cores dinâmicas que mudam com o scroll,
efeitos visuais de nível profissional e uma experiência de usuário totalmente imersiva.
"""

import streamlit as st

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(
    page_title="Quantum Leap | O Futuro é Agora",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS, JAVASCRIPT E ANIMAÇÕES AVANÇADAS ---
epic_code = """
<style>
    /* --- FONTES E VARIÁVEIS GLOBAIS --- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap');
    :root {
        --c1: #6a0dad; /* Roxo */
        --c2: #ff00ff; /* Magenta */
        --c3: #00ffff; /* Ciano */
        --c4: #ff8c00; /* Laranja */
        --dark: #0A001A;
        --light: #F0E6FF;
        --font: 'Poppins', sans-serif;
    }

    /* --- RESET E BODY --- */
    body { font-family: var(--font); background: var(--dark); color: var(--light); overflow-x: hidden; }
    .main { background: transparent !important; }
    .section { max-width: 1100px; margin: auto; padding: 6rem 2rem; text-align: center; position: relative; z-index: 2; }
    .hidden { opacity: 0; transform: translateY(50px); transition: all 1s ease-out; }
    .visible { opacity: 1; transform: translateY(0); }

    /* --- FUNDO DINÂMICO E PARTÍCULAS --- */
    #dynamic-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; transition: background 1s ease; }
    #particles-js { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }

    /* --- HEADER --- */
    .header { position: fixed; top: 0; left: 0; right: 0; z-index: 10; backdrop-filter: blur(12px); background: rgba(10,0,26,0.7); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-weight: 900; font-size: 1.8rem; background: linear-gradient(90deg, var(--c2), var(--c3)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

    /* --- BOTÕES --- */
    .cta-button { background: linear-gradient(90deg, var(--c1), var(--c2)); color: white; padding: 14px 32px; border-radius: 50px; text-decoration: none; font-weight: 600; transition: all 0.3s ease; border: none; box-shadow: 0 5px 20px rgba(255,0,255,0.4); }
    .cta-button:hover { transform: scale(1.05) translateY(-3px); box-shadow: 0 10px 30px rgba(0,255,255,0.5); }

    /* --- HERO --- */
    .hero h1 { font-size: 4.5rem; font-weight: 900; line-height: 1.1; background: linear-gradient(90deg, var(--c3), var(--c2), var(--c4)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: text-flow 5s ease-in-out infinite; background-size: 200% 200%; }
    @keyframes text-flow { 0%, 100% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } }

    /* --- BENEFÍCIOS (CARDS 3D) --- */
    .benefits-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; perspective: 1000px; }
    .benefit-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 2rem; transition: transform 0.5s, box-shadow 0.5s; transform-style: preserve-3d; }
    .benefit-card:hover { box-shadow: 0 20px 50px rgba(0,0,0,0.5); }

    /* --- COMO FUNCIONA (TIMELINE) --- */
    .timeline { position: relative; padding: 2rem 0; }
    .timeline::before { content: ''; position: absolute; left: 50%; top: 0; bottom: 0; width: 3px; background: linear-gradient(to bottom, var(--c1), var(--c3)); border-radius: 3px; }
    .timeline-item { position: relative; width: 50%; padding: 1rem 2rem; box-sizing: border-box; }
    .timeline-item:nth-child(odd) { left: 0; text-align: right; }
    .timeline-item:nth-child(even) { left: 50%; text-align: left; }
    .timeline-item::after { content: ''; position: absolute; top: 1.5rem; width: 20px; height: 20px; background: var(--dark); border: 4px solid var(--c2); border-radius: 50%; z-index: 1; }
    .timeline-item:nth-child(odd)::after { right: -10px; }
    .timeline-item:nth-child(even)::after { left: -10px; }

</style>

<div id="dynamic-bg"></div>
<div id="particles-js"></div>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
    // --- ANIMAÇÃO DE SCROLL --- 
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                // entry.target.classList.remove('visible'); // Opcional: re-animar ao rolar para cima
            }
        });
    }, { threshold: 0.1 });
    document.addEventListener("DOMContentLoaded", () => {
        const sections = document.querySelectorAll('.section');
        sections.forEach(section => observer.observe(section));
    });

    // --- FUNDO DINÂMICO --- 
    const bg = document.getElementById('dynamic-bg');
    const colors = ['#6a0dad', '#ff00ff', '#00ffff', '#ff8c00'];
    window.addEventListener('scroll', () => {
        const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
        const colorIndex = Math.min(Math.floor(scrollPercent * colors.length), colors.length - 1);
        const nextColorIndex = (colorIndex + 1) % colors.length;
        const blend = (scrollPercent * colors.length) % 1;
        // Esta é uma forma simplificada de misturar cores. Uma biblioteca seria melhor.
        bg.style.background = `linear-gradient(135deg, ${colors[colorIndex]}, ${colors[nextColorIndex]})`;
    });

    // --- PARTÍCULAS --- 
    particlesJS('particles-js', {
        "particles": { "number": { "value": 50 }, "color": { "value": "#ffffff" }, "shape": { "type": "triangle" }, "opacity": { "value": 0.3, "anim": { "enable": true, "speed": 1 } }, "size": { "value": 4, "random": true }, "line_linked": { "enable": true, "distance": 150, "color": "#ffffff", "opacity": 0.2 }, "move": { "enable": true, "speed": 2, "direction": "none", "out_mode": "out" } },
        "interactivity": { "events": { "onhover": { "enable": true, "mode": "repulse" } } }
    });

    // --- CARDS 3D --- 
    const cards = document.querySelectorAll('.benefit-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; 
            const y = e.clientY - rect.top;
            const { width, height } = rect;
            const rotateX = (y / height - 0.5) * -30; // Rotação no eixo X
            const rotateY = (x / width - 0.5) * 30;  // Rotação no eixo Y
            card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'rotateX(0) rotateY(0) scale(1)';
        });
    });

</script>
"""
st.markdown(epic_code, unsafe_allow_html=True)

# --- ESTRUTURA DA PÁGINA ---

# 1. HEADER
st.markdown('<div class="header"><div class="logo">Quantum Leap</div><a href="#cta-final" class="cta-button">Pedir Acesso Antecipado</a></div>', unsafe_allow_html=True)

# 2. HERO
st.markdown('<div class="section hero"><h1>O Salto Quântico para sua Produtividade</h1><p style="font-size: 1.3rem; max-width: 700px; margin: 1rem auto 2rem auto;">Nossa IA generativa não apenas automatiza, ela reinventa seus fluxos de trabalho, prevê suas necessidades e transforma dados brutos em decisões geniais.</p><a href="#cta-final" class="cta-button" style="padding: 20px 45px; font-size: 1.3rem;">Ver o Futuro em Ação</a></div>', unsafe_allow_html=True)

# 3. PROBLEMA
st.markdown('<div class="section hidden"><h2>Sua equipe está presa no passado?</h2><p>Ferramentas legadas, processos manuais e dados desconexos são âncoras que impedem sua empresa de alcançar a velocidade da luz. O custo da ineficiência é maior do que você imagina.</p></div>', unsafe_allow_html=True)

# 4. SOLUÇÃO
st.markdown('<div class="section hidden"><h2>Quantum Leap é a Singularidade da Eficiência.</h2><p>Nós conectamos todas as suas fontes de dados, aprendemos com cada interação e entregamos uma interface unificada que não só responde, mas antecipa. É menos trabalho, mais genialidade.</p></div>', unsafe_allow_html=True)

# 5. BENEFÍCIOS
st.markdown('<div class="section hidden"><h2>Benefícios de Outra Dimensão</h2><div class="benefits-grid"><div class="benefit-card"><h3>Inteligência Preditiva</h3><p>Nossa IA analisa tendências e prevê resultados, dando a você o poder de tomar decisões antes mesmo que o problema surja.</p></div><div class="benefit-card"><h3>Automação Hiper-Personalizada</h3><p>Criamos automações que se adaptam ao seu jeito de trabalhar, aprendendo e melhorando a cada dia.</p></div><div class="benefit-card"><h3>Insights Instantâneos</h3><p>Transforme montanhas de dados em gráficos e relatórios acionáveis com um simples comando de voz.</p></div></div></div>', unsafe_allow_html=True)

# 6. DIFERENCIAIS
st.markdown('<div class="section hidden"><h2>Não somos apenas uma ferramenta. Somos um novo paradigma.</h2><p>Enquanto outros oferecem automação, nós oferecemos cognição. Quantum Leap não segue regras, ela entende o contexto. É a diferença entre um robô de fábrica e um co-piloto genial.</p></div>', unsafe_allow_html=True)

# 7. COMO FUNCIONA
st.markdown('<div class="section hidden"><h2>A Jornada para o Futuro</h2><div class="timeline"><div class="timeline-item hidden"><h3>Passo 1: Conexão Neural</h3><p>Integramos com todo o seu ecossistema digital em minutos, criando uma rede neural de dados unificada.</p></div><div class="timeline-item hidden"><h3>Passo 2: Período de Aprendizagem</h3><p>Nossa IA observa silenciosamente, aprendendo os padrões e nuances do seu negócio por 7 dias.</p></div><div class="timeline-item hidden"><h3>Passo 3: Ativação Quântica</h3><p>A IA assume o controle das tarefas repetitivas, começando a otimizar e sugerir melhorias proativamente.</p></div></div></div>', unsafe_allow_html=True)

# 8. PROVA SOCIAL
st.markdown('<div class="section hidden"><h2>+1.000 Empresas Já Deram o Salto</h2><p style="font-size: 1.5rem; font-weight: 600; margin: 2rem 0;">"Quantum Leap não é uma melhoria, é uma metamorfose. Nossa capacidade de inovar aumentou em 300%."</p><p>- CTO, InovaTech Solutions</p></div>', unsafe_allow_html=True)

# 9. GARANTIA
st.markdown('<div class="section hidden"><h2>Garantia de Singularidade</h2><p>Se após 30 dias você não sentir que sua produtividade entrou em uma nova dimensão, oferecemos reembolso total e um relatório completo de otimização como nosso presente.</p></div>', unsafe_allow_html=True)

# 10. CTA FINAL
st.markdown('<div id="cta-final" class="section hidden"><h2>Está pronto para o Salto Quântico?</h2><p>Peça seu acesso antecipado e seja um dos primeiros a experimentar o futuro da produtividade.</p><div style="max-width: 600px; margin: 2rem auto;"></div></div>', unsafe_allow_html=True)
col1, col2 = st.columns([3,2])
with col1:
    st.text_input("Seu e-mail profissional", label_visibility="collapsed", placeholder="Seu e-mail profissional")
with col2:
    st.button("Quero Acesso ao Futuro", use_container_width=True, type="primary")

# 11. FAQ
st.markdown('<div class="section hidden"><h2>Perguntas do Multiverso</h2></div>', unsafe_allow_html=True)
with st.expander("Isso vai substituir minha equipe?"):
    st.write("Não. Vai super-potencializar sua equipe. Quantum Leap elimina o trabalho tedioso para que os humanos possam focar no que fazem de melhor: criar, inovar e resolver problemas complexos.")
with st.expander("A segurança é de nível militar?"):
    st.write("Nível quântico. Usamos criptografia pós-quântica e servidores isolados para garantir que seus dados sejam impenetráveis.")

# 12. FOOTER
st.markdown('<div class="section footer hidden"><p>© 2026 Quantum Leap Inc. Todos os universos reservados.</p></div>', unsafe_allow_html=True)
