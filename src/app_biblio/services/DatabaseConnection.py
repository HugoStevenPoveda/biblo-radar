import psycopg2

class DatabaseConnection:
    
    _instance = None
    dbname = 'bibloradar'
    user = 'postgres'
    password = '123postgis'
    host = 'localhost'  # Cambia esto si tu base de datos está en otro host
    port = '5432'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._connection = None
        return cls._instance
    
    

    def connect(self):
        """
        Connect to the database using the provided credentials.
        """
        try:
            self._connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            print(f"connect to database")
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            
            
            

    def execute(self, query, params=None):
        """
        Execute a SQL query on the database.
        """
        if self._connection is None:
            print("Error: database connection not established")
            return None
        try:
            cursor = self._connection.cursor()
            cursor.execute(query, params)
        except Exception as e:
            print("Error execute ",e)
            

        return cursor

    def disconnect(self):
        """
        Close the connection to the database.
        """
        if self._connection is not None:
            self._connection.close()
            self._connection = None
            
    def commit(self):
        # Confirmar la transacción
        if self._connection is not None:
            self._connection.commit()
        
