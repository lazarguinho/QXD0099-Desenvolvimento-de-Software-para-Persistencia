from fastapi import APIRouter, HTTPException
from models.Carta import Carta
from services.CartaService import verificar_carta_existe, adicionar_carta

router = APIRouter()

@router.post("/")
def criar_carta(carta: Carta):
    if verificar_carta_existe(carta.id):
        raise HTTPException(status_code=400, detail="Uma carta com este ID já existe.")
    
    adicionar_carta(carta)
    return {"message": "Carta adicionada com sucesso!"}
