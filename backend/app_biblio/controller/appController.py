from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .BibliotecaRouter import biblioteca
from .LibroRouter import libro

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Headers permitidos
)

app.include_router(biblioteca)
app.include_router(libro)

