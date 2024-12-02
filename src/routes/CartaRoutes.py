from fastapi import APIRouter, HTTPException
from typing import Optional, List
from models.Carta import Carta
from services.CartaService import verificar_carta_existe, adicionar_carta, filtrar_cartas

router = APIRouter()

@router.post("/")
def criar_carta(carta: Carta):
    if verificar_carta_existe(carta.id):
        raise HTTPException(status_code=400, detail="Uma carta com este ID já existe.")
    
    adicionar_carta(carta)
    return {"message": "Carta adicionada com sucesso!"}

@router.get("/filtrar/", response_model=List[Carta])
def listar_cartas_filtradas(tipo: Optional[str] = None, cor: Optional[str] = None, rarity: Optional[str] = None):
    return filtrar_cartas(tipo, cor, rarity)