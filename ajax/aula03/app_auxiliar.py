from flask import Flask, render_template, jsonify, request
import os

paginas = os.path.abspath('paginas')

app = Flask(__name__, template_folder= paginas)



@app.route('/')
def main():
    return render_template('tratando_respostas.html')

@app.route('/mensagem',methods = ['GET'])
def mensagem():

    print('chegou')
    
    try:
        return jsonify({'mensagem':'eae home'}) , 200

    except Exception as erro:
        print(f'algo saiu errado {erro} ')
        return jsonify({'erro' : "deu ruim"} , 500)





@app.route('/cadastrar', methods = ['POST'])
def fazer_cadastro():
    try:
        dados = request.get_json()
        print(dados.get('nome'), dados.get('sobrenome'))
        return jsonify({'msg' : 'carla cadastrada!'}) , 201

    except Exception as erro:
        print(f'algo saiu errado!')
        return jsonify({'erro' : "deu ruim"} , 500)
    

@app.route('/atualizar', methods= ['PUT'])
def atualizar():

    try:
        dados = request.get_json()

        print('Dados recebidos!', dados.get('nome'), dados.get('sobrenome'))
        return jsonify({'msg' : 'cliente Atualizado'}), 201


    except Exception as erro:

        print(f'algo saiu errado! {erro}')
        return jsonify({'erro' : "deu ruim!"}), 500

    
@app.route('/deletar', methods = ['DELETE'])
def deletar_cliente():
    try:
        dados = request.get_json()

        print(f'cliente { dados.get("id") } Deletado com sucesso!')

        return jsonify({'msg': 'sucesso'}), 204

    except Exception as erro:
        print(f'algo saiu errado!', erro)
        return jsonify({'erro' : 'deu ruim ein'}), 500

    

    













if __name__ == "__main__":
    print('Servidor rodando') 
    app.run(debug = True , port=3080)
    