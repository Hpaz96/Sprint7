import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Encabezado de la aplicación
st.header('Análisis de anuncios de venta de vehículos')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )

    fig_hist = go.Figure(
        data=[go.Histogram(x=car_data['odometer'])]
    )

    fig_hist.update_layout(
        title_text='Distribución del Odómetro'
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión entre odómetro y precio'
    )

    fig_scatter = go.Figure(
        data=[go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers'
        )]
    )

    fig_scatter.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
