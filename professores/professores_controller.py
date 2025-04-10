from flask import Flask, jsonify, request
import professores_model as model

app = Flask(__name__)

@app.route("/professores", methods=["GET"])
def exibir_professores():
    print("LISTA DE TODOS PROFESSORES:")
    return jsonify(model.getProfessores())

@app.route("/professores/<int:id>", methods=["GET"])
def exibir_professor_por_id(id):
    professor , status = model.obter_professor_por_id(id)
    if status != 200:
        return jsonify({"error": "Professor não encontrado"}), 400
    return jsonify(professor)

@app.route("/professores", methods=["POST"])
def criar_professor():
    print("CRIANDO PROFESSOR!")
    dados = request.json
    professor , status = model.criarProfessor(dados)
    return jsonify(professor), status

@app.route("/professores/<int:idProfessor>", methods=["PUT"])
def atualizar_professor(idProfessor):
    dados = request.get_json()
    professor , status = model.updateProfessor(idProfessor, dados)
    return jsonify(professor), status

@app.route("/professores/<int:idProfessor>", methods=["DELETE"])
def deletar_professor(idProfessor):
    professor , status = model.deleteProfessor(idProfessor)
    return jsonify(professor), status

if __name__ == "__main__":
    app.run(debug=True)