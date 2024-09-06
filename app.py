import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Autos",divider="gray")

hist_chk = st.checkbox("Construir histograma")
hist_disp_chk = st.checkbox("Construir gráfico de dispersión")

if hist_chk:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", nbins=20)
    st.plotly_chart(fig, use_container_width=True)
if hist_disp_chk:
    st.write('Creación de un histograma de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)