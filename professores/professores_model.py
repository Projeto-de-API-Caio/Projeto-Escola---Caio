
escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
    }

def getProfessores():
    return (escola["professores"])

def obter_professor_por_id(id):
    for professor in escola["professores"]:
        if professor.get("id") == id:
            return professor, 200
    return ({"error": "Professor não encontrado"}), 400

def criarProfessor(dados):
    if "id" not in dados or "nome" not in dados:
        return ({"error": "professor sem nome"}), 400
    
    for professor in escola["professores"]:
        if professor["id"] == dados["id"]:
            return ({"error": "id ja utilizada"}), 400
    
    novo_professor = {
        "id": dados["id"],
        "nome": dados["nome"]
    }
    escola["professores"].append(novo_professor)
    return (novo_professor), 200

def updateProfessor(idProfessor, dados):
    for professor in escola["professores"]:
        if professor["id"] == idProfessor:
            if "nome" not in dados or dados["nome"] == '':
                return ({"error": "professor sem nome"}), 400
            professor["nome"] = dados["nome"]
            return (professor), 200
    return ({"error": "Professor não encontrado"}), 400

def deleteProfessor(idProfessor):
    professor_existe = any(prof['id'] == idProfessor for prof in escola["professores"])
    if not professor_existe:
        return ({"error": "Professor não encontrado"}), 400

    escola["professores"] = [prof for prof in escola["professores"] if prof["id"] != idProfessor]
    return '', 200
