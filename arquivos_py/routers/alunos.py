from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter()


# criar - CREATE
@router.post('/alunos/', response_model=schemas.Aluno)
def criar_aluno(aluno: schemas.Aluno, db: Session = Depends(get_db)):
    aluno_existente = crud.listar_email_aluno(aluno.email, db)
    if aluno_existente:
        raise HTTPException(status_code=404, detail="Email já cadastrado!")
    return crud.criar_aluno(db=db, aluno=aluno)


# ler - READ - geral
@router.get('/alunos/', response_model=list[schemas.Aluno])
def listar_alunos(db: Session = Depends(get_db)):
    alunos = crud.listar_alunos(db)
    if not alunos:
        raise HTTPException(status_code=404, detail="Nenhum aluno encontrado!")
    return alunos


# ler - READ - por id
@router.get("/alunos/{id}", response_model=schemas.Aluno)
def id_aluno(id: int, db: Session = Depends(get_db)):
    aluno = crud.listar_id_aluno(db, id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno


# atualizar - UPDATE
@router.put("/alunos/{id}", response_model=schemas.Aluno)
def atualizar_aluno(id: int, aluno_atualizado: schemas.AlunoUpdate,
                    db: Session = Depends(get_db)):
    aluno = crud.atualizar_aluno(db, id, aluno_atualizado)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return aluno


# remover - DELETE
@router.delete("/alunos/{id}", response_model=schemas.Aluno)
def deletar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = crud.deletar_aluno(id, db)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return aluno
