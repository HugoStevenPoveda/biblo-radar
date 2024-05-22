import streamlit as st
import pandas as pd
import requests
response = requests.get('http://127.0.0.1:8000/bibliotecas/')
coordenadas = []
print(type(response.json()))
for obj in response.json():
    coordenadas.append([float(obj['longitud']),
                        float(obj['latitud'])])

map_data = pd.DataFrame(
    coordenadas,
    columns=['lon', 'lat'])

st.map(map_data)
