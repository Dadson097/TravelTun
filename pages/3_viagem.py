import streamlit as st

st.set_page_config(
    page_title="Sobre o TravelTun",
    page_icon="🌍",
    layout="wide"
)

st.set_page_config(
    page_title="Sobre o TravelTun",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}  /* menu original */
        #MainMenu {visibility: hidden;}               /* menu superior */
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🌍 TravelTun")

    st.page_link("1_sobre.py", label="🏠 Sobre")
    st.page_link("pages/2_cadastro.py", label="📝 Cadastro")
    st.page_link("pages/3_viagem.py", label="✈️ Viagem")
    st.page_link("pages/4_listagem.py", label="📋 Listagem")
    st.page_link("pages/5_avaliacao.py", label="⭐ Avaliação")

if not st.session_state.get("logado", False):
    st.warning("⚠️ Você precisa fazer login para acessar esta página.")
    st.stop()

st.set_page_config(page_title="Cadastro de Viagem", page_icon="✈️", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#1E90FF;'>📋 Cadastro de Viagem</h1>",
    unsafe_allow_html=True
)

if "viagens" not in st.session_state:
    st.session_state.viagens = []
if "atividades_temp" not in st.session_state:
    st.session_state.atividades_temp = []

st.subheader("🌍 Informações da Viagem")
col1, col2 = st.columns(2)
with col1:
    destino = st.text_input("📍 Destino da viagem")
with col2:
    data = st.date_input("📅 Data da viagem")

orcamento = st.number_input(
    "💰 Orçamento estimado (R$)",
    min_value=0.0,
    step=50.0,
    format="%.2f"
)

st.markdown("---")

st.subheader("🎯 Adicionar atividades")
colA, colB = st.columns([2, 1])
with colA:
    nome_atividade = st.text_input("Nome da atividade")
with colB:
    custo_atividade = st.number_input(
        "Custo (R$)",
        min_value=0.0,
        step=1.0,
        format="%.2f"
    )

if st.button("➕ Adicionar atividade"):
    if nome_atividade.strip() and custo_atividade > 0:
        st.session_state.atividades_temp.append(
            {"nome": nome_atividade.strip(), "custo": custo_atividade}
        )
        st.success(f"✅ Atividade **{nome_atividade}** adicionada com sucesso!")
    else:
        st.warning("⚠️ Preencha o nome e um custo maior que zero.")

if st.session_state.atividades_temp:
    st.write("### 📋 Atividades cadastradas até agora:")

    atividades_formatadas = []
    for i, atividade in enumerate(st.session_state.atividades_temp, start=1):
        valor = f"{atividade['custo']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        atividades_formatadas.append({
            "index": i,
            "Atividade": atividade["nome"],
            "Custo (R$)": f"R$ {valor}"
        })

    st.data_editor(
        atividades_formatadas,
        hide_index=True,
        column_config={
            "index": st.column_config.NumberColumn(label="#", format="%d"),
            "Atividade": st.column_config.TextColumn("Atividade"),
            "Custo (R$)": st.column_config.TextColumn("Custo (R$)")
        }
    )

st.markdown("---")

if st.button("💾 Salvar viagem"):
    if destino and data and orcamento > 0:
        nova_viagem = {
            "destino": destino,
            "data": str(data),
            "orcamento": orcamento,
            "atividades": st.session_state.atividades_temp.copy()
        }
        st.session_state.viagens.append(nova_viagem)
        st.session_state.atividades_temp = []
        st.success("🎉 Viagem cadastrada com sucesso!")
    else:
        st.warning("⚠️ Preencha todos os campos corretamente antes de salvar.")

if st.button("Avançar ➡️"):
    st.switch_page("pages/4_listagem.py")