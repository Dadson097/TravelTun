import streamlit as st

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

st.markdown(
    "<h1 style='text-align:center; color:#1E90FF;'>✈️ Sobre o TravelTun ✨</h1>",
    unsafe_allow_html=True
)

st.write(
    "O **TravelTun** nasceu com a ideia de tornar o planejamento de viagens e passeios de fim de semana "
    "algo simples, prático e eficiente. Muitas vezes, organizar um roteiro pode parecer complicado, "
    "mas aqui você encontra uma forma fácil de reunir tudo em um só lugar: destinos, atividades e orçamento."
)

st.write(
    "Nosso propósito é ajudar você a aproveitar melhor o tempo livre, seja explorando novos destinos "
    "ou redescobrindo lugares próximos. Entendemos que momentos de lazer são essenciais para o bem-estar, "
    "e por isso criamos ferramentas que permitem montar roteiros personalizados sem complicação."
)

st.markdown("---")

st.subheader("🌟 Com o TravelTun, você pode:")
st.markdown("""
- 🔐 Criar ou simular uma conta de acesso  
- 📍 Cadastrar os locais que deseja visitar  
- 📅 Definir datas e atividades para cada viagem  
- 💰 Estimar o orçamento total  
- ✂️ Simular cortes de gastos para economizar  
- ⭐ Avaliar sua experiência após o passeio  
""")

col1, col2 = st.columns(2)
with col1:
    st.success("✅ Planejamento rápido e prático")
with col2:
    st.info("🌍 Explore novos destinos ou redescubra os próximos de você")

st.markdown("---")

st.markdown(
    "<h3 style='text-align:center; color:#228B22;'>Porque viajar bem começa com um bom plano — e é exatamente isso que o TravelTun oferece. 🌟</h3>",
    unsafe_allow_html=True
)

if st.button("Avançar ➡️"):
    st.switch_page("pages/2_cadastro.py")