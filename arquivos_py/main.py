import os
import time
from fastapi import FastAPI

from .database import Base, engine, create_engine
from .routers import alunos

app = FastAPI()


db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

if db_url is None:
    print("Erro: A variável de ambiente SQLALCHEMY_DATABASE_URL não está definida.")
    exit(1)


max_attempts = 5
attempts = 0

while attempts < max_attempts:
    try:
        engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"), pool_pre_ping=True)
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        break
    except Exception as e:
        max_attempts += 1
        print("Tentando conectar ao banco de dados...")
        time.sleep(5)
if attempts == max_attempts:
    print("Falha ao conectar ao banco de dados após várias tentativas. Encerrando o aplicativo.")
    exit(1)

Base.metadata.create_all(bind=engine)

app.include_router(alunos.router)


# healthcheck
@app.get("/health")
def health_check():
    return {"status": "healthy"}
