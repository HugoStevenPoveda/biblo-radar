# Usar una imagen base oficial de Python
FROM python:3.9.19-alpine3.20

WORKDIR /app

# Copiar el archivo de requisitos y el directorio de scripts al contenedor
COPY requirements.txt /app/requirements.txt
COPY app_biblio/ /app/app_biblio/

# Instalar las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app_biblio.controller.appController:app", "--host", "0.0.0.0", "--port", "8000"]
