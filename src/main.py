from fastapi import FastAPI
from routes.CartaRoutes import router as CartaRoutes

app = FastAPI()

app.include_router(CartaRoutes, prefix="/cartas", tags=["Cartas"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Cartas de Magic: The Gathering!"}
