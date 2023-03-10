from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    num_avaliacoes = 3
    return render_template("index.html", num_avaliacoes=num_avaliacoes)


@app.route('/calcular', methods=['POST'])
def calcular():
    # Obter as notas das avaliações
    num_avaliacoes = int(request.form['num_avaliacoes'])

    notas = []

    for i in range(num_avaliacoes):
        nota = float(request.form['nota_{}'.format(i)])
        notas.append(nota)

    # Calcular a média ponderada de notas
    pesos = [1/num_avaliacoes] * num_avaliacoes
    nota_final = sum([notas[i]*pesos[i] for i in range(num_avaliacoes)])

    # Obter a meta de GPA e calcular a nota necessária
    media_aprovacao = float(request.form['media_aprovacao'])
    meta_gpa = media_aprovacao
    if nota_final < media_aprovacao:
        nota_necessaria = (meta_gpa - nota_final*(num_avaliacoes/10)) / (1-(num_avaliacoes/10))
        mensagem = "Para alcançar sua nota para aprovação, você precisa de uma nota de pelo menos {:.2f} na próxima avaliação.".format(nota_necessaria)
    else:
        mensagem = "Parabéns! Você já está aprovado."
    
    return render_template('resultado.html', nota_final=nota_final, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
