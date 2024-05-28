from pydantic import BaseModel
from typing import Optional


class Libro(BaseModel):
    id: Optional[str]
    autor: str
    titulo: str
    descripcion: str
    genero: str
    fecha_publicacion: str
    version_digital: str


class LibroBuilder:
    def __init__(self):
        self.id = None
        self.autor = None
        self.titulo = None
        self.descripcion = None
        self.genero = None
        self.fecha_publicacion = None
        self.version_digital = None

    def set_id(self, id: str) -> 'LibroBuilder':
        self.id = id
        return self

    def set_autor(self, autor: str) -> 'LibroBuilder':
        self.autor = autor
        return self

    def set_titulo(self, titulo: str) -> 'LibroBuilder':
        self.titulo = titulo
        return self

    def set_descripcion(self, descripcion: str) -> 'LibroBuilder':
        self.descripcion = descripcion
        return self

    def set_genero(self, genero: str) -> 'LibroBuilder':
        self.genero = genero
        return self

    def set_fecha_publicacion(self, fecha_publicacion: str) -> 'LibroBuilder':
        self.fecha_publicacion = fecha_publicacion
        return self

    def set_version_digital(self, version_digital: str) -> 'LibroBuilder':
        self.version_digital = version_digital
        return self

    def build(self) -> 'Libro':
        return Libro(**self.__dict__)
