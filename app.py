from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


languages = [
    {'name': 'JavaScript'},
    {'name': 'C#'},
    {'name': 'Java'},
    {'name': 'PHP'},
    {'name': 'Dart'},
    {'name': 'C++'},
    {'name':'Python'}
]


@app.get('/')
def main():
    return render_template('index.html')


@app.get('/api/langs')
def returnAll():
    return jsonify({'languages': languages})


@app.get('/api/langs/<name>')
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.post('/api/langs')
def addLang():
    language = request.get_json('name')

    languages.append(language)
    return jsonify({'languages': languages})


if __name__ == '__main__':
    app.run(debug=True)