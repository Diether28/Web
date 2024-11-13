import os
from dotenv import load_dotenv
import google.generativeai as gemini

# Cargar las variables de entorno
load_dotenv()

# Obtener la clave de la API
api_key = os.getenv('Gemini_key')

if not api_key:
    raise ValueError("N se encontro la clave de la api en las variables")

gemini.configure(api_key = api_key)

prompt = "Genera un poema sobre inteligencia artificial"
model = gemini.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content(prompt)

Generate_text = response('Generate_text','No se pudo generar texto')
print(Generate_text)