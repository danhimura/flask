from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    variavel = 'Game adivinhe o numero correto'


    if request.method =='GET':
        return render_template("index.html", variavel=variavel)

    else:
        numero = randint(1, 20)
        palpite = int(request.form.get('name'))

        if numero == palpite:
            return '<h1>Você Ganhou</hi>'

        else:
            return '<h1>Perdeu Idiota</hi>'


@app.route('/<string:nome>')
def error(nome):
    variavel = f'Párgina {nome} não encontrada Erro 404'
    return render_template('error.html', variavel=variavel)



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
