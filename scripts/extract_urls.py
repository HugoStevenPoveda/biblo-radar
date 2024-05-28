import requests
from minio import Minio
from minio.error import S3Error
import json
from io import BytesIO
import time

def obtener_json_desde_url(url, intentos_maximos=5, tiempo_espera=6):
    for intento in range(1, intentos_maximos + 1):
        try:
            response = requests.get(url, timeout=20)  
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud:", e)
            if intento < intentos_maximos:
                print(f"Reintentando en {tiempo_espera} segundos ({intento}/{intentos_maximos})")
                time.sleep(tiempo_espera)
    return None

def guardar_json_en_minio(json_data, minio_client, bucket_name, file_name):
    try:
        json_bytes = BytesIO(json.dumps(json_data).encode('utf-8'))
        tamaño_objeto = json_bytes.getbuffer().nbytes
        minio_client.put_object(bucket_name, file_name, json_bytes, tamaño_objeto)
        print("JSON guardado exitosamente en MinIO:", file_name)
    except S3Error as exc:
        print("Error al guardar JSON en MinIO:", exc)

if __name__ == "__main__":
    # Configuración de MinIO
    minio_client = Minio(
        endpoint='minio:9000',
        access_key='User',
        secret_key='p4ssw0rd',
        secure=False
    )

    # Nombre del bucket en MinIO
    bucket_name = 'bucketbiblos'

    # URL del servicio REST
    urls = {}
    with open("/app/urls.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre, ruta = linea.strip().split("=")
            urls[nombre.strip()] = ruta.strip()

    # Iterar sobre las URLs y procesar cada JSON
    for nombre, url in urls.items():
        print(nombre, url)
        json_data = obtener_json_desde_url(url)
        if json_data:
            guardar_json_en_minio(json_data, minio_client, bucket_name, f"{nombre}.json")
