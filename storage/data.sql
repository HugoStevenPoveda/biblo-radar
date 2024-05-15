DO $$
BEGIN

    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'bibliotecas_inf') THEN
        CREATE TABLE bibliotecas_inf (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255),
            direccion VARCHAR(255),
            telefono VARCHAR(20),
            email VARCHAR(255),
            pagina_web VARCHAR(255),
            estado VARCHAR(20),
            nodo VARCHAR(255),
            clasificacion VARCHAR(255),
            longitud VARCHAR(255),--en eje x
            latitud VARCHAR(255),--en eje y 
            geom GEOMETRY(Point, 3857)  -- Columna para almacenar la geometría
        );
    END IF;
    
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'libros') THEN
        CREATE TABLE libros (
            id VARCHAR(50) PRIMARY KEY,
            autor VARCHAR(1200) NOT NULL,
            titulo VARCHAR(1200) NOT NULL,
            descripcion TEXT,
            genero VARCHAR(100),
            fecha_publicacion VARCHAR(250),
            version_digital VARCHAR(1200)
        );
    END IF;
    
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'biblioteca_libro') THEN
        CREATE TABLE biblioteca_libro (
            id SERIAL PRIMARY KEY,
            biblioteca_id INT REFERENCES bibliotecas_inf(id),
            libro_id VARCHAR(50) REFERENCES libros(id),
            UNIQUE(biblioteca_id, libro_id)  -- Garantiza que no haya duplicados de la relación
        );
    END IF;
END $$;
