from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db


# criar - CREATE
def criar_aluno(aluno: schemas.Aluno, db: Session = Depends(get_db)):
    try:
        db_aluno = models.AlunoModel(nome=aluno.nome, email=aluno.email)
        db.add(db_aluno)
        db.commit()
        db.refresh(db_aluno)
        return db_aluno
    except Exception as e:
        print(f"Erro ao criar aluno: {e}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


# ler - READ - geral
def listar_email_aluno(email: str, db: Session):
    return db.query(models.AlunoModel).filter(models.AlunoModel.email == email).first()


def listar_alunos(db: Session = Depends(get_db)):
    return db.query(models.AlunoModel).all()


# ler - READ - por id
def listar_id_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.AlunoModel).filter(models.AlunoModel.id == id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno


# atualizar - UPDATE
def atualizar_aluno(id: int, aluno_atualizado: schemas.AlunoUpdate,
                    db: Session = Depends(get_db)):
    aluno = db.query(models.AlunoModel).filter(models.AlunoModel.id == id).first()
    if aluno is None:
        return None

    if aluno_atualizado.nome is not None:
        aluno.nome = aluno_atualizado.nome
    if aluno_atualizado.email is not None:
        aluno.email = aluno_atualizado.email

    db.commit()
    db.refresh(aluno)
    return aluno


# remover - DELETE
def deletar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.AlunoModel).filter(models.AlunoModel.id == id).first()
    if aluno is None:
        return None

    db.delete(aluno)
    db.commit()
    return aluno
