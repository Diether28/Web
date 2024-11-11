import streamlit as st
from forms.contacto import contact_form
# @st.dialog(&quot;cont&quot;)
# def ver_contacto():
# name = st.text_input(&quot;Nombre:&quot;, placeholder=&quot;Escribir Nombres&quot;)
# email = st.text_input(&quot;Email:&quot;, placeholder=&quot;nombre@email.com&quot;)
# message = st.text_area(&quot;Mensaje:&quot;)
# st.write(&quot;---&quot;)
# submit_button = st.button(&quot;Enviar&quot;, use_container_width=True)

#Ventana modal
@st.dialog("contacto")
def ver_form_contacto():
    contact_form()
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center&quot")
    with col1:
        st.image("img/dioni.png", width=230)
    with col2:
        st.title("Dionicio Manzanares", anchor=False)
        st.write(
            "Analista de datos senior, que ayuda a las empresas apoyando la toma de decisiones basada endatos. Como Ciencia de Datos.")
        if st.button("Contacto"): # Mostrar botón ventana modal
            ver_form_contacto()
# if st.button("cont"):
# ver_contacto()
# --- Experiencia y calificaciones ---
st.write("\n")
st.subheader("Experiencia y calificaciones", anchor=False)
st.write(
"""
- 7 años de experiencia extrayendo información útil a partir de datos.
- Fuerte experiencia práctica y conocimiento en Python y Excel.
- Buen conocimiento de los principios estadísticos y sus respectivas aplicaciones.
- Excelente jugador de equipo y con un fuerte sentido de iniciativa en las tareas.
"""
)
# --- HABILIDADES ---
st.write("\n")
st.subheader("Habilidades", anchor=False)
st.write(
"""
- Programación: Python (Scikit-learn, Pandas), SQL, VBA
- Visualización de Datos: PowerBi, MS Excel, Plotly
- Modelado: Logistic regression, linear regression, decision trees
- Base de Datos: Postgres, MongoDB, MySQL
"""
)