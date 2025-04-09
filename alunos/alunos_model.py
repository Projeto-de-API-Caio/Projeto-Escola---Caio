from flask import request

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
    }

class AlunoNaoIdentificado(Exception):
    pass

def getAlunos():
    return (escola["alunos"])

def obter_aluno_por_id(id):
    for aluno in escola["alunos"]:
        if aluno.get("id") == id:
            return (aluno)
    return ({"erro": "aluno nao encontrado"}), 400

def criarAluno():
    dados = request.json
    if "id" not in dados or "nome" not in dados:
        return ({"erro": "aluno sem nome"}), 400
    
    for aluno in escola["alunos"]:
        if aluno["id"] == dados["id"]:
            return ({"erro": "id ja utilizada"}), 400
    
    novo_aluno = {
        "id": dados["id"],
        "nome": dados["nome"]
    }
    escola["alunos"].append(novo_aluno)
    return (novo_aluno), 200

def updateAluno(idAluno):
    for aluno in escola["alunos"]:
        if aluno["id"] == idAluno:
            dados = request.json
            if "nome" not in dados or dados["nome"] == '':
                return ({"erro": "aluno sem nome"}), 400
            aluno["nome"] = dados["nome"]
            return (aluno), 200
    return ({"erro": "aluno nao encontrado"}), 400

def deleteAluno(idAluno):
    aluno_existe = any(aluno['id'] == idAluno for aluno in escola["alunos"])
    if not aluno_existe:
        return ({"erro": "aluno nao encontrado"}), 400

    escola["alunos"] = [aluno for aluno in escola["alunos"] if aluno["id"] != idAluno]
    return '', 204