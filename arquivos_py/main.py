from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import Base, SessionLocal, engine
from sqlalchemy import Column, Integer, String
from typing import Optional

app = FastAPI()

# Cria a tabela Alunos
class AlunoModel(Base):
    __tablename__ = 'ALUNOS'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    nome = Column(String, index=True) 
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

# Cria o Schema Aluno
class Aluno(BaseModel):
    id: int | None = None
    nome: str
    email: EmailStr

    class Config:
        from_attributes = True

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True

# Acessa o Banco de Dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# criar - CREATE
@app.post('/alunos/', response_model = Aluno)
def criar_aluno(aluno: Aluno, db: Session = Depends(get_db)):
    try:
        db_aluno = AlunoModel(nome = aluno.nome, email = aluno.email)
        db.add(db_aluno)
        db.commit()
        db.refresh(db_aluno)
        return db_aluno
    except Exception as e:
        print(f"Erro ao criar aluno: {e}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# ler - READ - geral
@app.get('/alunos/', response_model=list[Aluno])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(AlunoModel).all()

# ler - READ - por id
@app.get("/alunos/{id}", response_model=Aluno)
def id_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id == id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# atualizar - UPDATE
@app.put("/alunos/{id}", response_model=Aluno)
def atualizar_aluno(id: int, aluno_atualizado: AlunoUpdate, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id == id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    if aluno_atualizado.nome is not None:
        aluno.nome = aluno_atualizado.nome
    if aluno_atualizado.email is not None:
        aluno.email = aluno_atualizado.email

    db.commit()
    db.refresh(aluno)
    return aluno

# remover - DELETE
@app.delete("/alunos/{id}", response_model=Aluno)
def deletar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id == id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    db.delete(aluno)
    db.commit()
    return aluno