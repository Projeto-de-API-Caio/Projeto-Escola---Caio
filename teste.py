import requests
import unittest

class TestStringMethods(unittest.TestCase):

    # TESTE VICTORIA-----------------------------------------------------------------------------------
    def test_010(self):
        # verifica se um aluno pode ser deletado

        r = requests.delete('http://localhost:5000/alunos/3')
        self.assertEqual(r.status_code, 204) 
        r = requests.get('http://localhost:5000/alunos/3')
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')
        print("10 OK")

    def test_011(self):
        #tenta deletar um aluno que nao

        r = requests.delete('http://localhost:5000/alunos/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')
        print("11 OK")

    def test_012(self):
        requests.post('http://localhost:5000/reseta')

        r = requests.post('http://localhost:5000/alunos', json={"id": 5, "nome": "Fabiano"})
        self.assertEqual(r.status_code, 200)

        r_delete = requests.delete('http://localhost:5000/alunos/5')
        self.assertEqual(r_delete.status_code, 204)

        r_lista = requests.get('http://localhost:5000/alunos')
        alunos = r_lista.json()
        self.assertFalse(any(aluno["id"] == 5 for aluno in alunos), "Aluno 5 ainda está na lista")

        print("12 OK")

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
    unittest.main()