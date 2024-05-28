
from DatabaseConnection import DatabaseConnection
from Libro import Libro , LibroBuilder
import json
from minio import Minio
from minio.error import S3Error



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
    list_libros = []
    for file in json_files:
        try:
            print(f"Leyendo archivo: {file}")
            data = minio_client.get_object(bucket_name, file)
            # Leer los datos del archivo
            json_content = data.read().decode('utf-8')
            json_data = json.loads(json_content)
            for elemento in json_data:
                print("///////////////////////////")
                try:
                    try:
                        autor =  elemento['autor_entidades']  
                    except:
                        autor =  elemento['autor_personas'] 
                              
                    libro = LibroBuilder()\
                        .set_id( elemento['id_BNE'])\
                        .set_autor(autor)\
                        .set_titulo(elemento['título'])\
                        .set_descripcion(elemento['descripcion_notas'])\
                        .set_genero(elemento['genero_forma'])\
                        .set_fecha_publicacion(elemento['fecha_publicacion'])\
                        .set_version_digital(elemento['version_digital'])\
                        .build()
                    list_libros.append(libro)
                except Exception as e:
                    print("Error:", e)
                    continue
            load_biblos_bd(list_libros)
            list_libros=[]
           
        
        except S3Error as err:
            print(err)
            print(err)

    


def load_biblos_bd(libros):
    """
    Imprime la información de los biblos en los datos JSON.
    """
    db_connection = DatabaseConnection()
    db_connection.connect()

    query = """
            INSERT INTO libros (id, autor, titulo, descripcion, genero, fecha_publicacion, version_digital)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    for libro in libros:
        valores = (
            libro.id,
            libro.autor,
            libro.titulo,
            libro.descripcion,
            libro.genero,
            libro.fecha_publicacion,
            libro.version_digital
        )
        cursor =db_connection.execute(query, valores)
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
    bucket_name = 'bucketlibros'

    # Conexión a MinIO
    minio_client = connect_to_minio(
        minio_endpoint, minio_access_key, minio_secret_key, minio_secure)

    # Obtener archivos JSON
    json_files = list_json_files(minio_client, bucket_name)

    # Cargar datos JSON
    list_bibliotecas = load_json_data_to_list(
        minio_client, bucket_name, json_files)

    # Imprimir información de los biblos
   # load_biblos_bd(list_bibliotecas)
