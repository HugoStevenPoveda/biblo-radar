
import sys
sys.path.append(r'app_biblio/')
from services.BilbiotecaService import BibliotecaService
from fastapi import APIRouter


biblioteca = APIRouter()
biblioteca_service = BibliotecaService()


@biblioteca.get('/bibliotecas')
async def get_bibliotecas():
    return biblioteca_service.get_bibliotecas()


@biblioteca.get('/bibliotecas/{id_libro}')
async def get_bibliotecas(id_libro):
    return biblioteca_service.get_bibliotecas_by_id_libro(id_libro)


@biblioteca.get('/bibliotecas/{id_libro}/{longitud}/{latitud}')
async def get_bibliotecas(id_libro, longitud, latitud):
    return biblioteca_service.get_bibliotecas_by_id_libro_coordenada(id_libro, longitud, latitud)
