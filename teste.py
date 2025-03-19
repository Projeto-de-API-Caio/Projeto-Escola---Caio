import requests
import unittest

class TestStringMethods(unittest.TestCase):

   
    # TESTES JOICY-------------------------------------------------------------------------------------
    def test_004_buscaAlunoId(self):

         # busca aluno por ID
        r = requests.get('http://localhost:5000/alunos/1')
        self.assertEqual(r.status_code, 200)
        aluno = r.json()
        self.assertEqual(aluno['id'], 1)
        self.assertEqual(aluno['nome'], 'Filipe')
        print("4 OK")

    def test_005__AlunoInexistente(self):
        # tenta acessar aluno que não existe

        r = requests.get('http://localhost:5000/alunos/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("5 OK")

    def test_006_verificação(self):
         # verifica se dados retornados são certos

        r = requests.post('http://localhost:5000/alunos', json={"id": 2, "nome": "Matheus"})
        self.assertEqual(r.status_code, 200)
        r_get = requests.get('http://localhost:5000/alunos/2')
        self.assertEqual(r_get.status_code, 200)
        aluno = r_get.json()
        self.assertEqual(aluno['nome'], 'Matheus')
        print("6 OK")

    
   



  
    # TESTE EXTRA------------------------------------------------------------------------------------
    def test_016_semAluno(self):
        #criar aluno sem nome (erro)


        aluno_data = {"id": 6}
        r = requests.post('http://localhost:5000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("16 OK")

if __name__ == '__main__':
    unittest.main()