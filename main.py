from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tarefas = []

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False 

@app.get("/")
def inicio():
    return {"mensagem": "API de tarefas funcionando"}

@app.get("/tarefas")
def listar_tarefas():
    return {"tarefas": tarefas}

@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return{"mensagem": "Tarefa criada","tarefa":tarefa}
    
@app.put("/tarefas/{indice}")
def atualizar_tarefa(indice: int, tarefa: Tarefa):
    if indice < 0 or indice >= len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefas[indice] = tarefa
    return {"mensagem": "Tarefa atualizada", "tarefa": tarefa}

@app.delete("/tarefas/{indice}")
def deletar_tarefa(indice: int):
    if indice < 0 or indice >= len(tarefas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa = tarefas.pop(indice)
    return {"mensagem": "Tarefa deletada", "tarefa": tarefa}