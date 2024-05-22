
from services.DatabaseConnection import DatabaseConnection

class BibliotecaService:
    

    def get_bibliotecas(self):
        bibliotecas = []
        db_connection = DatabaseConnection()
        db_connection.connect()
        query = """
            SELECT * FROM bibliotecas_inf
        """
        cursor = db_connection.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        bibliotecas = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        db_connection.disconnect()
        return bibliotecas
    
    
    def get_bibliotecas_by_id_libro(self, id_libro):
        bibliotecas = []
        db_connection = DatabaseConnection()
        db_connection.connect()
        query =  """
            SELECT b.id, b.nombre,b.longitud , b.latitud 
            FROM bibliotecas_inf b
            JOIN biblioteca_libro bl ON b.id = bl.biblioteca_id
            WHERE bl.libro_id = %s
        """
        cursor = db_connection.execute(query, ('' + id_libro + '',))
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        bibliotecas = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        db_connection.disconnect()
        return bibliotecas
    
