import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
streamlit
pandas
matplotlib
seaborn

# Configuración del título del dashboard
st.set_page_config(page_title='Dashboard de Exportaciones', layout='wide')

# Cargar los datos desde los archivos de GitHub
@st.cache_data
def load_data():
    exportaciones_url = 'https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/exportaciones.csv'
    segmentos_url = 'https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/segmentos.csv'
    exportaciones_df = pd.read_csv(exportaciones_url)
    segmentos_df = pd.read_csv(segmentos_url)
    return exportaciones_df, segmentos_df

exportaciones_df, segmentos_df = load_data()

# Mostrar el título del dashboard
st.title('Dashboard Interactivo de Exportaciones')

# Sección de exportaciones por país
st.header('Exportaciones por País')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='País', y='Exportaciones (USD millones)', data=exportaciones_df, ax=ax)
ax.set_title('Exportaciones por País (en millones de USD)')
ax.set_ylabel('Millones de USD')
ax.set_xlabel('País')
st.pyplot(fig)

# Sección de segmentos de clientes por país
st.header('Segmentos de Clientes por País')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='País', y='Tamaño del Mercado (USD millones)', hue='Segmento de Clientes', data=segmentos_df, ax=ax)
ax.set_title('Segmentos de Clientes por País (en millones de USD)')
ax.set_ylabel('Millones de USD')
ax.set_xlabel('País')
st.pyplot(fig)

# Mostrar las tablas de datos para revisión
st.subheader('Datos de Exportaciones')
st.dataframe(exportaciones_df)

st.subheader('Datos de Segmentos de Clientes')
st.dataframe(segmentos_df)

# Mensaje de cierre
st.write('Dashboard creado con datos de exportaciones y segmentos de clientes.')
