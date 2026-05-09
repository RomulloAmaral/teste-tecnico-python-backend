from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from .database import Base


class RegistroFoco(Base):
    __tablename__ = "registros_foco"

    id = Column(Integer, primary_key=True, index=True)
    nivel_foco = Column(Integer, nullable=False)
    tempo_minutos = Column(Integer, nullable=False)
    comentarios = Column(Text, nullable=False)
    category = Column(String, nullable=True)
    quantidade_distracao = Column(Integer, nullable=True)
    principal_distracao = Column(String, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
