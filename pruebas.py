import streamlit as st
import numpy as np
import pandas as pd

import requests

from pyproj import Proj, transform


response = requests.get('http://127.0.0.1:8000/bibliotecas/')
coordenadas = []

print(type(response.json()))
for row in response.json():
    coordenadas.append([float(row[9]), float(row[10])])


print(coordenadas)
map_data = pd.DataFrame(
   coordenadas,
    columns=['lon', 'lat'])


st.write(response.json())

st.map(map_data)