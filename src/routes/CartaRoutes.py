from fastapi import APIRouter, HTTPException
from typing import Optional, List
from src.models.Carta import Carta
from src.services.CartaService import verificar_carta_existe, adicionar_carta, filtrar_cartas, calcular_hash_csv, ler_dados_csv
from src.utils.logging_config import logger

router = APIRouter()

@router.post("/")
def criar_carta(carta: Carta):
    if verificar_carta_existe(carta.id):
        logger.error(f"Ao tentar adicionar um carta com id {carta.id} ja existente.")
        raise HTTPException(status_code=400, detail="Uma carta com este ID já existe.")
    
    adicionar_carta(carta)
    logger.info(
        f"Carta inserida com sucesso: id={carta.id}, nome={carta.nome}, tipo={carta.tipo}, "
        f"custo={carta.custo}, cor={carta.cor}, rarity={carta.rarity}, habilidade={carta.habilidade}"
    )
    return {"message": "Carta adicionada com sucesso!"}

@router.get("/filtrar/", response_model=List[Carta])
def listar_cartas_filtradas(tipo: Optional[str] = None, cor: Optional[str] = None, rarity: Optional[str] = None):
    logger.info(f"Listando cartas filtradas: tipo={tipo}, cor={cor}, rarity={rarity}")
    return filtrar_cartas(tipo, cor, rarity)

@router.get("/hash/")
def calcular_hash():
    try:
        logger.info("Hash SHA256 do arquivo CSV calculado.")
        return {"hash": calcular_hash_csv()}
    except Exception as e:
        logger.error(f"Erro ao calcular o hash SHA256: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/all", response_model=List[Carta])
def listar_todas_cartas():
    return ler_dados_csv()


    