from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {
        'id': 1,
        'titulo': 'Fallen Angels - 1995',
        'diretor': 'Wong-Kar-Wai'
    },
    {
        'id': 2,
        'titulo': 'Scarface',
        'diretor': 'Brian De Palma'
    },
    {
        'id': 3,
        'titulo': 'Taxi Driver',
        'diretor': 'Martin Scorsese'
    }
]

@app.route('/filmes',methods=['GET'])
def consulta_filmes():
    return jsonify(filmes)

@app.route('/filmes/<int:id>',methods=['GET'])
def busca_de_filme_id(id):
    for filme in filmes:
       if filme.get('id') == id:
           return jsonify(filme)

@app.route('/filmes/<int:id>', methods=['PUT'])
def editar_filme_id(id):
    filme_editado = request.get_json() 
    for indice,filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].update(filme_editado)
            return jsonify(filmes[indice])

@app.route('/filmes',methods=['POST'])
def adicionar_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)

    return jsonify(filmes)

@app.route('/filmes/<int:id>',methods=['DELETE'])
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]
        return jsonify(filmes)

app.run(port=5000,host='localhost',debug=True)
