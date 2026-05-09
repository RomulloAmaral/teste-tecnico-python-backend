from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.RegistroFoco, summary="Criar um registro de foco")
def criar_registro_foco(registro: schemas.RegistroFocoCreate, db: Session = Depends(get_db)):
    novo = models.RegistroFoco(
        nivel_foco=registro.nivel_foco,
        tempo_minutos=registro.tempo_minutos,
        comentarios=registro.comentarios,
        category=registro.category,
        quantidade_distracao=registro.quantidade_distracao,
        principal_distracao=registro.principal_distracao,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

