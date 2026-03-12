from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Anuncio(BaseModel):
    texto: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

anuncios = []

@app.get("/anuncios")
def obtener_anuncios():
    return anuncios

@app.post("/anuncios")
def agregar_anuncio(anuncio: Anuncio):
    anuncios.append({"texto": anuncio.texto})
    return anuncios
