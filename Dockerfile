FROM python:3.12-alpine3.20

RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    libpq-dev \
    postgresql && \
    rm -rf /var/cache/apk/*

RUN adduser -D appuser

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

USER appuser

HEALTHCHECK --interval=5m --timeout=3s CMD ["poetry", "run", "uvicorn", "arquivos_py.main:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["poetry", "run", "uvicorn", "arquivos_py.main:app", "--host", "0.0.0.0", "--port", "8000"]
