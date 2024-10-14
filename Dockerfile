FROM python:3.12-alpine3.20

RUN apk update && \
    apk add --no-cache \
    gcc \
    libpq-dev \
    linux-headers \
    musl-dev \
    postgresql && \
    rm -rf /var/cache/apk/* && \
    adduser -D appuser

WORKDIR /app

RUN pip install poetry \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

USER appuser

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD ["wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:8080/health"]

CMD [ "poetry", "run", "uvicorn", "arquivos_py.main:app", "--host", "0.0.0.0", "--port", "8000" ]
