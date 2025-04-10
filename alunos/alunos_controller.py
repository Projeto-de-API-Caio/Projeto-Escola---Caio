from flask import Flask, jsonify, request
import alunos_model as model


app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def exibir_alunos():
    print("LISTA DE TODOS ALUNOS:")
    return  jsonify(model.getAlunos())

@app.route("/alunos/<int:id>", methods=["GET"])
def exibir_alunos_por_id(id):
    aluno, status = model.obter_aluno_por_id(id)
    return jsonify(aluno), status
    
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    print("CRIANDO ALUNO!")
    dados = request.json
    aluno, status = model.criarAluno(dados)
    return jsonify(aluno), status

@app.route("/alunos/<int:idAluno>", methods=["PUT"])
def atualizar_aluno(idAluno):
    dados = request.json
    aluno, status = model.updateAluno(idAluno, dados)
    return jsonify(aluno), status

@app.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deletar_aluno(idAluno):
    resposta, status = model.deleteAluno(idAluno)
    return (jsonify(resposta), status) if resposta else ('', status)

if __name__ == "__main__":
    app.run(debug=True)