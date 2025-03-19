from flask import Flask, jsonify, request

app = Flask(__name__)

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
}


#GET ID da Joicy S2-----------------------------------------------------------------------------------------------------


@app.route("/alunos/<int:id>", methods=["GET"])
def obter_aluno_por_id(id):
    for aluno in escola["alunos"]:
        if aluno.get("id") == id:
            return jsonify(aluno)
    return jsonify({"erro": "aluno nao encontrado"}), 400

@app.route("/professores/<int:id>", methods=["GET"])
def obter_professor_por_id(id):
    for professor in escola["professores"]:
        if professor.get("id") == id:
            return jsonify(professor)
    return jsonify({"erro": "professor nao encontrado"}), 400

@app.route("/turma/<int:id>", methods=["GET"])
def obter_turma_por_id(id):
    for turma in escola["turmas"]:
        if turma["id"] == id:
            return jsonify(turma)
    return jsonify({"erro": "turma nao encontrada"}), 400



# RESETAR DADOS
@app.route("/reseta", methods=["POST", "DELETE"])
def reseta():
    escola["alunos"].clear()
    escola["professores"].clear()
    escola["turmas"].clear()
    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
