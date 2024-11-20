import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from cryptography.fernet import Fernet

# Cargar la API key desde el archivo .env
load_dotenv()

# Cargar la clave de encriptación
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Crear un objeto Fernet con la clave
cipher_suite = Fernet(key)

# Desencriptar la API key
encrypted_api_key = os.getenv("ENCRYPTED_API_KEY").encode()
api_key = cipher_suite.decrypt(encrypted_api_key).decode()

# Configurar el modelo Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash",tools="code_execution")

# Función para generar respuestas
def generate_response(prompt):
    response = model.generate_content(prompt, generation_config = genai.GenerationConfig(
        #max_output_tokens=1000,
        temperature=2.0,
    ))
    return response.text

# Configurar la interfaz de Streamlit
st.title("Chatbot con Gemini AI")
st.write("Hola, ¿cómo estás? ¿En qué puedo ayudarte hoy?")

# Input del usuario
user_input = st.text_input("Tu mensaje:")

# Procesar la entrada del usuario y mostrar la respuesta
if st.button("Enviar"):
    if user_input:
        response = generate_response(user_input)
        st.write("Chatbot:", response)
    else:
        st.write("Por favor, ingresa un mensaje.")
