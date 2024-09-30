
# Documentação da API

## Índice
1. [Instruções de Configuração](#instruções-de-configuração)
2. [Endpoints](#endpoints)
   - [Listar Produtos Disponíveis](#listar-produtos-disponíveis)
   - [Criar uma Venda](#criar-uma-venda)
   - [Listar Vendas](#listar-vendas)
   - [Obter Detalhes de uma Venda](#obter-detalhes-de-uma-venda)
   - [Adicionar Produto a uma Venda](#adicionar-produto-a-uma-venda)
   - [Cancelar uma Venda](#cancelar-uma-venda)
3. [Postman Documentation](#postman-documentation)

## Instruções de Configuração

### Requisitos
- Python 3.x
- Django 4.x
- Django Rest Framework
- SQLite (padrão)

### Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusername/seuprojeto.git
    cd seuprojeto
    ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ``` 

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Carregue os dados na base de dados:
    ```bash
    python manage.py seed_products
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

Agora, a API estará acessível em `http://localhost:8000/`.

---

## Endpoints

### Listar Produtos Disponíveis

- **URL:** `/api/products/`
- **Método:** `GET`
- **Descrição:** Lista todos os produtos disponíveis para venda (que ainda não foram vendidos).

**Exemplo de Requisição:**

```bash
curl -X GET http://localhost:8000/api/products/
```

### Criar uma Venda

- **URL:** `/api/sales/`
- **Método:** `POST`
- **Descrição:** Cria uma nova venda com os produtos selecionados.

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:8000/api/sales/ -H "Content-Type: application/json" -d '{ "total": 100.00, "Products": [1, 2, 3] }'
```

### Listar Vendas

- **URL:** `/api/sales/`
- **Método:** `GET`
- **Descrição:** Lista todas as vendas realizadas.

**Exemplo de Requisição:**

```bash
curl -X GET http://localhost:8000/api/sales/
```

### Obter Detalhes de uma Venda

- **URL:** `/api/sales/{id}/`
- **Método:** `GET`
- **Descrição:** Exibe os detalhes de uma venda específica com base no ID.

**Exemplo de Requisição:**

```bash
curl -X GET http://localhost:8000/api/sales/1/
```

### Adicionar Produto a uma Venda

- **URL:** `/api/sales/{id}/add-product/`
- **Método:** `POST`
- **Descrição:** Adiciona novos produtos a uma venda existente.

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:8000/api/sales/1/add-product/ -H "Content-Type: application/json" -d '{ "Products": [4, 5] }'
```

### Cancelar uma Venda

- **URL:** `/api/sales/{id}/cancel/`
- **Método:** `POST`
- **Descrição:** Cancela uma venda existente.

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:8000/api/sales/1/cancel/
```


## Postman Documentation

- Para mais informações e testes detalhados, você pode acessar a documentação no Postman através deste link: [Documentação Postman](https://documenter.getpostman.com/view/28920398/2sAXqzWxwa)
