# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Criar uma API REST em Python com FastAPI, aprendendo a definir rotas, receber parâmetros, validar dados com Pydantic e tratar erros.

## 📝 Tasks

### 🛠️ Create Your First Endpoint

#### Descrição
Instale o FastAPI e o Uvicorn (`pip install fastapi uvicorn`) e crie um arquivo `main.py` com uma aplicação que responde em uma rota raiz.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` chamada `app`
- Expor uma rota `GET /` que retorna um JSON com a chave `message`
- Executar a API com `uvicorn main:app --reload` e acessar a rota no navegador


### 🛠️ Use Path and Query Parameters

#### Descrição
Crie rotas que recebem dados pela URL para retornar informações de itens de uma lista.

#### Requisitos
O programa concluído deve:

- Criar uma rota `GET /items/{item_id}` que retorna o item correspondente a partir de uma lista ou dicionário
- Retornar um erro 404 quando o `item_id` não existir
- Criar uma rota `GET /items` que aceita o parâmetro opcional `limit` e retorna no máximo essa quantidade de itens


### 🛠️ Validate Data with Pydantic

#### Descrição
Crie uma rota `POST` que recebe dados em JSON e valida sua estrutura usando um modelo Pydantic.

#### Requisitos
O programa concluído deve:

- Definir uma classe `Item` herdando de `BaseModel`, com os campos `name` (texto), `price` (número) e `in_stock` (booleano)
- Criar uma rota `POST /items` que recebe um `Item` e o adiciona à lista de itens
- Retornar o item criado com status 201
- Rejeitar automaticamente requisições com tipos de dados incorretos


### 🛠️ Handle Errors and Document Your API

#### Descrição
Melhore a API tratando erros de forma clara e conferindo a documentação gerada automaticamente pelo FastAPI.

#### Requisitos
O programa concluído deve:

- Usar `HTTPException` para retornar erro 404 com uma mensagem clara quando um item não for encontrado
- Impedir a criação de itens com `name` já existente, retornando erro 400
- Acessar a documentação interativa em `/docs` e testar todas as rotas por ela
