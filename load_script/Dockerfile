# Usa una imagen base oficial de Python
FROM python:3.9.19-alpine3.20

# Establece el directorio de trabajo
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Instala las dependencias si es necesario (usando pip install)

# Define el comando por defecto que se ejecutará al iniciar el contenedor
CMD ["sh", "-c", "python load_biblos.py && python load_libros.py && python load_libros_biblo.py "]