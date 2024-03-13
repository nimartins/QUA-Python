#renderiza o que esta na pasta templates

from flask import Flask, render_template

#classe letra maiuscula = para orientar o produto
#construtor padrao: sem parametro (), em python nao usa
#parametro de init = ele mesmo, self = atributos da classe
class Produto:
    def __init__(self, nome_prod, marca_prod, preco_prod):
        #propriedades
        self.nome = nome_prod
        self.marca = marca_prod
        self.preco = preco_prod

#variável de aplicação
app = Flask(__name__)

@app.route('/inicio')
def ola():
    return '<h1>Iniciando Flask</h1>'

@app.route('/lista')
def lista():

    #a linha abaixo instancia um novo produto
    prod01 = Produto("Camisa","Nike","R$ 300,00")
    prod02 = Produto("Blusa","Lacoste","R$ 255,00")
    prod03 = Produto("Calça","Oakley","R$ 200,00")

    produtos_cadastrados = [prod01, prod02, prod03]

    return render_template('lista.html',descricao="Aqui estão seus produtos cadastrados.",lista_prod = produtos_cadastrados)

app.run()
