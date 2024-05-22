import streamlit as st
import pandas as pd

# Datos de ejemplo
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Laura'],
    'Edad': [30, 25, 40, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

# Crear un DataFrame de ejemplo
df = pd.DataFrame(data)

# Mostrar la tabla en Streamlit
st.write(df)

# Manejar el evento de clic en una fila de la tabla
for index, row in df.iterrows():
    if st.button(f"Seleccionar fila {index}"):
        st.write(f'Se ha hecho clic en la fila {index}: {row}')
