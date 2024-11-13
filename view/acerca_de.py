import streamlit as st
from forms.contacto import contact_form

def ver_form_contacto():
    # Ventana modal para el formulario de contacto
    contact_form()

def mostrar():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("image/appdes.png", width=230)
    with col2:
        st.title("Diether Salablanca", anchor=False)
        st.write(
            "Analista de datos junior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. "
            "Especializado en Ciencia de Datos."
        )
  # Botón para mostrar el formulario de contacto en la ventana modal
    if st.button("Contacto"):  
        ver_form_contacto()

    # --- Experiencia y calificaciones ---
st.write("\n")
st.subheader("Experiencia y calificaciones", anchor=False)
st.write("""
- Fuerte experiencia práctica y conocimiento en Python.
- Buen conocimiento sobre la creaciones de app moviles.
""")

    # --- HABILIDADES ---
st.write("\n")
st.subheader("Habilidades", anchor=False)
st.write("""
- Programación: Python (FastApi,Flask,Streamlit) y creacion de videos Juegos(godot)
- Visualización de Datos:Plotly
- Base de Datos:MongoDB, MySQL
    """)

# Llama a la función principal
mostrar()