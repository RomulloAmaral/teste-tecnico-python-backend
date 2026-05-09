from pydantic import BaseModel, Field, conint
from datetime import datetime
from typing import Optional, Literal, List


class RegistroFocoBase(BaseModel):
    nivel_foco: conint(ge=1, le=5) = Field(
        ..., description="Nível de foco entre 1 (muito distraído) e 5 (estado de flow)"
    )
    tempo_minutos: conint(gt=0) = Field(
        ..., description="Tempo de foco em minutos, deve ser maior que zero"
    )
    comentarios: str = Field(..., min_length=1, max_length=500)
    category: Optional[Literal["coding", "estudando", "reunião"]] = None
    quantidade_distracao: conint(ge=0) = Field(
        None,
        description="Quantidade de distrações deve ser maior ou igual a 0",
    )
    principal_distracao: Optional[str] = None    

class RegistroFocoCreate(RegistroFocoBase):
    pass


class RegistroFoco(RegistroFocoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class DiagnosticoBase(BaseModel):
    registro_id: int
    nivel: str
    recomendacao: str


class DiagnosticoCreate(DiagnosticoBase):
    pass


class Diagnostico(DiagnosticoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class MetricasProdutividade(BaseModel):
    total_registros: int
    tempo_total_minutos: int
    nivel_foco_medio: float
    quantidade_distracao_media: float


class DiagnosticoProdutividade(BaseModel):
    nivel_produtividade: str
    diagnostico: str
    metricas: MetricasProdutividade
    recomendacoes: List[str]