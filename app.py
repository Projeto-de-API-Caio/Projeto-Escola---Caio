from flask import Flask, jsonify, request

app = Flask(__name__)

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
}


#GET do Capolupo---------------------------------------------------------------------------------------------------------

@app.route("/alunos", methods=["POST"])
def criarAluno():
    dados = request.json
    if "id" not in dados or "nome" not in dados:
        return jsonify({"erro": "aluno sem nome"}), 400
    
    for aluno in escola["alunos"]:
        if aluno["id"] == dados["id"]:
            return jsonify({"erro": "id ja utilizada"}), 400
    
    novo_aluno = {
        "id": dados["id"],
        "nome": dados["nome"]
    }
    escola["alunos"].append(novo_aluno)
    return jsonify(novo_aluno), 200

@app.route("/professores", methods=["POST"])
def criarProfessor():
    dados = request.json
    if "id" not in dados or "nome" not in dados:
        return jsonify({"erro": "professor sem nome"}), 400
    
    for professor in escola["professores"]:
        if professor["id"] == dados["id"]:
            return jsonify({"erro": "id ja utilizada"}), 400
    
    novo_professor = {
        "id": dados["id"],
        "nome": dados["nome"]
    }
    escola["professores"].append(novo_professor)
    return jsonify(novo_professor), 200

@app.route("/turmas", methods=["POST"])
def criarTurma():
    dados = request.json
    if "id" not in dados or "nome" not in dados or "alunos" not in dados:
        return jsonify({"erro": "informacoes incompletas para criar turma"}), 400
    
    nova_turma = {
        "id": dados["id"],
        "nome": dados["nome"],
        "alunos": dados["alunos"]
    }
    escola["turmas"].append(nova_turma)
    return jsonify(nova_turma), 200

@app.route("/alunos", methods=["GET"])
def getAlunos():
    return jsonify(escola["alunos"])

@app.route("/professores", methods=["GET"])
def getProfessores():
    return jsonify(escola["professores"])

@app.route("/turmas", methods=["GET"])
def getTurmas():
    return jsonify(escola["turmas"])

# RESETAR DADOS

@app.route("/reseta", methods=["POST", "DELETE"])
def reseta():
    escola["alunos"].clear()
    escola["professores"].clear()
    escola["turmas"].clear()
    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
