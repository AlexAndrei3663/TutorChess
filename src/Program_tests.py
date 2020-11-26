import unittest
import random as rd
from estruturasDeDados import ArvoreRedBlack as Arvore
from estruturasDeDados import PilhaEncadeada as Pilha
from estruturasDeDados import ListaDuplamenteEncadeada as Lista

class ArvoreRedBlackTests(unittest.TestCase):
    def setUp(self):
        self.tree = Arvore.RedBlackTree()

    def test_max_value_tree(self):
        # Gerando arvore aleatória
        teste_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rd.shuffle(teste_values)
        for i in teste_values:
            self.tree.add(i, i)
            
        self.assertEqual(self.tree.max().value, 10, 'Valor não corresponde com o esperado.')

    def test_min_value_tree(self):
        # Gerando arvore aleatória
        teste_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rd.shuffle(teste_values)
        for i in teste_values:
            self.tree.add(i, i)
            
        self.assertEqual(self.tree.min().value, 0, 'Valor não corresponde com o esperado.')

    def test_three_highest_values_tree(self):
        # Gerando arvore aleatória
        teste_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rd.shuffle(teste_values)
        for i in teste_values:
            self.tree.add(i, i)
        teste_tree = self.tree.max3()
        self.assertEqual(teste_tree[0].value, 10, 'Maior valor não corresponde com o esperado.')
        self.assertEqual(teste_tree[1].value,  9, 'Segundo maior valor não corresponde com o esperado.')
        self.assertEqual(teste_tree[2].value,  8, 'Terceiro maior valor não corresponde com o esperado.')

    def test_three_lowest_values_tree(self):
        # Gerando arvore aleatória
        teste_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rd.shuffle(teste_values)
        for i in teste_values:
            self.tree.add(i, i)
        teste_tree = self.tree.min3()
        self.assertEqual(teste_tree[0].value, 0, 'Menor valor não corresponde com o esperado.')
        self.assertEqual(teste_tree[1].value, 1, 'Segundo menor valor não corresponde com o esperado.')
        self.assertEqual(teste_tree[2].value, 2, 'Terceiro menor valor não corresponde com o esperado.')

