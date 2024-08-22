import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Visualización de datos - Anuncios de venta de coches') # crear un encabezado

# crear una casilla de verificación
build_histogram = st.checkbox('Construye un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
 # escribir un mensaje
    st.write('Creación de un histograma considerando el odómetro de los coches.')
           
 # crear un histograma 
    fig = px.histogram(car_data, x="odometer")
       
 # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

# crear una casilla de verificación
build_dispersion = st.checkbox('Construye un gráfico de dispersión')

if build_dispersion: # si la casilla de verificación está seleccionada
 # escribir un mensaje
    st.write('Creación de un gráfico de dispersión considerando el odómetro y el precio de los coches.')
           
 # crear un gráfico de dispersión 
    fig = px.scatter(car_data, x="odometer", y="price")
    
 # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)