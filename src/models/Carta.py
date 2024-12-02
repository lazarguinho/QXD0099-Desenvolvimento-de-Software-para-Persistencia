from pydantic import BaseModel

class Carta(BaseModel):
    id: int
    nome: str
    tipo: str
    custo: int
    cor: str
    rarity: str
    habilidade: str
