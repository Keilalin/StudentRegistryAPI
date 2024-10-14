FROM python:3.12-alpine3.20@cb3ba1d3ac8b90cb85a4fe2a0e26a42af542f64ea86598d0409bc35493c4e561229f8d3142a23013c98b1a037495a8bf123ff977066230ab36a3a13dc92da9c4

RUN apk update && \
    apk add --no-cache \
    gcc \
    linux-headers \
    libpq-dev \
    musl-dev \
    postgresql \
    && rm -rf /var/cache/apk/* \
    adduser -D appuser

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

USER appuser

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD ["wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:8080/health"]

CMD [ "poetry", "run", "uvicorn", "arquivos_py.main:app", "--host", "0.0.0.0", "--port", "8000" ]
