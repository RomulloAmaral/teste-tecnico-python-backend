from typing import List
from ..models import RegistroFoco



def avaliar_produtividade(registros: List[RegistroFoco]) -> dict:
    if not registros:
        return {
            "nivel_produtividade": "Sem dados",
            "diagnostico": "Não há registros suficientes para análise.",
            "metricas": {
                "total_registros": 0,
                "tempo_total_minutos": 0,
                "nivel_foco_medio": 0.0,
                "quantidade_distracao_media": 0.0,
            },
            "recomendacoes": ["Comece registrando suas sessões de foco."]
        }

    # Calcular métricas
    total_registros = len(registros)
    tempo_total = sum(r.tempo_minutos for r in registros)
    nivel_foco_medio = sum(r.nivel_foco for r in registros) / total_registros
    quantidade_distracao_media = sum(r.quantidade_distracao or 0 for r in registros) / total_registros

    # Análise de produtividade
    if nivel_foco_medio >= 4 and quantidade_distracao_media <= 2:
        nivel = "Excelente"
        diagnostico = f"Produtividade excepcional! Média de {nivel_foco_medio:.1f} no nível de foco."
        recomendacoes = [
            "Continue com suas práticas atuais",
            "Considere compartilhar suas técnicas com colegas"
        ]
    elif nivel_foco_medio >= 3 and quantidade_distracao_media <= 4:
        nivel = "Boa"
        diagnostico = f"Produtividade sólida. Média de {nivel_foco_medio:.1f} no nível de foco."
        recomendacoes = [
            "Mantenha o ritmo atual",
            "Identifique padrões de distração para otimizar ainda mais"
        ]
    elif nivel_foco_medio >= 2:
        nivel = "Regular"
        diagnostico = f"Produtividade regular. Há espaço para melhorias."
        recomendacoes = [
            "Implemente técnicas de gerenciamento de distrações",
            "Considere pausas mais estruturadas",
            "Avalie seus horários de trabalho"
        ]
    else:
        nivel = "Baixa"
        diagnostico = f"Produtividade abaixo do esperado. Média de {nivel_foco_medio:.1f} no nível de foco."
        recomendacoes = [
            "Revise suas técnicas de foco",
            "Identifique e minimize fontes de distração",
            "Considere sessões mais curtas e frequentes"
        ]

    return {
        "nivel_produtividade": nivel,
        "diagnostico": diagnostico,
        "metricas": {
            "total_registros": total_registros,
            "tempo_total_minutos": tempo_total,
            "nivel_foco_medio": round(nivel_foco_medio, 1),
            "quantidade_distracao_media": round(quantidade_distracao_media, 1)
        },
        "recomendacoes": recomendacoes
    }
