from pydantic import BaseModel

class AlunoCreate(BaseModel):
    nome: str
    idade: int
    nota_primeiro_semestre: int
    nota_segundo_semestre: int
    nome_professor: str
    numero_sala: int

class Aluno(BaseModel):
    id: int
    nome: str
    idade: int
    nota_primeiro_semestre: int
    nota_segundo_semestre: int
    nome_professor: str
    numero_sala: int

    class Config:
        orm_mode = True
