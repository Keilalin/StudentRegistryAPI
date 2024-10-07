from sqlalchemy import Column, Integer, String

from .database import Base


# Cria a tabela Alunos
class AlunoModel(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
