# 📽️ API de Filmes com Flask

Este projeto é uma API simples desenvolvida em **Python** com **Flask**, que permite realizar operações de CRUD (Create, Read, Update, Delete) em uma lista de filmes.

---

## 🚀 Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)

---

## 📌 Funcionalidades
A API trabalha com uma lista de filmes em memória (sem banco de dados).  
Cada filme possui os atributos:
- `id` (int)
- `titulo` (string)
- `diretor` (string)

Endpoints disponíveis:

### 🔍 Consultar todos os filmes
GET /filmes

shell
Copiar código
Retorna a lista completa de filmes.

### 🔍 Consultar filme por ID
GET /filmes/<id>

vbnet
Copiar código
Exemplo:
```http
GET /filmes/2
Resposta:

json
Copiar código
{
  "id": 2,
  "titulo": "Scarface",
  "diretor": "Brian De Palma"
}
✏️ Editar um filme por ID
bash
Copiar código
PUT /filmes/<id>
Body (JSON):

json
Copiar código
{
  "titulo": "Scarface (1983)",
  "diretor": "Brian De Palma"
}
Retorna o filme atualizado.

➕ Adicionar novo filme
bash
Copiar código
POST /filmes
Body (JSON):

json
Copiar código
{
  "id": 4,
  "titulo": "Pulp Fiction",
  "diretor": "Quentin Tarantino"
}
❌ Excluir filme por ID
bash
Copiar código
DELETE /filmes/<id>
▶️ Como executar o projeto
Clone este repositório:

bash
Copiar código
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
Copiar código
pip install flask
Execute a aplicação:

bash
Copiar código
python app.py
A API estará disponível em:

arduino
Copiar código
http://localhost:5000
📖 Exemplos de uso com curl
Listar todos os filmes:

bash
Copiar código
curl http://localhost:5000/filmes
Adicionar um novo filme:

bash
Copiar código
curl -X POST http://localhost:5000/filmes -H "Content-Type: application/json" -d '{"id":4,"titulo":"Pulp Fiction","diretor":"Quentin Tarantino"}'
Editar um filme:

bash
Copiar código
curl -X PUT http://localhost:5000/filmes/2 -H "Content-Type: application/json" -d '{"titulo":"Scarface (1983)","diretor":"Brian De Palma"}'
Excluir um filme:

bash
Copiar código
curl -X DELETE http://localhost:5000/filmes/1
