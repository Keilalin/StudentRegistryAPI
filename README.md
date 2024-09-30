<h1 align="center"> StudentRegistryAPI </h1>
Esta API permite gerenciar informações de alunos por meio das operações básicas de CRUD (Create, Read, Update, Delete). 
Combinando  FastAPI e PostgreSQL através do SQLAlchemy, o projeto foi desenvolvido em Python.
<br></br>

Índice
=================
<!--ts-->
   * [Pré Requisitos](#pre-requisitos)
        * [Rodando a API](#-rodando-a-api-com-fastapi)
        * [Operações CRUD](#operações-crud)
        * [Teste da API](#teste-da-api)
   * [Arquivos](https://github.com/Keilalin/StudentRegistryAPI/tree/461c2a2e6a9a3a4595b5f82d6570746e49ebc04a/arquivos_py)
   * [Tecnologias](#tecnologias)
<!--te-->

### Pré-requisitos

Antes de executar o projeto, certifique-se de que você tenha instalado os seguintes softwares e bibliotecas:

1. [**Python 3.12 ou superior**](https://www.python.org/): O projeto é desenvolvido em Python, então você precisará ter uma versão compatível instalada.
2. [**PostgreSQL**](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads): Um banco de dados PostgreSQL deve estar instalado e em execução em sua máquina ou acessível via rede.
3. **Variáveis de ambiente**: As seguintes variáveis de ambiente devem ser configuradas no seu arquivo `.env`:
   - `DB_USERNAME`: Nome de usuário do banco de dados.
   - `DB_PASSWORD`: Senha do banco de dados.
   - `DB_HOST`: Endereço do servidor do banco de dados (ex: `localhost`).
   - `DB_PORT`: Porta do servidor do banco de dados (ex: `5432`).
   - `DB_NAME`: Nome do banco de dados que será utilizado.

4. **Dependências do Python**: As bibliotecas necessárias podem ser instaladas usando o `pip`. Execute o seguinte comando para instalar as dependências:

   ```bash
   pip install fastapi[all] sqlalchemy psycopg2 python-dotenv

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### 🎲 Rodando a API com FastAPI

```bash
# Clone este repositório
git clone <https://github.com/Keilalin/StudentRegistryAPI.git>

# Acesse a pasta do projeto no terminal/cmd
cd StudentRegistryAPI

# Vá para a pasta arquivos_py
cd arquivos_py

# Ative seu ambiente virtual
No Windows:
    .\venv\Scripts\Activate.ps1
    
No macOS ou Linux:
    source venv/bin/activate

# Instale as dependências
pip install fastapi[all] sqlalchemy psycopg2 python-dotenv

# Execute a aplicação com o uvicord
uvicorn main:app --reload

# O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000/docs>
```

### Operações CRUD
- POST: **CREATE Aluno**
  
  **Entrada**: JSON com `nome` e `email`.
      - Não há a necessidade de incluir o número da id, a não ser que queira.
  
  **Retorno**: `Aluno` criado.

- GET: **READ Alunos**
  
  **Retorno**: lista de alunos cadastrados.

- GET: **READ Aluno**
  
  **Entrada**: `id` do aluno para busca
  
  **Retorno**: `Aluno`

- PUT: **UPDATE Aluno**
  
  **Entrada**: JSON com `nome` e/ou `email`.
  
  **Retorno**: `Aluno` atualizado.

- DELETE: **DELETE Aluno**
  
  **Entrada**: `id` do aluno para busca
  
  **Retorno**: `Aluno` removido.

### Teste da API

Swagger UI: http://127.0.0.1:8000/docs

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [VS Code](https://code.visualstudio.com/)
