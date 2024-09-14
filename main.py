from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.post("/usuarios", response_model=schemas.Aluno, status_code=status.HTTP_201_CREATED)
def create_aluno(aluno: schemas.AlunoCreate, session: Session = Depends(get_session)):

    # create an instance of the aluno database model
    alunodb = models.Aluno(
        nome = aluno.nome,
        idade = aluno.idade,
        nota_primeiro_semestre = aluno.nota_primeiro_semestre,
        nota_segundo_semestre = aluno.nota_segundo_semestre,
        nome_professor = aluno.nome_professor,
        numero_sala = aluno.numero_sala,
    )

    # add it to the session and commit it
    session.add(alunodb)
    session.commit()
    session.refresh(alunodb)

    # return the aluno object
    return alunodb

@app.get("/usuarios/{id}", response_model=schemas.Aluno)
def read_aluno(id: int, session: Session = Depends(get_session)):

    # get the aluno item with the given id
    aluno = session.query(models.Aluno).get(id)

    # check if aluno item with given id exists. If not, raise exception and return 404 not found response
    if not aluno:
        raise HTTPException(status_code=404, detail=f"aluno item with id {id} not found")

    return aluno

@app.put("/usuarios/{id}", response_model=schemas.Aluno)
def update_aluno(
    id: int,
    nome = str,
    idade = int,
    nota_primeiro_semestre = int,
    nota_segundo_semestre = int,
    nome_professor = str,
    numero_sala = int,
    session: Session = Depends(get_session)
):

    # get the aluno item with the given id
    aluno = session.query(models.Aluno).get(id)

    # update aluno item with the given task (if an item with the given id was found)
    if aluno:
        aluno.nome = nome
        aluno.idade = idade
        aluno.nota_primeiro_semestre = nota_primeiro_semestre
        aluno.nota_segundo_semestre = nota_segundo_semestre
        aluno.nome_professor = nome_professor
        aluno.numero_sala = numero_sala
        session.commit()

    # check if aluno item with given id exists. If not, raise exception and return 404 not found response
    if not aluno:
        raise HTTPException(status_code=404, detail=f"aluno item with id {id} not found")

    return aluno

@app.delete("/usuarios/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_aluno(id: int, session: Session = Depends(get_session)):

    # get the aluno item with the given id
    aluno = session.query(models.Aluno).get(id)

    # if aluno item with given id exists, delete it from the database. Otherwise raise 404 error
    if aluno:
        session.delete(aluno)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"aluno item with id {id} not found")

    return None

@app.get("/usuarios", response_model = List[schemas.Aluno])
def read_aluno_list(session: Session = Depends(get_session)):

    # get all aluno items
    aluno_list = session.query(models.Aluno).all()

    return aluno_list
