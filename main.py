from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db
from typing import List

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rota para criar um novo aluno
@app.post("/usuarios/", response_model=schemas.Aluno)
def create_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = models.Aluno(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

# Rota para ler a lista de todos os alunos
@app.get("/usuarios/all", response_model=List[schemas.Aluno])
def read_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    alunos = db.query(models.Aluno).offset(skip).limit(limit).all()
    return alunos

# Rota para ler um aluno por ID
@app.get("/usuarios/{id}", response_model=schemas.Aluno)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# Rota para atualizar as informações de um aluno
@app.put("/usuarios/{id}", response_model=schemas.Aluno)
def update_aluno(aluno_id: int, aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    for var, value in vars(aluno).items():
        setattr(db_aluno, var, value) if value else None
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

# Rota para deletar um aluno
@app.delete("/usuarios/{id}", response_model=schemas.Aluno)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if db_aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(db_aluno)
    db.commit()
    return db_aluno
