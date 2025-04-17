import os
from config import app, db
from alunos.alunos_controller import alunos_blueprint
from professores.professores_controller import professores_blueprint
from flask import jsonify

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)


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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )