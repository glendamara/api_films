# 🎬 Filmes API

Esta é uma API RESTful simples, criada com **Python** e **Flask**, para gerenciar uma lista de filmes.

## 🚀 Como Executar

1.  Certifique-se de que você tem **Python** e **Flask** instalados.
2.  Salve o código como um arquivo Python (por exemplo, `app.py`).
3.  Execute o arquivo a partir do seu terminal:
    ```bash
    python app.py
    ```
4.  A aplicação estará rodando em `http://localhost:5000`.

   ## 💻 Endpoints

| Método HTTP | Endpoint          | Funcionalidade                                    |
|-------------|-------------------|---------------------------------------------------|
| **GET** | `/filmes`         | Recupera a lista completa de todos os filmes.     |
| **GET** | `/filmes/<int:id>`| Busca um filme específico usando seu ID.          |
| **POST** | `/filmes`         | Adiciona um novo filme à lista.                   |
| **PUT** | `/filmes/<int:id>`| Atualiza as informações de um filme existente.    |
| **DELETE** | `/filmes/<int:id>`| Exclui um filme da lista usando seu ID.  
