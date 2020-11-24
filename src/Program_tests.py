import unittest
from estruturasDeDados import PilhaEncadeada as Pilha

class ArvoreRedBlackTests(unittest.TestCase):
    pass

class ListaDuplamenteEncadeadaTests(unittest.TestCase):
    pass

class PilhaEncadeadaTests(unittest.TestCase):
    def setUp(self):
        self.pilha = Pilha.Pilha()

    def test_adding_element(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)

        # Adição
        self.pilha.empilhar(-3)
        self.assertEqual(len(self.pilha), 3, 'Tamanho invalido.')
        self.assertEqual(self.pilha.retorna_topo(), -3, 'Valor não corresponde com o esperado.')

    def test_remove_element(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)
        self.pilha.empilhar(-3)

        #Remoção
        self.pilha.desempilha()
        self.assertEqual(len(self.pilha), 2, 'Tamanho invalido.')
        self.assertEqual(self.pilha.retorna_topo(), 120, 'Valor não corresponde com o esperado.')
    
    def test_remove_element_empty(self):
        # Remover elemento invalido
        with self.assertRaises(Warning):
            self.pilha.desempilha()

    def test_change_top(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)
        self.pilha.empilhar(-3)

        # Alterar topo
        self.pilha.altera_topo([1, 2, 3, 4])
        self.assertEqual(len(self.pilha), 3, 'Tamanho invalido.')
        self.assertEqual(self.pilha.retorna_topo(), [1, 2, 3, 4], 'Valor não corresponde com o esperado.')

    def test_clear_stack(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)
        self.pilha.empilhar(-3)

        # Limpar pilha
        self.pilha.limpa_pilha()
        self.assertEqual(len(self.pilha), 0, 'Tamanho invalido.')
        self.assertEqual(self.pilha.retorna_topo(), None, 'Valor não corresponde com o esperado.')

    def test_equal_stack(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)
        self.pilha.empilhar(-3)

        # Segunda pilha
        segunda_pilha = Pilha.Pilha()
        segunda_pilha.empilhar(10)
        segunda_pilha.empilhar(120)
        segunda_pilha.empilhar(-3)

        # Comparação
        self.assertTrue(self.pilha == segunda_pilha, 'Pilhas diferentes.')
        
if __name__ == "__main__":
    unittest.main()