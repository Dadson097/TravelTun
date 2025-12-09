import streamlit as st

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Sistema de Avaliação",
    page_icon="⭐", 
    layout="wide"
)

with st.sidebar:
    st.title("🌍 TravelTun")
    st.page_link("1_sobre.py", label="🏠 Sobre")
    st.page_link("pages/2_cadastro.py", label="📝 Cadastro")
    st.page_link("pages/3_viagem.py", label="✈️ Viagem")
    st.page_link("pages/4_listagem.py", label="📋 Listagem")
    st.page_link("pages/5_avaliacao.py", label="⭐ Avaliação")
st.markdown("---")
st.markdown("### 🔐 Conta")

if not st.session_state.get("logado", False):
    st.warning("⚠️ Você precisa fazer login para acessar esta página.")
    st.stop()

if "avaliacoes" not in st.session_state:
    st.session_state["avaliacoes"] = []

st.markdown(
    "<h1 style='text-align:center; color:#FFD700;'>⭐ Sistema de Avaliação</h1>",
    unsafe_allow_html=True
)

st.subheader("✨ Avalie o nosso sistema TravelTun")
st.write("Bem-vindo ao sistema de avaliação de viagens! Sua opinião é muito importante para nós.")

col1, col2 = st.columns([2,1])
with col1:
    nome = st.text_input("👤 Digite seu nome:")
with col2:
    nota = st.slider("⭐ Avalie de 1 a 5:", 1, 5, 3)

comentario = st.text_area(
    "💬 Deixe seu comentário (opcional):",
    placeholder="O que você mais gostou? Tem alguma sugestão?",
    height=100,
    help="Seu feedback nos ajuda a melhorar o sistema!"
)

if st.button("📩 Enviar avaliação", type="primary"):
    if nome.strip() == "":
        st.error("⚠️ Por favor, digite seu nome antes de enviar.")
    else:
        st.session_state["avaliacoes"].append({
            "nome": nome, 
            "nota": nota,
            "comentario": comentario if comentario.strip() else "Sem comentário"
        })
        st.success(f"🎉 Obrigado {nome}, você deu nota {nota} ⭐")

if st.session_state["avaliacoes"]:
    st.markdown("---")
    st.write("### 📋 Avaliações recebidas:")

    for i, avaliacao in enumerate(st.session_state["avaliacoes"], start=1):
        estrelas = "⭐" * avaliacao['nota']
        
        with st.expander(f"{i}. {avaliacao['nome']} → {estrelas}"):
            st.write(f"**Nota:** {avaliacao['nota']}/5")
            if avaliacao['comentario'] != "Sem comentário":
                st.write(f"**Comentário:** {avaliacao['comentario']}")
            else:
                st.write("**Comentário:** *Nenhum comentário*")
    
    notas = [a["nota"] for a in st.session_state["avaliacoes"]]
    media = sum(notas) / len(notas)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📊 Média das avaliações", f"{media:.2f} ⭐")
    with col2:
        st.metric("📈 Total de avaliações", len(st.session_state["avaliacoes"]))
    
    st.markdown("---")
    st.write("### 📈 Estatísticas")
    
    contagem_notas = {}
    for avaliacao in st.session_state["avaliacoes"]:
        nota = avaliacao['nota']
        contagem_notas[nota] = contagem_notas.get(nota, 0) + 1
    
    for n in range(5, 0, -1):
        count = contagem_notas.get(n, 0)
        percent = (count / len(st.session_state["avaliacoes"])) * 100 if st.session_state["avaliacoes"] else 0
        st.write(f"{'⭐' * n} ({n} estrelas): {count} avaliações ({percent:.1f}%)")
        st.progress(percent / 100)
    
else:
    st.info("Ainda não recebemos nenhuma avaliação. Seja o primeiro a avaliar! ✨")

st.markdown("---")
if st.button("🗑️ Limpar todas as avaliações"):
    st.session_state["avaliacoes"] = []
    st.success("Avaliações limpas com sucesso!")

    st.rerun()
