import streamlit as st


home = st.Page(
    page="view/home.py",
    title="Inicio",
    icon="🏠",
    default=True
)

acerca_de = st.Page(
    page="view/acerca_de.py",
    title="Acerca de",
    icon="👤",
)

project_1 = st.Page(
    page="view/ventas.py",
    title="Ventas",
    icon="🛒"
)

project_2 = st.Page(
    page="view/chatbot.py",
    title="Chatbot",
    icon="🤖"
)

pg = st.navigation(
    {
        "Informacion:":[home,acerca_de],
        "Projectos:":[project_1,project_2],
    }
)

# --Logo y derechos de actor--
st.sidebar.markdown("Elaborado con ❤️ por [Streamlit](https://share.streamlit.io/user/diether28)")

pg.run()