class ListaDuplamenteEncadeadaTests(unittest.TestCase):
    def setUp(self):
        self.lista = Lista.Lista()
        self.lista.insere_inicio('meio')

    def test_initialize_list(self):
        lista_test = Lista.Lista(3, 'teste')
        self.assertEqual(len(lista_test), 3, 'Tamanho Invalido.')
        self.assertEqual(lista_test[0], 'teste', 'Valor não corresponde com o esperado.')
        self.assertEqual(lista_test[1], 'teste', 'Valor não corresponde com o esperado.')
        self.assertEqual(lista_test[2], 'teste', 'Valor não corresponde com o esperado.')

    def test_adding_element_begin_list(self):
        self.lista.insere_inicio('inicio')
        self.assertEqual(len(self.lista), 2, 'Tamanho Invalido.')
        self.assertEqual(self.lista[0], 'inicio', 'Valor não corresponde com o esperado.')
        self.assertEqual(self.lista[1], 'meio', 'Valor não corresponde com o esperado.')

    def test_adding_element_end_list(self):
        self.lista.insere_final('final')
        self.assertEqual(len(self.lista), 2, 'Tamanho Invalido.')
        self.assertEqual(self.lista[1], 'final', 'Valor não corresponde com o esperado.')
        self.assertEqual(self.lista[0], 'meio', 'Valor não corresponde com o esperado.')

    def test_adding_element_position_list(self):
        # Adiciona elementos
        self.lista.insere_inicio('inicio')
        self.lista.insere_final('final')

        # (inicio) -- (meio) -- (posicao) -- (final)
        self.lista.insere_posicao('posicao', 2)
        self.assertEqual(len(self.lista), 4, 'Tamanho Invalido.')
        self.assertEqual(self.lista[0], 'inicio', 'Valor não corresponde com o esperado.')
        self.assertEqual(self.lista[1], 'meio', 'Valor não corresponde com o esperado.')
        self.assertEqual(self.lista[2], 'posicao', 'Valor não corresponde com o esperado.')
        self.assertEqual(self.lista[3], 'final', 'Valor não corresponde com o esperado.')

    def test_adding_element_invalid_position_list(self):
        # -1 não existe
        with self.assertRaises(IndexError):
            self.lista.insere_posicao(4, -1)
        # só existe 1 elemento, então não tem como linkar com o 50
        with self.assertRaises(IndexError):
            self.lista.insere_posicao(4, 50)

    def test_change_element_list(self):
        self.lista[0] = 'troca'
        self.assertEqual(len(self.lista), 1, 'Tamanho Invalido.')
        self.assertEqual(self.lista[0], 'troca', 'Valor não corresponde com o esperado.')

    def test_change_invalid_element_list(self):
        # -1 não existe
        with self.assertRaises(IndexError):
            self.lista[-1] = 10
        # só existe 1 elemento, então não tem como mudar o 50
        with self.assertRaises(IndexError):
            self.lista[50] = 10  

    def test_remove_element_begin_list(self):
        # Adicionar elementoss
        self.lista.insere_final('final')

        '''
        (meio) -- (final)
        (final)
        ''' 
        self.lista.excluir_inicio()
        self.assertEqual(len(self.lista), 1, 'Tamanho Invalido.')
        self.assertEqual(self.lista[0], 'final', 'Valor não corresponde com o esperado.')

    def test_remove_element_end_list(self):
        # Adicionar elementoss
        self.lista.insere_inicio('inicio')

        '''
        (inicio) -- (meio)
        (inicio)
        ''' 
        self.lista.excluir_final()
        self.assertEqual(len(self.lista), 1, 'Tamanho Invalido.')
        self.assertEqual(self.lista[0], 'inicio', 'Valor não corresponde com o esperado.')

    def test_remove_invalid_element_list(self):
        self.lista.excluir_final()

        # Remover do final ou do inicio de uma lista vazia
        with self.assertRaises(Warning):
            self.lista.excluir_final()
        with self.assertRaises(Warning):
            self.lista.excluir_inicio()

        self.lista.insere_final(10)
        # Remover valor inexistente na lista
        with self.assertRaises(Warning):
            self.lista.excluir_posicao(50)

    def test_print_front_list(self):
        self.lista.insere_inicio('inicio')
        self.lista.insere_final('final')

        '''
        (inicio) -- (meio) -- (final)
        '''
        
        self.assertEqual(self.lista.mostrar_frente(), 'inicio meio final ', 'Print Invalido.')
        self.assertEqual(self.lista.mostrar_tras(), 'final meio inicio ', 'Print Invalido.')

class PilhaEncadeadaTests(unittest.TestCase):
    def setUp(self):
        self.pilha = Pilha.Pilha()

    def test_adding_element_stack(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)

        # Adição
        self.pilha.empilhar(-3)
        self.assertEqual(len(self.pilha), 3, 'Tamanho invalido.')
        self.assertEqual(self.pilha.retorna_topo(), -3, 'Valor não corresponde com o esperado.')

    def test_remove_element_stack(self):
        # Adicionar elementos
        self.pilha.empilhar(10)
        self.pilha.empilhar(120)
        self.pilha.empilhar(-3)

        #Remoção
        self.pilha.desempilha()
        self.assertEqual(len(self.pilha), 2, 'Tamanho invalido.')
        self.assertEqual(self.pilha.retorna_topo(), 120, 'Valor não corresponde com o esperado.')
    
    def test_remove_element_empty_stack(self):
        # Remover elemento invalido
        with self.assertRaises(Warning):
            self.pilha.desempilha()

    def test_change_top_stack(self):
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