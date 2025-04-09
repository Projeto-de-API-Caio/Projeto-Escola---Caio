from flask import Flask, jsonify, request

app = Flask(__name__)

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
    }

# RESETAR DADOS

@app.route("/reseta", methods=["POST", "DELETE"])
def reseta():
    escola["alunos"].clear()
    escola["professores"].clear()
    escola["turmas"].clear()
    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
