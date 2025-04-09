from flask import Flask, jsonify, request
import alunos_model as model


app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def exibir_alunos():
    print("LISTA DE TODOS ALUNOS:")
    return  jsonify(model.getAlunos())

@app.route("/alunos/<int:id>", methods=["GET"])
def exibir_alunos_por_id(id):
    return jsonify(model.obter_aluno_por_id(id)) 
    
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    print("CRIANDO ALUNO!")
    return jsonify(model.criarAluno())

@app.route("/alunos/<int:idAluno>", methods=["PUT"])
def atualizar_aluno(idAluno):
    return jsonify(model.updateAluno(idAluno))

@app.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deletar_aluno(idALuno):
    return jsonify(model.deleteAluno(idALuno))

