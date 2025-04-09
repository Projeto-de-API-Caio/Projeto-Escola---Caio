from flask import request

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
    }

def getTurmas():
    return (escola["turmas"])

def obter_turma_por_id(id):
    for turma in escola["turmas"]:
        if turma["id"] == id:
            return (turma)
    return ({"erro": "turma nao encontrada"}), 400

def criarTurma():
    dados = request.json
    if "id" not in dados or "nome" not in dados or "alunos" not in dados:
        return ({"erro": "informacoes incompletas para criar turma"}), 400
    
    nova_turma = {
        "id": dados["id"],
        "nome": dados["nome"],
        "alunos": dados["alunos"]
    }
    escola["turmas"].append(nova_turma)
    return (nova_turma), 200

def updateTurma(idTurma):
    for turma in escola["turmas"]:
        if turma["id"] == idTurma:
            dados = request.json
            if "nome" in dados:
                turma["nome"] = dados["nome"]
            if "alunos" in dados:
                turma["alunos"] = dados["alunos"]
            return (turma), 200
    return ({"erro": "turma nao encontrada"}), 400

def deleteTurma(idTurma):
    turma_existe = any(turma["id"] == idTurma for turma in escola["turmas"])
    if not turma_existe:
        return ({"erro": "turma nao encontrada"}), 400

    escola["turmas"] = [turma for turma in escola["turmas"] if turma["id"] != idTurma]
    return '', 204