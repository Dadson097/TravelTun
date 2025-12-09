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

if "viagens" not in st.session_state:
    st.session_state.viagens = []

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}  
        #MainMenu {visibility: hidden;}               
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

if st.session_state.viagens:
    for i, viagem in enumerate(st.session_state.viagens, start=1):
        with st.expander(f"✈️ Viagem {i}: {viagem['destino']}"):
            st.write(f"📅 **Data:** {viagem['data']}")
            st.write(f"💰 **Orçamento:** R$ {viagem['orcamento']:,.2f}".replace(".", ","))

            if viagem["atividades"]:
                st.write("🎯 **Atividades planejadas:**")
                for atividade in viagem["atividades"]:
                    st.write(f"   • {atividade['nome']} - R$ {atividade['custo']:,.2f}".replace(".", ","))

                total_gasto = sum(a["custo"] for a in viagem["atividades"])
                st.metric("💵 Total das atividades", f"R$ {total_gasto:,.2f}".replace(".", ","))

                if total_gasto > viagem["orcamento"]:
                    st.error(f"⚠ Gastos ultrapassaram o orçamento em R$ {(total_gasto - viagem['orcamento']):,.2f}".replace(".", ","))
                else:
                    sobra = viagem["orcamento"] - total_gasto
                    st.success(f"✅ Dentro do orçamento! Ainda sobram R$ {sobra:,.2f}".replace(".", ","))
                    st.metric("📊 Saldo do orçamento", f"R$ {sobra:,.2f}".replace(".", ","))

                st.markdown("---")
                
                atividades_para_cortar = st.multiselect(
                    f"✂️ Selecione atividades para cortar da Viagem {i}",
                    options=[a["nome"] for a in viagem["atividades"]],
                    key=f"corte_multi_{i}"
                )

                if st.button(f"Cortar atividades selecionadas da Viagem {i}", key=f"btn_corte_multi_{i}"):
                    if atividades_para_cortar:
                        economia_total = 0
                        for nome in atividades_para_cortar:
                            atividade = next(a for a in viagem["atividades"] if a["nome"] == nome)
                            economia_total += atividade["custo"]
                            viagem["atividades"].remove(atividade)

                        novo_total = sum(a["custo"] for a in viagem["atividades"])
                        novo_saldo = viagem["orcamento"] - novo_total

                        st.success(f"✅ Atividades cortadas! Economia total: R$ {economia_total:,.2f}".replace(".", ","))
                        st.metric("Novo total das atividades", f"R$ {novo_total:,.2f}".replace(".", ","))
                        st.metric("Novo saldo do orçamento", f"R$ {novo_saldo:,.2f}".replace(".", ","))
                    else:
                        st.info("ℹ️ Nenhuma atividade selecionada para cortar.")

            else:
                st.info("ℹ️ Nenhuma atividade cadastrada para esta viagem.")
else:
    st.warning("⚠️ Nenhuma viagem cadastrada ainda.")

st.markdown("---")
if st.button("Avançar ➡️"):
    st.switch_page("pages/5_avaliacao.py")
