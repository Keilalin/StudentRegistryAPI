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

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1
