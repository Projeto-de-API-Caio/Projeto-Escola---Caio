import requests
import unittest

class TestStringMethods(unittest.TestCase):
    def test_013(self):
        #  editar o nome de um aluno

        r = requests.put('http://localhost:5000/alunos/3', json={"nome": "Fabiano Silva"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado') 
        print("13 OK")

    def test_014(self):
       # tentar editar um aluno sem nome (erro)
        r = requests.put('http://localhost:5000/alunos/3', json={"id": 3})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("14 OK")

    def test_015(self):
        # tenta editar um aluno que nao existe
        r = requests.put('http://localhost:5000/alunos/100', json={"nome": "Novo Nome"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("15 OK")
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
