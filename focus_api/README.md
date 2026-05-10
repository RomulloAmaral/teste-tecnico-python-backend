# Focus API

API desenvolvida em FastAPI para registrar sessões de foco e gerar diagnósticos inteligentes de produtividade.

---

# Objetivo

O projeto foi desenvolvido como solução para o desafio técnico de criação de uma API de produtividade, permitindo registrar sessões de foco e gerar análises automáticas com base nos dados salvos.

---

# Tecnologias e bibliotecas utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite

---

# Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/RomulloAmaral/teste-tecnico-python-backend.git
```

## 2. Acesse a pasta do projeto

```bash
cd teste-tecnico-python-backend
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Execute o projeto

```bash
uvicorn focus_api.app.main:app --reload
```

---

# Acessar a documentação da API

Após executar o projeto, acesse:

```bash
http://127.0.0.1:8000/docs
```

A documentação Swagger será aberta contendo todas as rotas da API.

---

# Como utilizar a API

## Registrar foco

Endpoint:

```bash
POST /registro_foco/
```

### Passos:
1. Clique em `Try it out`
2. Preencha o JSON
3. Clique em `Execute`

### Exemplo:

```json
{
  "nivel_foco": 5,
  "tempo_minutos": 120,
  "comentarios": "Desenvolvimento da API",
  "category": "coding",
  "quantidade_distracao": 1,
  "principal_distracao": "Celular"
}
```

---

## Gerar diagnóstico de produtividade

Endpoint:

```bash
GET /diagnostico-produtividade/
```

### Passos:
1. Clique em `Try it out`
2. Clique em `Execute`

A API retornará:
- média de foco
- tempo total focado
- nível de produtividade
- recomendações inteligentes

---

## Limpar registros

Endpoint:

```bash
DELETE /registro_foco/limpar
```

### Passos:
1. Clique em `Try it out`
2. Clique em `Execute`

Todos os registros serão removidos do banco de dados.

---

# Melhorias implementadas

Além dos requisitos do desafio técnico, foram adicionadas as seguintes melhorias:

- Campo `quantidade_distracao`
- Campo `principal_distracao`
- Rota para limpar registros
- Tratamento de erros com mensagens em português
- Diagnóstico inteligente baseado nos registros
- Recomendações automáticas de produtividade

---

# Estrutura do projeto

```bash
focus_api/
│
├── app/
│   ├── routers/
│   ├── services/
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── main.py
│
├── focus_api.db
├── requirements.txt
└── README.md
```

---

# Artefatos gerados

Durante o desenvolvimento, utilizei IA principalmente para:

- `focus_api.db`: banco de dados SQLite com registros de foco e diagnósticos
- `requirements.txt`: dependências necessárias para rodar a API
- código da aplicação em `app/` com rotas, modelos, schemas e serviços
- `README.md`: documentação de uso e endpoints

---

# Autor

Rômullo Amaral