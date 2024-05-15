import sys
sys.path.append(r'src/app_biblio/')
from services.DatabaseConnection import DatabaseConnection

db_connection = DatabaseConnection()
db_connection.connect()
query = '''
DO $$
DECLARE
    v_biblioteca_id INT;
    v_libro_id VARCHAR(50);
    total_bibliotecas INT;
    total_libros INT;
    total_registros INT := 0;
BEGIN
    -- Obtener el número total de bibliotecas y libros
    SELECT COUNT(*) INTO total_bibliotecas FROM bibliotecas_inf;
    SELECT COUNT(*) INTO total_libros FROM libros;

    -- Determinar el número total de registros necesario
    total_registros := total_bibliotecas * 3000;

    -- Eliminar todos los registros actuales de biblioteca_libro
    DELETE FROM biblioteca_libro;

    -- Insertar registros aleatorios
    FOR i IN 1..total_registros LOOP
        -- Seleccionar un id de biblioteca aleatorio
        v_biblioteca_id := (SELECT id FROM bibliotecas_inf ORDER BY RANDOM() LIMIT 1);
        -- Seleccionar un id de libro aleatorio
        v_libro_id := (SELECT id FROM libros ORDER BY RANDOM() LIMIT 1);
        -- Insertar el par (biblioteca_id, libro_id) en biblioteca_libro si no existe
        INSERT INTO biblioteca_libro (biblioteca_id, libro_id)
        VALUES (v_biblioteca_id, v_libro_id)
        ON CONFLICT DO NOTHING;
    END LOOP;
END $$;

'''

cursor =db_connection.execute(query)
db_connection.commit()
cursor.close()
db_connection.disconnect()
