from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html");

@app.route('/inicio_imc')
def inicio_imc():
    return render_template("inicio_imc.html");

@app.route('/imc', methods=['GET'])
def imc():
    nome = request.args.get('nome')
    altura = float(request.args.get('altura'))
    peso = float(request.args.get('peso'))
    imc = round((peso/altura ** 2),2)
                
    mensagem = ''

    if (imc < 18.5):
        mensagem = "Você está abaixo do peso."

    elif(imc < 24.9):
        mensagem = "Você está com o peso normal."
    
    elif(imc < 29.9):
        mensagem = "Você está com sobrepeso"

    else:
        mensagem = "você está obseso"

    return render_template("imc.html", mensagem = mensagem, nome = nome, imc = imc);

@app.route('/inicio_pizzaria')
def inicio_pizzaria():
    return render_template("inicio_pizzaria.html");

@app.route('/fazer_pedido')
def fazer_pedido():
    return render_template("fazer_pedido.html");

@app.route('/confirmacao', methods=['POST'])
def confirmacao():
    massa = request.form.get('massa')
    molho = request.form.get('molho')
    ingrediente1 = request.form.get ('ingrediente1')
    ingrediente2 = request.form.get ('ingrediente2')
    ingrediente3 = request.form.get ('ingrediente3')
    ingrediente4 = request.form.get ('ingrediente4')
    borda = request.form.get ('borda')
    endereco = request.form.get ('endereco')
    

    return render_template("confirmacao.html", massa = massa, molho = molho, ingrediente1 = ingrediente1, ingrediente2 = ingrediente2, ingrediente3 = ingrediente3, ingrediente4 = ingrediente4, borda = borda, endereco = endereco);