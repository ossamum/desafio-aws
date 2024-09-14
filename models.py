from sqlalchemy import Column, Integer, String
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    idade = Column(Integer)
    nota_primeiro_semestre = Column(Integer)
    nota_segundo_semestre = Column(Integer)
    nome_professor = Column(String(255))
    numero_sala = Column(Integer)
