from flask import Flask, jsonify, request
import professores_model as model

app = Flask(__name__)

@app.route("/professores", methods=["GET"])
def exibir_professores():
    print("LISTA DE TODOS PROFESSORES:")
    return jsonify(model.getProfessores())

@app.route("/professores/<int:id>", methods=["GET"])
def exibir_professor_por_id(id):
    return jsonify(model.obter_professor_por_id(id)) 

@app.route("/professores", methods=["POST"])
def criar_professor():
    print("CRIANDO PROFESSOR!")
    return jsonify(model.criarProfessor())

@app.route("/professores/<int:idProfessor>", methods=["PUT"])
def atualizar_aluno(idProfessor):
    return jsonify(model.updateProfessor(idProfessor))

@app.route("/professores/<int:idProfessor>", methods=["DELETE"])
def deletar_aluno(idProfessor):
    return jsonify(model.deleteProfessor(idProfessor))

if __name__ == "__main__":
    app.run(debug=True)
