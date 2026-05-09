from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..services.analytics import avaliar_produtividade

router = APIRouter()


@router.get("/", response_model=schemas.DiagnosticoProdutividade, summary="Obter diagnóstico geral de produtividade")
def diagnostico_produtividade(db: Session = Depends(get_db)):
    registros = db.query(models.RegistroFoco).order_by(models.RegistroFoco.criado_em.desc()).limit(50).all()
    return avaliar_produtividade(registros)


