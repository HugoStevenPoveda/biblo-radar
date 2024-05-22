import streamlit as st
import pandas as pd
import numpy as np

import streamlit_option_menu
from streamlit_option_menu import option_menu

from card_libros import biblioteca_card_border
from buscador import buscador


st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)


# Llamar al componente personalizado con los datos de ejemplo
lista_bibliotecas = []


with st.sidebar:
    selected = option_menu(
        menu_title="Bibliotecas Radar",
        options=["Home", "Contact Us"],
        icons=["house", "envelope"],
        menu_icon="cast",
        default_index=0,
        # orientation = "horizontal",
    )
if selected == "Home":

    st.header('Buscador libros ')
    with st.container():
        result = buscador()
        if result:
            for obj in result:
                lista_bibliotecas.append(
                    {'autor': obj['autor'], 'titulo': obj['titulo'],
                        'descripcion': obj['descripcion']}
                )

    with st.container():
        # Dividir la pantalla en columnas
        # Puedes ajustar el número de columnas según sea necesario
        columnas = st.columns(3)

    # Iterar sobre la lista de bibliotecas y mostrar cada una en una columna
        for i, biblioteca in enumerate(lista_bibliotecas):
            with columnas[i % len(columnas)]:
                biblioteca_card_border(**biblioteca)
    with st.container():
        st.header('Buscador libros ')


if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")
