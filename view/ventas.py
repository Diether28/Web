import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("Filtrar Datos y Captura de Datos")
st.write("El procesamiento de datos a través de Ciencia de Datos usando Streamlit de Python")

dfDatos = pd.read_csv('http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

# Mostrar la tabla de los registros
st.metric("***Registros Totales***", len(dfDatos))
st.dataframe(dfDatos, use_container_width=True)

# Crear un gráfico de dispersión con colores basados en el continente
fig_scatter = px.scatter(dfDatos, x='mean_house_income', y='lifeExpectancy', color='continent', 
                         title='Gráfico de Dispersión del Ingreso Medio del Hogar vs Esperanza de Vida',
                         labels={'mean_house_income':'Ingreso Medio del Hogar', 'lifeExpectancy':'Esperanza de Vida', 'continent':'Continente'})
st.plotly_chart(fig_scatter)

# Crear un gráfico de líneas con colores basados en el continente
fig_line = px.line(dfDatos, x='year', y='population', color='continent', 
                   title='Gráfico de Líneas de la Población a lo Largo del Tiempo',
                   labels={'year':'Año', 'population':'Población', 'continent':'Continente'})
st.plotly_chart(fig_line)

# Crear un gráfico de barras con colores basados en el continente
fig_bar = px.bar(dfDatos, x='continent', y='population', color='continent', 
                 title='Gráfico de Barras de la Población por Continente',
                 labels={'continent':'Continente', 'population':'Población'})
st.plotly_chart(fig_bar)
