from typing import Optional

from pydantic import BaseModel, EmailStr


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
