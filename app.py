from flask import Flask, jsonify, request

app = Flask(__name__)

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
}


#GET do Capolupo---------------------------------------------------------------------------------------------------------


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
