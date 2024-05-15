
import sys
sys.path.append(r'src/app_biblio/')
from services.DatabaseConnection import DatabaseConnection


class BibliotecaService:
    


    def get_bibliotecas(self):
        bibliotecas = []
        db_connection = DatabaseConnection()
        db_connection.connect()
        query = """
            SELECT * FROM bibliotecas_inf
        """
        cursor =db_connection.execute(query)
        for row in cursor.fetchall():
                bibliotecas.append(row)
        cursor.close()
        db_connection.disconnect()
        return bibliotecas
    
