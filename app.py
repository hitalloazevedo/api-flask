from flask import Flask, jsonify, request


app = Flask(__name__)


languages = [
    {'name': 'Javascript'},
    {'name': 'C#'},
    {'name': 'Java'}
]


@app.get('/')
def main():
    return "<h1>A API ESTÁ NO AR!</h1> <p>Acesse /langs para visualizar</p> <footer>Desenvolvida por Hitallo Azevedo</footer>"


@app.get('/langs')
def returnAll():
    return jsonify({'languages': languages})


@app.post('/langs')
def addLang():
    language = request.get_json('name')

    languages.append(language)
    return jsonify({'languages': languages})


if __name__ == '__main__':
    app.run(debug=True)