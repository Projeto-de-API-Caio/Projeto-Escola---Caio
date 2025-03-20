import requests
import unittest

class TestStringMethods(unittest.TestCase): 

    def test_001_get_alunos(self):
        
        r = requests.get('http://localhost:5000/alunos')
        self.assertEqual(r.status_code, 200)
        alunos = r.json()
        self.assertIsInstance(alunos, list)
        print("1 OK")

    def test_002_lista_vazia(self):
         # verifica se a lista alunos está vazia

        r = requests.get('http://localhost:5000/alunos')
        self.assertEqual(r.status_code, 200)
        alunos = r.json()
        self.assertEqual(len(alunos), 0)
        print("2 OK")

    def test_003_get_dados(self):
        # garante que a lista alunos traga dados criados

        r = requests.post('http://localhost:5000/alunos', json={"id": 1, "nome": "Filipe"})
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://localhost:5000/alunos')
        self.assertEqual(len(r_lista.json()), 1)
        self.assertEqual(r_lista.json()[0]['nome'], 'Filipe')
        print("3 OK")

    def teste_17_get_turmas_lista(self):
        resp = requests.get('http://localhost:5000/turmas')
        if resp.status_code == 404:
            self.fail("pagina /turmas não encontrada")

        try:
            retorno = resp.json()
        except:
            self.fail("retorno não saiu como json")

        self.assertEqual(type(retorno),type([]))
        print("17 OK")

    def test_007(self):
       # cria aluno novo com dados válidos

        aluno_data = {"id": 3, "nome": "Victoria"}
        r = requests.post('http://localhost:5000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 200)
        aluno = r.json()
        self.assertEqual(aluno['nome'], 'Victoria')
        self.assertEqual(aluno['id'], 3)
        print("7 OK")

    def test_008(self):
        # verifica se nao é possível criar um aluno com ID que já existe

        aluno_data = {"id": 3, "nome": "Joicy"}
        r = requests.post('http://localhost:5000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'id ja utilizada')
        print("8 OK")

    def test_009(self):
        # cria aluno sem nome (erro)

        aluno_data = {"id": 4}
        r = requests.post('http://localhost:5000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("9 OK")

   
    # TESTE EXTRA------------------------------------------------------------------------------------
    def test_016(self):
        #criar aluno sem nome (erro)


        aluno_data = {"id": 6}
        r = requests.post('http://localhost:5000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("16 OK")

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
