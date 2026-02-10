import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Megavale Card - Soluções em Benefícios",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZADO (Para ficar parecido com um site real) ---
st.markdown("""
<style>
    /* Remover margens padrão do Streamlit para parecer um site full-width */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    /* Estilo do Header Simulado */
    .header-style {
        font-size: 20px;
        font-weight: bold;
        color: #003366;
        text-align: center;
        padding: 10px;
    }
    
    /* Botões personalizados */
    div.stButton > button {
        width: 100%;
        background-color: #004488;
        color: white;
        border-radius: 5px;
        border: none;
        height: 50px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #0066cc;
        color: white;
    }

    /* Cards de Serviços */
    .service-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #004488;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    
    /* Rodapé */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #003366;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO AUXILIAR PARA CARREGAR IMAGENS DA WEB ---
# Como não tenho os arquivos locais, uso imagens de placeholder da web
def load_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None

# --- HEADER / MENU ---
# Simulação de barra de navegação
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col1:
    # Logo simulado
    st.markdown("## **MEGAVALE**") 
    st.caption("Soluções em cartões")

with col2:
    st.button("🏠 Início")
with col3:
    st.button("🏢 Para Empresas")
with col4:
    st.button("👤 Para Usuários")
with col5:
    st.button("🔒 Portal Cliente")

st.markdown("---")

# --- SEÇÃO HERO (BANNER PRINCIPAL) ---
# Usando uma imagem genérica de "negócios/cartão" do Unsplash
banner_url = "https://images.unsplash.com/photo-1556742049-0cfed4f7a07d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80"
st.image(banner_url, use_container_width=True)

st.markdown("""
<div style="text-align: center; padding: 40px;">
    <h1 style="color: #003366;">A melhor solução em benefícios para sua empresa</h1>
    <p style="font-size: 18px; color: #666;">Gestão completa, facilidade para o RH e liberdade para o colaborador.</p>
</div>
""", unsafe_allow_html=True)

# --- ÁREA DE AÇÃO RÁPIDA (Grid) ---
c1, c2, c3 = st.columns(3)

with c1:
    st.info("🏢 **SOU EMPRESA**")
    st.markdown("Contrate agora os melhores benefícios para seus colaboradores com isenção fiscal.")
    if st.button("Solicitar Proposta", key="btn_empresa"):
        st.success("Formulário de proposta aberto!")

with c2:
    st.warning("💳 **CONSULTAR SALDO**")
    st.markdown("Acesse seu saldo, extrato e rede credenciada de forma rápida e segura.")
    cpf = st.text_input("Digite seu CPF", placeholder="000.000.000-00")
    if st.button("Consultar", key="btn_saldo"):
        if cpf:
            st.info(f"Buscando saldo para o CPF: {cpf}...")
        else:
            st.error("Por favor, digite um CPF.")

with c3:
    st.success("🏪 **REDE CREDENCIADA**")
    st.markdown("Aceite Megavale no seu estabelecimento e aumente suas vendas.")
    if st.button("Quero me Credenciar", key="btn_rede"):
        st.balloons()

st.markdown("---")

# --- SEÇÃO DE PRODUTOS ---
st.markdown("<h2 style='text-align: center; color: #004488;'>Nossos Cartões</h2>", unsafe_allow_html=True)
st.write("") # Espaçamento

col_prod1, col_prod2, col_prod3, col_prod4 = st.columns(4)

def card_template(titulo, icone, desc):
    st.markdown(f"""
    <div class="service-card">
        <h3>{icone} {titulo}</h3>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

with col_prod1:
    card_template("Alimentação", "🛒", "Para compras em supermercados, açougues e mercearias.")
    st.image("https://images.unsplash.com/photo-1580913428706-c311ab527eb6?auto=format&fit=crop&w=300&q=80", caption="Vale Alimentação")

with col_prod2:
    card_template("Refeição", "🍽️", "Aceito em restaurantes, lanchonetes e padarias.")
    st.image("https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=300&q=80", caption="Vale Refeição")

with col_prod3:
    card_template("Combustível", "⛽", "Gestão de frota e facilidade no abastecimento.")
    st.image("https://images.unsplash.com/photo-1632823471565-1ec2a1ad4015?auto=format&fit=crop&w=300&q=80", caption="Vale Combustível")

with col_prod4:
    card_template("Flex", "🎁", "Multibenefícios em um único cartão para seu time.")
    st.image("https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&w=300&q=80", caption="Megavale Flex")

st.write("---")

# --- CONTATO / APP ---
c_app, c_contato = st.columns([1, 1])

with c_app:
    st.subheader("📱 Baixe nosso App")
    st.write("Tenha o controle total na palma da sua mão. Disponível para Android e iOS.")
    st.markdown("👉 **[Google Play Store](#)**")
    st.markdown("👉 **[Apple App Store](#)**")

with c_contato:
    st.subheader("📞 Fale Conosco")
    st.text_input("Nome")
    st.text_input("Email")
    st.text_area("Mensagem")
    st.button("Enviar Mensagem")

# --- FOOTER ---
st.markdown("""
<br><br><br>
<div class='footer'>
    <p>© 2024 Megavale Card. Todos os direitos reservados. | Desenvolvido com Streamlit</p>
</div>
""", unsafe_allow_html=True)
