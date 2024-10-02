FROM python:3.12-alpine3.20

# Atualiza e instala as dependências do sistema
RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    libpq-dev \
    postgresql && \
    rm -rf /var/cache/apk/*

RUN adduser -D appuser

# Define o diretório de trabalho
WORKDIR /app

# Instala o Poetry
RUN pip install poetry

RUN poetry config virtualenvs.create false

# Copia os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock* /app/

# Instala as dependências
RUN poetry install --no-root

# Copia o restante da aplicação
COPY . /app

USER appuser

# Comando de verificação de saúde
HEALTHCHECK --interval=5m --timeout=3s CMD ["poetry", "run", "uvicorn", "arquivos_py.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Comando padrão ao rodar o contêiner
CMD ["poetry", "run", "uvicorn", "arquivos_py.main:app", "--host", "0.0.0.0", "--port", "8000"]
