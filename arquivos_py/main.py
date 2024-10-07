from fastapi import FastAPI

from .database import Base, engine
from .routers import alunos

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(alunos.router)


# healthcheck
@app.get("/health")
def health_check():
    return {"status": "healthy"}
