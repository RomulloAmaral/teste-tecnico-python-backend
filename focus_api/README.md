# Focus API

Projeto FastAPI para gerenciar registros de foco e gerar diagnósticos simples.

## Como executar

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints principais

- `GET /` - status da API
- `POST /registros/` - criar um registro
- `GET /registros/` - listar registros
- `GET /registros/{id}` - obter registro por ID
- `POST /diagnostico/` - criar diagnóstico com base em um registro existente
- `GET /diagnostico/{id}` - obter diagnóstico por ID
