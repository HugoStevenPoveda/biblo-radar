import sys
sys.path.append(r'src/app_biblio/')
from services.BilbiotecaService import BibliotecaService
from fastapi import FastAPI

app = FastAPI()


biblioteca_service = BibliotecaService()


# Definir las rutas de tu servicio FastAPI
@app.get("/bibliotecas/")
async def get_bibliotecas():
    return biblioteca_service.get_bibliotecas()






