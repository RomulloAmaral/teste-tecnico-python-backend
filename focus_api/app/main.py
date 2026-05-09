from fastapi import FastAPI
from .routers import registro, diagnostico
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Focus API",
    description="API de registro e diagnóstico de foco",
    version="0.1.0",
)

app.include_router(registro.router, prefix="/registro_foco", tags=["Registros"])
app.include_router(diagnostico.router, prefix="/diagnostico-produtividade", tags=["Diagnóstico"])

@app.get("/", summary="Status da API")
def root():
    return {"message": "Focus API está em execução"}
