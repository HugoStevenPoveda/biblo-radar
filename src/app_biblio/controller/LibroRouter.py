import sys
sys.path.append(r'src/app_biblio/')
from services.LibroService import LibroService
from fastapi import APIRouter

libro = APIRouter()
libro_service = LibroService()


@libro.get("/libro/{title}")
def get_libro_by_title(title):
    return libro_service.get_libro_by_title(title)
