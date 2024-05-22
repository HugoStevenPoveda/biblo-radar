import sys
sys.path.append(r'src/app_biblio/')
from fastapi import APIRouter
from services.BilbiotecaService import BibliotecaService


biblioteca = APIRouter()
biblioteca_service = BibliotecaService()


@biblioteca.get('/bibliotecas')
async def get_bibliotecas():
    return biblioteca_service.get_bibliotecas()


@biblioteca.get('/bibliotecas/{id_libro}')
async def get_bibliotecas(id_libro):
    return biblioteca_service.get_bibliotecas_by_id_libro(id_libro)
