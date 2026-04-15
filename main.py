from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TarefaSchema(BaseModel):
    titulo: str
    concluida: bool = False 

@app.get("/")
def inicio():
    return {"mensagem": "API de tarefas funcionando"}

@app.get("/tarefas")
def listar_tarefas(db: Session = Depends(get_db)):
    tarefas = db.query(models.Tarefa).all()
    return {"tarefas": tarefas}

@app.post("/tarefas")
def criar_tarefa(tarefa: TarefaSchema, db: Session = Depends(get_db)):
    nova_tarefa = models.Tarefa(titulo=tarefa.titulo, concluida=tarefa.concluida)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return {"mensagem": "Tarefa criada", "tarefa": nova_tarefa}

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: TarefaSchema, db: Session = Depends(get_db)):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db_tarefa.titulo = tarefa.titulo
    db_tarefa.concluida = tarefa.concluida
    db.commit()
    db.refresh(db_tarefa)
    return {"mensagem": "Tarefa atualizada", "tarefa": db_tarefa}

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(db_tarefa)
    db.commit()
    return {"mensagem": "Tarefa deletada"}