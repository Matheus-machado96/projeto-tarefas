#API de tarefas

API REST desenvolvida com Fast API e Python para gerenciamento de tarefas

## Tecnologias
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Funcionalidades
- Criar tarefa
- Listar tarefas
- Atualizar tarefa
- Deletar tarefa

## Como rodar

```bash
# ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install fastapi uvicorn sqlalchemy

# Rodar a API
python3 -m uvicorn main:app --reload