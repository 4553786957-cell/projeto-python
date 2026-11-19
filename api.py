from fastapi import FastAPI
import uvicorn
from routes.estado_routes import router as estado_router

app = FastAPI(
    title="API de Endereços - CRUD de Estados",
    description= "API REST desenvolvida com FastAPI e MySQL para gerenciamento de Estados.",
    version="1.0.0",
)

app.include_router(estado_router)

@app.get("/", tags=["Status"])
def raiz():
    return {
        "mensagem": "API de Estados em execução!",
        "documentação": "Acesse /docs para visualizar o Swagger UI",
    }

if __name__=="__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)