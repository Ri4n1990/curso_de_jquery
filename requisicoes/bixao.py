from flask import Flask, request, render_template, jsonify
import os

paginas = os.path.abspath('paginas')
print(paginas)

app = Flask(__name__, template_folder= paginas)


@app.route('/')
def inicio():

    return render_template('indes.html')

@app.route('/cliente', methods = ['POST'])
def cadastrar_cliente():
    try:
        dados = request.get_json()

        if dados.get('id') == 2:
            print(dados.get('nome'))

            return  jsonify({'nome': 'lufy da borracha'}), 200
        else:
            return jsonify({'usuario não cadastrado!'}) , 500
    
    except Exception as erro:
        return jsonify({'msg' : 'deu ruim'}), 500
        


@app.route('/cliente',methods = ['PUT'])
def atualizar_cliente():
    try:
        dados = request.get_json()
        print(dados.get('nome'))
        return jsonify({'nome':dados.get('nome')}), 200
    
    except Exception as erro:
        print(f'algo saiu errado {erro}')
        return jsonify({'msg' : 'deu ruim'}), 500





if __name__ == '__main__':
    app.run(debug=True)