import streamlit as st

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Sistema de Login", page_icon="🔑", layout="centered")

with st.sidebar:
    st.title("🌍 TravelTun")

    st.page_link("1_sobre.py", label="🏠 Sobre")
    st.page_link("pages/2_cadastro.py", label="📝 Cadastro")
    st.page_link("pages/3_viagem.py", label="✈️ Viagem")
    st.page_link("pages/4_listagem.py", label="📋 Listagem")
    st.page_link("pages/5_avaliacao.py", label="⭐ Avaliação")

if "usuarios" not in st.session_state:
    st.session_state.usuarios = {"admin": {"senha": "12345678", "nome": "Administrador"}}
if "logado" not in st.session_state:
    st.session_state.logado = False
if "usuario_atual" not in st.session_state:
    st.session_state.usuario_atual = None
if "menu" not in st.session_state:  
    st.session_state.menu = "📝 Cadastro" 
if "ultimo_cadastro" not in st.session_state:
    st.session_state.ultimo_cadastro = ""

def cadastrar(nome, username, senha, confirmar):
    if username in st.session_state.usuarios:
        st.warning("⚠️ Esse nome de usuário já está cadastrado.")
    elif len(senha) < 8:
        st.error("🔒 A senha deve ter no mínimo 8 caracteres.")
    elif senha != confirmar:
        st.error("❌ As senhas não coincidem.")
    else:
        st.session_state.usuarios[username] = {"senha": senha, "nome": nome}
        st.session_state.ultimo_cadastro = username
        st.session_state.menu = "🔑 Login"
        
        st.success("✅ Cadastro realizado com sucesso! Redirecionando para login...")
        st.rerun()

def login(username, senha):
    if username in st.session_state.usuarios and st.session_state.usuarios[username]["senha"] == senha:
        st.session_state.logado = True
        st.session_state.usuario_atual = username
        st.session_state.menu = "👤 Minha Conta"
        st.success(f"🎉 Bem-vindo, {st.session_state.usuarios[username]['nome']}!")
        st.rerun()
    else:
        st.error("❌ Usuário ou senha inválidos.")

st.sidebar.write("---")
menu = st.sidebar.radio(
    "📌 Navegação",
    ["📝 Cadastro", "🔑 Login", "👤 Minha Conta"],
    index=["📝 Cadastro", "🔑 Login", "👤 Minha Conta"].index(st.session_state.menu)
)

if menu != st.session_state.menu:
    st.session_state.menu = menu
    st.rerun()

if menu == "📝 Cadastro":
    st.header("📝 Cadastro")
    st.write("Página de cadastro do TravelTun.")

    nome = st.text_input("📌 Nome completo")
    novo_username = st.text_input("👤 Nome de usuário")
    nova_senha = st.text_input("🔒 Senha", type="password")
    confirmar_senha = st.text_input("🔒 Confirmar senha", type="password")

    if st.button("Cadastrar ➕"):
        cadastrar(nome, novo_username, nova_senha, confirmar_senha)

elif menu == "🔑 Login":
    st.header("🔑 Login")
    username = st.text_input("👤 Nome de usuário", value=st.session_state.ultimo_cadastro)
    senha = st.text_input("🔒 Senha", type="password")

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Entrar 🚀"):
            login(username, senha)
    with col2:
        if st.button("📝 Criar nova conta"):
            st.session_state.menu = "📝 Cadastro"
            st.rerun()

elif menu == "👤 Minha Conta":
    st.header("👤 Minha Conta")

    if st.session_state.logado:
        usuario = st.session_state.usuario_atual
        dados = st.session_state.usuarios[usuario]

        col1, col2 = st.columns(2)
        with col1:
            st.info(f"📌 Nome completo: **{dados['nome']}**")
        with col2:
            st.info(f"👤 Nome de usuário: **{usuario}**")

        if st.button("Sair ⏏️"):
            st.session_state.logado = False
            st.session_state.usuario_atual = None
            st.session_state.menu = "🔑 Login"  
            st.rerun()
    else:
        st.error("⚠️ Você precisa estar logado para acessar sua conta.")
        st.session_state.menu = "🔑 Login"  
        st.rerun()

st.markdown("---")
if st.session_state.logado:
    if st.button("Avançar para Viagem ➡️"):
        st.switch_page("pages/3_viagem.py")
else:
    st.info("🔒 Faça login para acessar as funcionalidades completas do TravelTun")