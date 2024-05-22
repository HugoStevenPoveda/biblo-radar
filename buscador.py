import streamlit as st
import requests

# Título de la aplicación


def buscador():

    # Widget para ingresar el texto a buscar
    texto_busqueda = st.text_input('Ingrese el texto a buscar')

    # Botón para enviar la búsqueda a la API REST
    if st.button('Buscar'):
        # Comprobamos si se ingresó texto
        if texto_busqueda:
            # Enviar el texto a la API REST
            url_api = 'http://localhost:8000/libro/'+texto_busqueda
            response = requests.get(url_api)

            # Mostrar el resultado de la búsqueda
            if response.status_code == 200:
                return response.json()
              
            else:
                st.error(
                    f'Error al realizar la búsqueda: {response.status_code}')
        else:
            st.warning('Por favor, ingrese texto para realizar la búsqueda')
