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

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
