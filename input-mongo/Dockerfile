# Usar una imagen base oficial de Python
FROM python:3.9.19-alpine3.20

WORKDIR /app

COPY . /app/


# Instalar las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 7000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7000"]