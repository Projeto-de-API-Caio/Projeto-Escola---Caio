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


if __name__ == '__main__':
    unittest.main()