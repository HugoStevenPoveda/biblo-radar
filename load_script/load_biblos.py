
import json
from minio import Minio
from minio.error import S3Error
from Biblioteca import Biblioteca , BibliotecaBuilder
from DatabaseConnection import DatabaseConnection


def connect_to_minio(endpoint, access_key, secret_key, secure=False):
    """
    Establece una conexión con MinIO.
    """
    return Minio(endpoint=endpoint, access_key=access_key, secret_key=secret_key, secure=secure)


def list_json_files(minio_client, bucket_name):
    """
    Lista los archivos JSON en un bucket de MinIO.
    """
    try:
        objects = minio_client.list_objects(bucket_name, recursive=True)
        # Filtrar los objetos que tienen extensión .json
        return [obj.object_name for obj in objects if obj.object_name.endswith('.json')]
    except S3Error as err:
        print(err)
        return []


def load_json_data_to_list(minio_client, bucket_name, json_files):
    """
    Carga los datos JSON de los archivos en un diccionario.
    """
    json_data = {}
    dict_biblos = []
    for file in json_files:
        try:
            print(f"Leyendo archivo: {file}")
            data = minio_client.get_object(bucket_name, file)
            # Leer los datos del archivo
            json_content = data.read().decode('utf-8')
            json_data[file] = json.loads(json_content)
            for biblo in json_data['url1.json']['features']:
                biblo = biblo['properties']
    
                biblioteca_builder = BibliotecaBuilder()
                biblioteca = biblioteca_builder\
                    .set_nombre(biblo['LECNOMBRE'])\
                    .set_direccion(biblo['LECDIRECCI'])\
                    .set_telefono(biblo['LECTELEFON'])\
                    .set_email(biblo['LECEMAIL'])\
                    .set_pagina_web(biblo['LECPAGWEB'])\
                    .set_estado(biblo['LECESTADO'])\
                    .set_nodo(biblo['LECNODO'])\
                    .set_clasificacion(biblo['LECCLASIF'])\
                    .set_point_x(biblo['POINT_X'])\
                    .set_point_y(biblo['POINT_Y'])\
                    .build()
                dict_biblos.append(biblioteca)

                
                print(biblioteca)

        except S3Error as err:\
        
            print(err)
    return dict_biblos


def load_biblos_bd(bibliotecas):
    """
    Imprime la información de los biblos en los datos JSON.
    """
    db_connection = DatabaseConnection()
    db_connection.connect()
    
    query = "INSERT INTO bibliotecas_inf (nombre, direccion, telefono, email, pagina_web, estado, nodo, clasificacion,longitud, latitud, geom) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 3857))"
    
    for biblioteca in bibliotecas:
        valores = (biblioteca.nombre, biblioteca.direccion, biblioteca.telefono, biblioteca.email, biblioteca.pagina_web,biblioteca.estado, biblioteca.nodo, biblioteca.clasificacion, biblioteca.point_x, biblioteca.point_y , biblioteca.point_x, biblioteca.point_y)
        cursor = db_connection.execute(query,valores)
        db_connection.commit()
        cursor.close()
        
    db_connection.disconnect()
   



if __name__ == "__main__":
    # Configuración de MinIO
    minio_endpoint = 'minio:9000'
    minio_access_key = 'User'
    minio_secret_key = 'p4ssw0rd'
    minio_secure = False

    # Nombre del bucket en MinIO
    bucket_name = 'bucketbiblos'

    # Conexión a MinIO
    minio_client = connect_to_minio(
        minio_endpoint, minio_access_key, minio_secret_key, minio_secure)

    # Obtener archivos JSON
    json_files = list_json_files(minio_client, bucket_name)

    # Cargar datos JSON
    list_bibliotecas = load_json_data_to_list(minio_client, bucket_name, json_files)
  

    # Imprimir información de los biblos
    load_biblos_bd(list_bibliotecas)
