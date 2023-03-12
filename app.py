from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extrai as informações do formulário
        num_avaliacoes = int(request.form['num_avaliacoes'])
        notas = []
        pesos = []
        for i in range(num_avaliacoes):
            nota = float(request.form['nota{}'.format(i)])
            peso = float(request.form['peso{}'.format(i)])
            notas.append(nota)
            pesos.append(peso)
        media_aprovacao = float(request.form['media_aprovacao'])

        # Calcula a nota final e determina a mensagem
        nota_final = sum([notas[i] * pesos[i] for i in range(num_avaliacoes)]) / (sum(pesos) * 1.0)
        gpa = nota_final / 20 - 1
        mensagem = ''
        if nota_final >= media_aprovacao:
            mensagem = 'Parabéns, você foi aprovado!'
        else:
            nota_necessaria = (media_aprovacao - sum([notas[i] * pesos[i] for i in range(num_avaliacoes)])) / (1 - sum(pesos))
            mensagem = f'Você precisa de uma nota de {nota_necessaria:.2f} na próxima avaliação para ser aprovado.'

        # Renderiza a página de resultado com as informações calculadas
        return render_template("resultado.html", nota_final=nota_final, mensagem=mensagem)
    else:
        num_avaliacoes = 3
        return render_template("index.html", num_avaliacoes=num_avaliacoes)

if __name__ == '__main__':
    app.run(debug=True)
