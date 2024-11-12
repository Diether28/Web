import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("Filtrar Datos y Captura de Datos")
st.write("El procesamiento de datos a través de Ciencia de Datos usando Streamlit de Python")

dfDatos = pd.read_csv('http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

# Mostrar la tabla de los registros
st.metric("***Registros Totales***", len(dfDatos))
st.dataframe(dfDatos, use_container_width=True)

# crear filtros 
continent_filter = st.multiselect(
    "Selecciona los continentes:",
    options=dfDatos['continent'].unique(),
    default=dfDatos['continent'].unique()
)

# Campo de entrada para el pais
country_filter = st.text_input(
    "Escriba el nombre del País (opcional):",
    value= ""
)

# Rango de edad
age_range = st.slider( 
    "Selecciona el Rango de Edad:", 
    min_value=int(dfDatos['median_age_year'].min()), 
    max_value=int(dfDatos['median_age_year'].max()), 
    value=(int(dfDatos['median_age_year'].min()), int(dfDatos['median_age_year'].max()))
)

# Filtrar los datos basados en las selecciones
filtered_data = dfDatos[
    (dfDatos['continent'].isin(continent_filter)) &
    (dfDatos['country'].str.contains(country_filter, case=False, na=False)) &
    (dfDatos['median_age_year'] >= age_range[0]) &
    (dfDatos['median_age_year'] <= age_range[1])
]

# Mostrar la tabla de los registros filtrados y la métrica actualizada 
st.metric("***Registros Totales Filtrados***", len(filtered_data)) 
st.dataframe(filtered_data, use_container_width=True)

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
