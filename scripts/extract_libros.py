import subprocess
import os
import shutil
from minio import Minio
from minio.error import S3Error

# URL del repositorio de GitHub
url_repositorio = 'https://github.com/HugoStevenPoveda/datos_libros.git'
# Directorio donde se ejecuta el script Python
directorio_destino = os.getcwd() 

def clonar_repositorio(url_repositorio, directorio_destino):
    try:
        # Ejecuta el comando git clone en el directorio actual
        subprocess.run(['git', 'clone', url_repositorio, './datos'])
    except ImportError as e:
        print("directorio existe ")

def eliminar_carpeta_con_contenido(ruta_carpeta):
    try:
        # Eliminar la carpeta y su contenido
        shutil.rmtree(ruta_carpeta)
        print(f"La carpeta '{ruta_carpeta}' y su contenido fueron eliminados correctamente.")
    except OSError as e:
        print(f"Error al eliminar la carpeta '{ruta_carpeta}': {e}")

def subir_archivos_a_minio(minio_client, ruta_carpeta, bucket_name):
    # Iterar sobre los archivos en la carpeta y subirlos a Minio
    for raiz, directorios, archivos in os.walk(ruta_carpeta):
        for nombre_archivo in archivos:
            ruta_completa = os.path.join(raiz, nombre_archivo)
            try:
                # Subir el archivo a Minio
                minio_client.fput_object(bucket_name, nombre_archivo, ruta_completa)
                print(f"Archivo '{nombre_archivo}' subido correctamente.")
            except S3Error as exc:
                print("error occurred.", exc)

if __name__ == "__main__":
    print(directorio_destino)
    eliminar_carpeta_con_contenido(directorio_destino+"/datos")
    clonar_repositorio(url_repositorio, directorio_destino)
    
    # Configuración de conexión a Minio
    minio_client =Minio(
            endpoint='minio:9000',
            access_key='User',
            secret_key='p4ssw0rd',
            secure=False)

    bucket_name = 'bucketlibros'

    # Ruta de la carpeta que deseas subir
    ruta_carpeta = directorio_destino+"/datos/libros_json"
    
    # Subir archivos a Minio
    subir_archivos_a_minio(minio_client, ruta_carpeta, bucket_name)
    eliminar_carpeta_con_contenido(directorio_destino+"/datos")
