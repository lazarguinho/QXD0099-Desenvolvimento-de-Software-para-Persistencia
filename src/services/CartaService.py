import csv
import os
from models.Carta import Carta

CSV_FILE_PATH = "data/cartas.csv"

if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "nome", "tipo", "custo", "cor", "rarity", "habilidade"])

def verificar_carta_existe(carta_id: int) -> bool:
    with open(CSV_FILE_PATH, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["id"]) == carta_id:
                return True
    return False

def adicionar_carta(carta: Carta):
    with open(CSV_FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([carta.id, carta.nome, carta.tipo, carta.custo, carta.cor, carta.rarity, carta.habilidade])
