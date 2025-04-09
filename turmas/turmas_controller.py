from flask import Flask, jsonify, request
import turmas_model as model

app = Flask(__name__)

@app.route("/turmas", methods=["GET"])
def exibir_turmas():
    print("LISTA DE TODAS TURMAS:")
    return model.getTurmas()

@app.route("/turma/<int:id>", methods=["GET"])
def exibir_turma_por_id(id):
    return jsonify(model.obter_turma_por_id(id)) 

@app.route("/turmas", methods=["POST"])
def criar_turma():
    return jsonify(model.criarTurma())

@app.route("/turmas/<int:idTurma>", methods=["PUT"])
def atualizar_turma(idTurma):
    return jsonify(model.updateTurma(idTurma))

@app.route("/turmas/<int:idTurma>", methods=["DELETE"])
def deletar_turma(idTurma):
    return jsonify(model.deleteTurma(idTurma))

