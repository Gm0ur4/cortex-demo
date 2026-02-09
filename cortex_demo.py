import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="YourApp - A New Way",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS MODERNO E SOFISTICADO - INSPIRADO EM HELPUP
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #ffffff;
        font-family: 'Inter', sans-serif;
        color: #1a1a1a;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: #ffffff;
    }
    
    /* HEADER/NAVBAR */
    .navbar {
        background: #ffffff;
        padding: 20px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #f0f0f0;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .navbar-logo {
        font-size: 28px;
        font-weight: 900;
        color: #FF1493;
        text-decoration: none;
    }
    
    .navbar-links {
        display: flex;
        gap: 40px;
        align-items: center;
    }
    
    .navbar-link {
        color: #1a1a1a;
        text-decoration: none;
        font-weight: 500;
        font-size: 16px;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .navbar-link:hover {
        color: #FF1493;
    }
    
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: #FF1493;
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-cta {
        background: #FF1493;
        color: white;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 2px solid #FF1493;
    }
    
    .navbar-cta:hover {
        background: white;
        color: #FF1493;
    }
    
    /* HERO SECTION */
    .hero-section {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
        color: white;
        padding: 120px 40px;
        text-align: left;
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 600px;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -5%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        flex: 1;
        max-width: 600px;
    }
    
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 20px;
        text-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    .hero-subtitle {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 40px;
        opacity: 0.95;
        font-weight: 400;
    }
    
    .hero-cta {
        display: inline-block;
        background: white;
        color: #FF1493;
        padding: 16px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 18px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    }
    
    .hero-mockup {
        position: relative;
        z-index: 2;
        flex: 1;
        text-align: center;
    }
    
    .phone-mockup {
        width: 300px;
        height: 600px;
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        border-radius: 40px;
        padding: 12px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        position: relative;
        margin: 0 auto;
    }
    
    .phone-mockup::before {
        content: '';
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 150px;
        height: 25px;
        background: #1a1a1a;
        border-radius: 0 0 20px 20px;
        z-index: 10;
    }
    
    .phone-screen {
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
        border-radius: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
        color: white;
        font-weight: 900;
    }
    
    /* SEÇÕES COM BORDAS TRACEJADAS */
    .feature-section {
        padding: 100px 40px;
        max-width: 1400px;
        margin: 0 auto;
        border: 3px dashed #FF1493;
        border-radius: 20px;
        margin: 60px auto;
        background: linear-gradient(135deg, rgba(255, 20, 147, 0.05) 0%, rgba(255, 105, 180, 0.05) 100%);
    }
    
    .feature-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 30px;
        color: #FF1493;
        line-height: 1.2;
    }
    
    .feature-description {
        font-size: 18px;
        color: #1a1a1a;
        line-height: 1.8;
        max-width: 700px;
        margin-bottom: 50px;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 40px;
        margin-top: 60px;
    }
    
    .feature-card {
        background: white;
        padding: 40px 30px;
        border-radius: 15px;
        border: 2px solid #f0f0f0;
        transition: all 0.4s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        border-color: #FF1493;
        box-shadow: 0 20px 50px rgba(255, 20, 147, 0.15);
    }
    
    .feature-card-icon {
        font-size: 48px;
        margin-bottom: 20px;
        display: inline-block;
    }
    
    .feature-card-title {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #1a1a1a;
    }
    
    .feature-card-desc {
        font-size: 16px;
        color: #666666;
        line-height: 1.6;
    }
    
    /* SEÇÃO DE BENEFÍCIOS */
    .benefits-section {
        background: #f8f8f8;
        padding: 100px 40px;
    }
    
    .benefits-container {
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .benefits-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 60px;
        color: #FF1493;
        text-align: center;
    }
    
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
    }
    
    .benefit-item {
        background: white;
        padding: 50px 40px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #e0e0e0;
        transition: all 0.4s ease;
    }
    
    .benefit-item:hover {
        transform: translateY(-15px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.1);
        border-color: #FF1493;
    }
    
    .benefit-number {
        font-size: 64px;
        font-weight: 900;
        color: #FF1493;
        margin-bottom: 20px;
    }
    
    .benefit-title {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 15px;
        color: #1a1a1a;
    }
    
    .benefit-desc {
        font-size: 16px;
        color: #666666;
        line-height: 1.6;
    }
    
    /* CTA SECTION */
    .cta-section {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
        color: white;
        padding: 100px 40px;
        text-align: center;
    }
    
    .cta-section-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 30px;
    }
    
    .cta-section-desc {
        font-size: 20px;
        margin-bottom: 50px;
        opacity: 0.95;
    }
    
    .cta-button {
        display: inline-block;
        background: white;
        color: #FF1493;
        padding: 18px 60px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 18px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* FOOTER */
    .footer {
        background: #1a1a1a;
        color: rgba(255, 255, 255, 0.8);
        padding: 60px 40px;
        text-align: center;
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-bottom: 30px;
        flex-wrap: wrap;
    }
    
    .footer-link {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .footer-link:hover {
        color: #FF1493;
    }
    
    .footer-contact {
        margin-bottom: 30px;
    }
    
    .footer-contact-item {
        margin-bottom: 10px;
        font-size: 16px;
    }
    
    .footer-copyright {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 30px;
        margin-top: 30px;
        font-size: 14px;
    }
    
    /* STREAMLIT OVERRIDES */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #FF1493, #FF69B4);
        color: white;
        border: none;
        padding: 16px 24px;
        border-radius: 15px;
        font-weight: 700;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(255, 20, 147, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(255, 20, 147, 0.5);
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 12px;
        font-size: 16px;
        background: white;
        color: #1a1a1a;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: #999999;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #FF1493;
        box-shadow: 0 0 0 3px rgba(255, 20, 147, 0.1);
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
            padding: 60px 20px;
            min-height: auto;
        }
        
        .hero-title {
            font-size: 42px;
        }
        
        .hero-mockup {
            margin-top: 40px;
        }
        
        .phone-mockup {
            width: 250px;
            height: 500px;
        }
        
        .feature-section {
            padding: 60px 20px;
            margin: 40px 20px;
        }
        
        .feature-title {
            font-size: 36px;
        }
        
        .benefits-section {
            padding: 60px 20px;
        }
        
        .benefits-title {
            font-size: 36px;
        }
        
        .cta-section {
            padding: 60px 20px;
        }
        
        .cta-section-title {
            font-size: 36px;
        }
        
        .footer-links {
            gap: 15px;
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
navbar_html = """
<div class="navbar">
    <a href="#" class="navbar-logo">YourApp</a>
    <div class="navbar-links">
        <a href="#" class="navbar-link">Features</a>
        <a href="#" class="navbar-link">About</a>
        <a href="#" class="navbar-link">Blog</a>
        <a href="#" class="navbar-link">Contact</a>
        <a href="#" class="navbar-cta">Get Started</a>
    </div>
</div>
"""
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = """
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">A new way to connect</div>
        <div class="hero-subtitle">
            Say hello to a brand new way of doing things. Connect with people who share your passion and make a real impact together.
        </div>
        <button class="hero-cta">Download Now</button>
    </div>
    <div class="hero-mockup">
        <div class="phone-mockup">
            <div class="phone-screen">📱</div>
        </div>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
features_html = """
<div class="feature-section">
    <div class="feature-title">Discover what makes us different</div>
    <div class="feature-description">
        We've built something special. A platform designed with you in mind, combining simplicity with powerful features.
    </div>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-card-icon">🎯</div>
            <div class="feature-card-title">Easy to Use</div>
            <div class="feature-card-desc">Intuitive interface designed for everyone. No complicated steps, just pure simplicity.</div>
        </div>
        <div class="feature-card">
            <div class="feature-card-icon">⚡</div>
            <div class="feature-card-title">Lightning Fast</div>
            <div class="feature-card-desc">Experience blazing-fast performance. Everything loads instantly, no waiting around.</div>
        </div>
        <div class="feature-card">
            <div class="feature-card-icon">🔒</div>
            <div class="feature-card-title">Secure</div>
            <div class="feature-card-desc">Your data is protected with enterprise-grade security. We take privacy seriously.</div>
        </div>
        <div class="feature-card">
            <div class="feature-card-icon">🌍</div>
            <div class="feature-card-title">Global Community</div>
            <div class="feature-card-desc">Join thousands of users worldwide. Connect, collaborate, and grow together.</div>
        </div>
    </div>
</div>
"""
st.markdown(features_html, unsafe_allow_html=True)

# ==================== BENEFITS SECTION ====================
benefits_html = """
<div class="benefits-section">
    <div class="benefits-container">
        <div class="benefits-title">Why choose us?</div>
        <div class="benefits-grid">
            <div class="benefit-item">
                <div class="benefit-number">1M+</div>
                <div class="benefit-title">Active Users</div>
                <div class="benefit-desc">Join our thriving community of over 1 million satisfied users worldwide.</div>
            </div>
            <div class="benefit-item">
                <div class="benefit-number">24/7</div>
                <div class="benefit-title">Support</div>
                <div class="benefit-desc">Our dedicated support team is always here to help you succeed.</div>
            </div>
            <div class="benefit-item">
                <div class="benefit-number">99.9%</div>
                <div class="benefit-title">Uptime</div>
                <div class="benefit-desc">Reliable service you can count on, guaranteed uptime and performance.</div>
            </div>
        </div>
    </div>
</div>
"""
st.markdown(benefits_html, unsafe_allow_html=True)

# ==================== CONTACT SECTION ====================
st.markdown("""
<div style="padding: 100px 40px; max-width: 1400px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 60px;">
        <h2 style="font-size: 56px; font-weight: 900; color: #FF1493; margin-bottom: 20px;">Get in Touch</h2>
        <p style="font-size: 18px; color: #666666;">Have questions? We'd love to hear from you.</p>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name", placeholder="John Doe")
with col2:
    email = st.text_input("Your Email", placeholder="john@example.com")

message = st.text_area("Message", placeholder="Tell us what's on your mind...", height=150)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Send Message", use_container_width=True):
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been sent successfully.")
        else:
            st.error("Please fill in all fields!")

# ==================== CTA SECTION ====================
cta_html = """
<div class="cta-section">
    <div class="cta-section-title">Ready to get started?</div>
    <div class="cta-section-desc">Join thousands of satisfied users today</div>
    <button class="cta-button">Download the App</button>
</div>
"""
st.markdown(cta_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
footer_html = '<div class="footer"><div class="footer-links"><a href="#" class="footer-link">Privacy Policy</a><a href="#" class="footer-link">Terms of Service</a><a href="#" class="footer-link">Contact</a><a href="#" class="footer-link">Blog</a></div><div class="footer-contact"><div class="footer-contact-item">📧 contact@yourapp.com</div><div class="footer-contact-item">📱 +1 (555) 123-4567</div></div><div class="footer-copyright">© 2025 YourApp. All rights reserved. Made with ❤️</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
