<h1 align="center"> StudentRegistryAPI </h1>
Esta API permite gerenciar informações de alunos por meio das operações básicas de CRUD (Create, Read, Update, Delete), rodando em Docker.
Integrando Docker, FastAPI e PostgreSQL através do SQLAlchemy, o projeto foi desenvolvido em Python.
<br></br>

Índice
=================
<!--ts-->
   * 📋 [Pré Requisitos](#pre-requisitos)
   * 🚀 [Rodando a API](#-rodando-a-api-com-fastapi)
        * ⚙️ [Operações CRUD](#operações-crud)
        * ✅ [Teste da API](#teste-da-api)
        * 🛡️ [Segurança](#segurança)
   * 🌐 [Tecnologias](#tecnologias)
<!--te-->

### 📋Pré-requisitos

Antes de executar o projeto, certifique-se de que você tenha instalado os seguintes softwares e bibliotecas:

1. [**Python 3.12 ou superior**](https://www.python.org/): O projeto é desenvolvido em Python, então você precisará ter uma versão compatível instalada.
2. [**PostgreSQL**](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads): Um banco de dados PostgreSQL deve estar instalado e em execução em sua máquina ou acessível via rede.
3. [**Rancher Desktop**](https://rancherdesktop.io/): Para utilizar o Rancher Desktop, é necessário que o Rancher esteja instalado e em execução em sua máquina, pois ele já fornece suporte integrado para gerenciamento de containers Docker.
4. **Variáveis de ambiente**: As seguintes variáveis de ambiente devem ser configuradas no seu arquivo `.env`:
   - `DB_USERNAME`: Nome de usuário do banco de dados.
   - `DB_PASSWORD`: Senha do banco de dados.
   - `DB_HOST`: Endereço do servidor do banco de dados (ex: `localhost`).
   - `DB_PORT`: Porta do servidor do banco de dados (ex: `5432`).
   - `DB_NAME`: Nome do banco de dados que será utilizado.
   - `PGADMIN_EMAIL`: Email de acesso ao POSTGRESQL.
   - `PGADMIN_PASSWORD`: Senha de acesso ao POSTGRESQL.
   - `SQLALCHEMY_DATABASE_URL`: "postgresql+psycopg://usuario:senha@bancodedados:5432/nomedobancodedados"
5. **Dependências do Python**: Este projeto requer algumas bibliotecas do Python. 
    > ✍ Elas serão instaladas automaticamente pelo docker-compose através do arquivo pyproject.toml.


### 🚀 Rodando a API com FastAPI

```bash
# Clone este repositório
git clone <https://github.com/Keilalin/StudentRegistryAPI.git>

# Acesse a pasta do projeto no terminal/cmd
cd StudentRegistryAPI

# Crie e Ative seu ambiente virtual
No Windows:
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    
No macOS ou Linux:
    python3 -m venv venv
    source venv/bin/activate

# Execute o docker-compose
docker-compose up --build -d

# O servidor do fastAPI iniciará na porta:8080 - acesse <http://localhost:8080/docs>

# O servidor do postgreSQL (pgadmin) iniciará na porta:5050 - acesse <http://localhost:5050>
```

### ⚙️ Operações CRUD
No servidor do fastAPI <http://localhost:8080/docs>, utilize as operações CRUD:

<details>
<summary> POST: <strong> CREATE Aluno</strong></summary>
  
  **Entrada**: JSON com `nome` e `email`.
      - Não há a necessidade de incluir o número da id, a não ser que queira.
  
  **Retorno**: `Aluno` criado. </details>

<details>
<summary>GET: <strong>READ Alunos</strong></summary>
  
  **Retorno**: lista de alunos cadastrados.</details>

<details>
<summary>GET: <strong>READ Aluno</strong></summary>
  
  **Entrada**: `id` do aluno para busca
  
  **Retorno**: `Aluno`</details>

<details>
<summary>PUT: <strong>UPDATE Aluno</strong></summary>
  
  **Entrada**: JSON com `nome` e/ou `email`.
  
  **Retorno**: `Aluno` atualizado.</details>

<details>
<summary>DELETE: <strong>DELETE Aluno</strong></summary>
  
  **Entrada**: `id` do aluno para busca
  
  **Retorno**: `Aluno` removido.</details>

### ✅ Teste da API

Swagger UI: http://localhost:8080/docs<br>
PGadmin Web: http://localhost:5050

### 🛡️ Segurança

Todas as imagens utilizadas para subir os contêineres foram escaneadas pelo Trivy e não foram encontradas vulnerabilidades.

### 🌐 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [Rancher Desktop](https://rancherdesktop.io/)
- [VS Code](https://code.visualstudio.com/)
