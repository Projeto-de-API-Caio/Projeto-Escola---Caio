from config import db

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
    }



class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'))
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float,nullable=False)
    media_final = db.Column(db.Numeric(5, 2),nullable=False)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final


    def to_dict(self):
        return {
        'id': self.id,
        'nome': self.nome,
        'idade': self.idade,
        'turma_id': self.turma_id,
        'data_nascimento': self.data_nascimento.isoformat(),
        'nota_primeiro_semestre': float(self.nota_primeiro_semestre),
        'nota_segundo_semestre': float(self.nota_segundo_semestre),
        'media_final': float(self.media_final)
                }


class AlunoNaoIdentificado(Exception):
    pass

def getAlunos():
    return (escola["alunos"])

def obter_aluno_por_id(id):
    for aluno in escola["alunos"]:
        if aluno.get("id") == id:
            return aluno, 200
    return ({"erro": "aluno nao encontrado"}), 400

def criarAluno(dados):
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

def updateAluno(idAluno, dados):
    for aluno in escola["alunos"]:
        if aluno["id"] == idAluno:
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





