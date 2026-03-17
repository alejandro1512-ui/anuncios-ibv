from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Anuncio(BaseModel):
    texto: str

@app.get("/anuncios")
def obtener_anuncios():
    respuesta = supabase.table("anuncios").select("*").execute()
    return respuesta.data

@app.post("/anuncios")
def agregar_anuncio(anuncio: Anuncio):
    respuesta = supabase.table("anuncios").insert({"texto": anuncio.texto}).execute()
    return respuesta.data