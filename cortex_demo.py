import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Portfolio Pessoal - Profissional de Excelência",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS PORTFOLIO PESSOAL - ALTO NÍVEL
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #0f1419 100%);
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        line-height: 1.8;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ANIMAÇÕES SOFISTICADAS */
    @keyframes heroReveal {
        0% { transform: translateY(100px) rotateX(20deg); opacity: 0; }
        100% { transform: translateY(0) rotateX(0deg); opacity: 1; }
    }
    
    @keyframes textTypewriter {
        0% { width: 0; }
        100% { width: 100%; }
    }
    
    @keyframes cursorBlink {
        0%, 49% { border-right-color: #00d4ff; }
        50%, 100% { border-right-color: transparent; }
    }
    
    @keyframes floatParallax {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-30px); }
    }
    
    @keyframes cardHoverGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.5); }
    }
    
    @keyframes skillBarFill {
        0% { width: 0; }
        100% { width: 100%; }
    }
    
    @keyframes rotateGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes slideInStagger {
        0% { transform: translateX(-50px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes pulseRing {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(1.5); opacity: 0; }
    }
    
    /* NAVBAR SOFISTICADA */
    .navbar {
        background: linear-gradient(90deg, rgba(15, 20, 25, 0.98) 0%, rgba(26, 31, 46, 0.98) 100%);
        backdrop-filter: blur(20px);
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 212, 255, 0.2);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
    }
    
    .navbar-logo {
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px;
        font-family: 'Syne', sans-serif;
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: #a0aec0;
        text-decoration: none;
        font-weight: 500;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
    }
    
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #00d4ff, #0099cc);
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #00d4ff;
    }
    
    .navbar-cta {
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        color: #0f1419;
        padding: 12px 32px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.6);
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #0f1419 100%);
        min-height: 900px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
        padding: 80px 80px;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
        animation: floatParallax 6s ease-in-out infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(0, 153, 204, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -150px;
        left: -150px;
        animation: floatParallax 8s ease-in-out infinite reverse;
    }
    
    .hero-content {
        z-index: 2;
        position: relative;
        max-width: 600px;
        animation: heroReveal 1s ease-out;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 800;
        margin-bottom: 20px;
        color: #ffffff;
        letter-spacing: -2px;
        line-height: 1.1;
        font-family: 'Syne', sans-serif;
    }
    
    .hero-subtitle {
        font-size: 20px;
        font-weight: 400;
        margin-bottom: 15px;
        color: #00d4ff;
        letter-spacing: 1px;
    }
    
    .hero-description {
        font-size: 16px;
        color: #a0aec0;
        margin-bottom: 50px;
        line-height: 1.8;
        max-width: 500px;
    }
    
    .hero-cta-group {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }
    
    .hero-cta-primary {
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        color: #0f1419;
        padding: 16px 48px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.4);
    }
    
    .hero-cta-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 50px rgba(0, 212, 255, 0.7);
    }
    
    .hero-cta-secondary {
        background: transparent;
        color: #00d4ff;
        padding: 16px 48px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid #00d4ff;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
    
    .hero-cta-secondary:hover {
        background: rgba(0, 212, 255, 0.1);
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.4);
    }
    
    .hero-image {
        z-index: 2;
        position: relative;
        width: 400px;
        height: 500px;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 153, 204, 0.05));
        border: 2px solid rgba(0, 212, 255, 0.3);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: cardHoverGlow 3s ease-in-out infinite;
        overflow: hidden;
    }
    
    .hero-image::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(0, 212, 255, 0.1) 50%, transparent 70%);
        animation: slideInStagger 3s ease-in-out infinite;
    }
    
    .hero-image-content {
        font-size: 120px;
        position: relative;
        z-index: 1;
    }
    
    /* SKILLS SECTION */
    .skills-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1f2e 0%, #0f1419 100%);
        position: relative;
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 100px;
        text-align: center;
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        font-family: 'Syne', sans-serif;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .skill-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(0, 153, 204, 0.02));
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 50px 40px;
        border-radius: 8px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInStagger 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
    }
    
    .skill-card:nth-child(1) { animation-delay: 0.1s; }
    .skill-card:nth-child(2) { animation-delay: 0.2s; }
    .skill-card:nth-child(3) { animation-delay: 0.3s; }
    
    .skill-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .skill-card:hover::before {
        left: 100%;
    }
    
    .skill-card:hover {
        transform: translateY(-15px);
        border-color: #00d4ff;
        box-shadow: 0 0 50px rgba(0, 212, 255, 0.3);
    }
    
    .skill-icon {
        font-size: 48px;
        margin-bottom: 20px;
    }
    
    .skill-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #00d4ff;
        letter-spacing: 0.5px;
        font-family: 'Syne', sans-serif;
    }
    
    .skill-desc {
        font-size: 15px;
        color: #a0aec0;
        line-height: 1.8;
        font-weight: 400;
    }
    
    /* EXPERIENCE TIMELINE */
    .experience-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
    }
    
    .experience-title {
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 100px;
        text-align: center;
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        font-family: 'Syne', sans-serif;
    }
    
    .experience-timeline {
        max-width: 900px;
        margin: 0 auto;
        position: relative;
    }
    
    .experience-timeline::before {
        content: '';
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 2px;
        height: 100%;
        background: linear-gradient(180deg, #00d4ff, transparent);
    }
    
    .experience-item {
        margin-bottom: 60px;
        position: relative;
        animation: slideInStagger 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .experience-item:nth-child(odd) {
        text-align: right;
        padding-right: 52%;
    }
    
    .experience-item:nth-child(even) {
        text-align: left;
        padding-left: 52%;
        animation: slideInStagger 0.8s ease-out;
    }
    
    .experience-item:nth-child(1) { animation-delay: 0.1s; }
    .experience-item:nth-child(2) { animation-delay: 0.2s; }
    .experience-item:nth-child(3) { animation-delay: 0.3s; }
    
    .experience-dot {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 16px;
        height: 16px;
        background: #00d4ff;
        border: 4px solid #0f1419;
        border-radius: 50%;
        top: 0;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
        animation: pulseRing 2s ease-out infinite;
    }
    
    .experience-content {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(0, 153, 204, 0.02));
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
    }
    
    .experience-year {
        font-size: 16px;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 10px;
        font-family: 'Syne', sans-serif;
    }
    
    .experience-role {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
    }
    
    .experience-company {
        font-size: 14px;
        color: #a0aec0;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .experience-desc {
        font-size: 14px;
        color: #a0aec0;
        line-height: 1.6;
    }
    
    /* PROJECTS GRID */
    .projects-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #1a1f2e 0%, #0f1419 100%);
    }
    
    .projects-title {
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 100px;
        text-align: center;
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        font-family: 'Syne', sans-serif;
    }
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .project-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(0, 153, 204, 0.02));
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 8px;
        overflow: hidden;
        transition: all 0.4s ease;
        position: relative;
        animation: slideInStagger 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
    }
    
    .project-card:nth-child(1) { animation-delay: 0.1s; }
    .project-card:nth-child(2) { animation-delay: 0.2s; }
    .project-card:nth-child(3) { animation-delay: 0.3s; }
    
    .project-card:hover {
        transform: translateY(-15px);
        border-color: #00d4ff;
        box-shadow: 0 0 50px rgba(0, 212, 255, 0.3);
    }
    
    .project-image {
        width: 100%;
        height: 200px;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 153, 204, 0.05));
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        position: relative;
        overflow: hidden;
    }
    
    .project-image::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.2), transparent);
        animation: slideInStagger 2s ease-in-out infinite;
    }
    
    .project-content {
        padding: 30px;
    }
    
    .project-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
        font-family: 'Syne', sans-serif;
    }
    
    .project-desc {
        font-size: 14px;
        color: #a0aec0;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    .project-tags {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }
    
    .project-tag {
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 12px;
        border: 1px solid rgba(0, 212, 255, 0.2);
    }
    
    /* CTA FINAL */
    .cta-final-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-final-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(15, 20, 25, 0.15);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    .cta-final-title {
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 20px;
        color: #0f1419;
        letter-spacing: -1px;
        font-family: 'Syne', sans-serif;
    }
    
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        color: rgba(15, 20, 25, 0.9);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 400;
    }
    
    .cta-final-button {
        background: #0f1419;
        color: #00d4ff;
        padding: 18px 60px;
        border: 2px solid #0f1419;
        border-radius: 4px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
    }
    
    /* FOOTER */
    .footer {
        background: #0f1419;
        color: #a0aec0;
        padding: 80px;
        text-align: center;
        border-top: 1px solid rgba(0, 212, 255, 0.2);
        box-shadow: 0 -8px 32px rgba(0, 212, 255, 0.1);
    }
    
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 400;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(0, 212, 255, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* RESPONSIVIDADE */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            gap: 20px;
            padding: 15px 20px;
        }
        
        .navbar-links {
            flex-direction: column;
            gap: 15px;
            width: 100%;
        }
        
        .hero-section {
            flex-direction: column;
            min-height: 600px;
            padding: 40px 20px;
        }
        
        .hero-image {
            width: 300px;
            height: 400px;
            margin-top: 40px;
        }
        
        .hero-title {
            font-size: 42px;
        }
        
        .skills-section,
        .experience-section,
        .projects-section,
        .cta-final-section {
            padding: 80px 20px;
        }
        
        .section-title,
        .experience-title,
        .projects-title,
        .cta-final-title {
            font-size: 36px;
        }
        
        .experience-timeline::before {
            left: 10px;
        }
        
        .experience-item:nth-child(odd),
        .experience-item:nth-child(even) {
            text-align: left;
            padding-left: 50px;
            padding-right: 0;
        }
        
        .experience-dot {
            left: 0;
            transform: translateX(-50%);
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
navbar_html = '<div class="navbar"><div class="navbar-logo">PORTFOLIO</div><div class="navbar-links"><a href="#" class="navbar-link">Sobre</a><a href="#" class="navbar-link">Skills</a><a href="#" class="navbar-link">Experiência</a><a href="#" class="navbar-link">Projetos</a><a href="#" class="navbar-cta">Contato</a></div></div>'
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = '''<div class="hero-section">
    <div class="hero-content">
        <div class="hero-subtitle">Bem-vindo ao meu portfólio</div>
        <div class="hero-title">Profissional de Excelência</div>
        <div class="hero-description">Especialista em criar soluções inovadoras com design sofisticado e tecnologia de ponta. Transformando ideias em realidade.</div>
        <div class="hero-cta-group">
            <button class="hero-cta-primary">Explorar Trabalhos</button>
            <button class="hero-cta-secondary">Saiba Mais</button>
        </div>
    </div>
    <div class="hero-image">
        <div class="hero-image-content">💼</div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== SKILLS SECTION ====================
skills_html = '''<div class="skills-section">
    <div class="section-title">Competências</div>
    <div class="skills-grid">
        <div class="skill-card">
            <div class="skill-icon">🎨</div>
            <div class="skill-title">Design</div>
            <div class="skill-desc">Criação de interfaces modernas e intuitivas com foco em experiência do usuário.</div>
        </div>
        <div class="skill-card">
            <div class="skill-icon">💻</div>
            <div class="skill-title">Desenvolvimento</div>
            <div class="skill-desc">Programação full-stack com tecnologias modernas e boas práticas.</div>
        </div>
        <div class="skill-card">
            <div class="skill-icon">🚀</div>
            <div class="skill-title">Inovação</div>
            <div class="skill-desc">Implementação de soluções criativas e escaláveis para desafios complexos.</div>
        </div>
    </div>
</div>'''
st.markdown(skills_html, unsafe_allow_html=True)

# ==================== EXPERIENCE SECTION ====================
experience_html = '''<div class="experience-section">
    <div class="experience-title">Experiência</div>
    <div class="experience-timeline">
        <div class="experience-item">
            <div class="experience-dot"></div>
            <div class="experience-content">
                <div class="experience-year">2022 - Presente</div>
                <div class="experience-role">Diretor de Inovação</div>
                <div class="experience-company">Tech Solutions</div>
                <div class="experience-desc">Liderança de projetos estratégicos e implementação de tecnologias emergentes.</div>
            </div>
        </div>
        <div class="experience-item">
            <div class="experience-dot"></div>
            <div class="experience-content">
                <div class="experience-year">2020 - 2022</div>
                <div class="experience-role">Gerente de Projetos</div>
                <div class="experience-company">Digital Agency</div>
                <div class="experience-desc">Gestão de equipes multidisciplinares e entrega de projetos de grande escala.</div>
            </div>
        </div>
        <div class="experience-item">
            <div class="experience-dot"></div>
            <div class="experience-content">
                <div class="experience-year">2018 - 2020</div>
                <div class="experience-role">Especialista em UX/UI</div>
                <div class="experience-company">Design Studio</div>
                <div class="experience-desc">Criação de experiências digitais inovadoras e interfaces de alto impacto.</div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(experience_html, unsafe_allow_html=True)

# ==================== PROJECTS SECTION ====================
projects_html = '''<div class="projects-section">
    <div class="projects-title">Projetos Destaque</div>
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-image">🌐</div>
            <div class="project-content">
                <div class="project-title">Plataforma Digital</div>
                <div class="project-desc">Sistema completo de gestão com interface intuitiva e performance otimizada.</div>
                <div class="project-tags">
                    <span class="project-tag">Design</span>
                    <span class="project-tag">Frontend</span>
                    <span class="project-tag">Backend</span>
                </div>
            </div>
        </div>
        <div class="project-card">
            <div class="project-image">📱</div>
            <div class="project-content">
                <div class="project-title">App Mobile</div>
                <div class="project-desc">Aplicação nativa com experiência fluida e sincronização em tempo real.</div>
                <div class="project-tags">
                    <span class="project-tag">Mobile</span>
                    <span class="project-tag">iOS</span>
                    <span class="project-tag">Android</span>
                </div>
            </div>
        </div>
        <div class="project-card">
            <div class="project-image">🎯</div>
            <div class="project-content">
                <div class="project-title">Campanha Marketing</div>
                <div class="project-desc">Estratégia digital integrada com resultados mensuráveis e ROI elevado.</div>
                <div class="project-tags">
                    <span class="project-tag">Marketing</span>
                    <span class="project-tag">Analytics</span>
                    <span class="project-tag">Growth</span>
                </div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(projects_html, unsafe_allow_html=True)

# ==================== CTA FINAL ====================
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-content">
        <div class="cta-final-title">Vamos Trabalhar Juntos?</div>
        <div class="cta-final-desc">Tenho a expertise para transformar sua visão em uma solução de alto impacto.</div>
        <button class="cta-final-button">Iniciar Projeto</button>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-text">Email: contato@portfolio.com | Telefone: +55 (11) 98765-4321</div><div class="footer-text">LinkedIn: linkedin.com/in/seu-perfil | GitHub: github.com/seu-usuario</div><div class="footer-copyright">© 2025 Portfolio Pessoal. Todos os direitos reservados.</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
