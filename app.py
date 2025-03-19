from flask import Flask, jsonify, request

app = Flask(__name__)

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
}


#PUT (MATHEUS)--------------------------------------------------------------------------------------------


@app.route("/alunos/<int:idAluno>", methods=["PUT"])
def updateAluno(idAluno):
    for aluno in escola["alunos"]:
        if aluno["id"] == idAluno:
            dados = request.json
            if "nome" not in dados or dados["nome"] == '':
                return jsonify({"erro": "aluno sem nome"}), 400
            aluno["nome"] = dados["nome"]
            return jsonify(aluno), 200
    return jsonify({"erro": "aluno nao encontrado"}), 400

@app.route("/professores/<int:idProfessor>", methods=["PUT"])
def updateProfessor(idProfessor):
    for professor in escola["professores"]:
        if professor["id"] == idProfessor:
            dados = request.json
            if "nome" not in dados or dados["nome"] == '':
                return jsonify({"erro": "professor sem nome"}), 400
            professor["nome"] = dados["nome"]
            return jsonify(professor), 200
    return jsonify({"erro": "professor nao encontrado"}), 400

@app.route("/turmas/<int:idTurma>", methods=["PUT"])
def updateTurma(idTurma):
    for turma in escola["turmas"]:
        if turma["id"] == idTurma:
            dados = request.json
            if "nome" in dados:
                turma["nome"] = dados["nome"]
            if "alunos" in dados:
                turma["alunos"] = dados["alunos"]
            return jsonify(turma), 200
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
