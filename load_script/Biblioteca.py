from pydantic import BaseModel
from typing import Optional

class Biblioteca(BaseModel):
    nombre: str
    direccion: str
    telefono: Optional[str]
    email: str
    pagina_web: str
    estado: str
    nodo: str
    clasificacion: str
    point_x: float
    point_y: float

class BibliotecaBuilder:
    def __init__(self):
        self.nombre = None
        self.direccion = None
        self.telefono = None
        self.email = None
        self.pagina_web = None
        self.estado = None
        self.nodo = None
        self.clasificacion = None
        self.point_x = None
        self.point_y = None

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_direccion(self, direccion):
        self.direccion = direccion
        return self

    def set_telefono(self, telefono):
        self.telefono = telefono
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_pagina_web(self, pagina_web):
        self.pagina_web = pagina_web
        return self

    def set_estado(self, estado):
        self.estado = estado
        return self

    def set_nodo(self, nodo):
        self.nodo = nodo
        return self

    def set_clasificacion(self, clasificacion):
        self.clasificacion = clasificacion
        return self

    def set_point_x(self, point_x):
        self.point_x = point_x
        return self

    def set_point_y(self, point_y):
        self.point_y = point_y
        return self

    def build(self):
        return Biblioteca(
            nombre=self.nombre,
            direccion=self.direccion,
            telefono=self.telefono,
            email=self.email,
            pagina_web=self.pagina_web,
            estado=self.estado,
            nodo=self.nodo,
            clasificacion=self.clasificacion,
            point_x=self.point_x,
            point_y=self.point_y
        )


