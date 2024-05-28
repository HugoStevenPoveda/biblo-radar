
from services.DatabaseConnection import DatabaseConnection

class LibroService:
    

    def get_libro_by_title( self, title):
        
        libros = []
        db_connection = DatabaseConnection()
        db_connection.connect()
        query = """
            SELECT * FROM libros WHERE titulo ILIKE %s
        """
        cursor = db_connection.execute(query, ('%' + title + '%',))
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        libros = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        db_connection.disconnect()
        return libros
    
   
