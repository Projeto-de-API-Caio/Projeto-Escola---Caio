from flask import Flask, jsonify, request

app = Flask(__name__)

#GET do Capolupo---------------------------------------------------------------------------------------------------------


@app.route("/alunos", methods=["GET"])
def exibir_alunos():
    print("LISTA DE TODOS ALUNOS:")
    return model.getAlunos()

@app.route("/professores", methods=["GET"])
def exibir_professores():
    print("LISTA DE TODOS PROFESSORES:")
    return model.getProfessores()

@app.route("/turmas", methods=["GET"])
def exibir_turmas():
    print("LISTA DE TODAS TURMAS:")
    return model.getTurmas()


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


#Meu codigo (POST)FILIPE---------------------------------------------------------------------------------------------

##confirmação
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    print("CRIANDO ALUNO!")
    return model.criarAluno

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


#PUT do SEM MUNDIAL2(MATHEUS)--------------------------------------------------------------------------------------------


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


#DELETAR DA VICTORIA------------------------------------------------------------------------------------------------------


@app.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deleteAluno(idAluno):
    aluno_existe = any(aluno['id'] == idAluno for aluno in escola["alunos"])
    if not aluno_existe:
        return jsonify({"erro": "aluno nao encontrado"}), 400

    escola["alunos"] = [aluno for aluno in escola["alunos"] if aluno["id"] != idAluno]
    return '', 204

@app.route("/professores/<int:idProfessor>", methods=["DELETE"])
def deleteProfessor(idProfessor):
    professor_existe = any(prof['id'] == idProfessor for prof in escola["professores"])
    if not professor_existe:
        return jsonify({"erro": "professor nao encontrado"}), 400

    escola["professores"] = [prof for prof in escola["professores"] if prof["id"] != idProfessor]
    return '', 204

@app.route("/turmas/<int:idTurma>", methods=["DELETE"])
def deleteTurma(idTurma):
    turma_existe = any(turma["id"] == idTurma for turma in escola["turmas"])
    if not turma_existe:
        return jsonify({"erro": "turma nao encontrada"}), 400

    escola["turmas"] = [turma for turma in escola["turmas"] if turma["id"] != idTurma]
    return '', 204


# RESETAR DADOS

@app.route("/reseta", methods=["POST", "DELETE"])
def reseta():
    escola["alunos"].clear()
    escola["professores"].clear()
    escola["turmas"].clear()
    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
