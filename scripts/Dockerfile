# Usa una imagen base oficial de Python
FROM python:3.9.19-alpine3.20
RUN apk update && apk add --no-cache git

# Establece el directorio de trabajo
WORKDIR /app
COPY requirements.txt /app/requirements.txt

COPY urls.txt /app/urls.txt

# Copia tus scripts de Python al directorio de trabajo en el contenedor
COPY extract_libros.py /app/
COPY extract_urls.py /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Instala las dependencias si es necesario (usando pip install)

# Define el comando por defecto que se ejecutará al iniciar el contenedor
CMD ["sh", "-c", "python extract_urls.py && python extract_libros.py"]
