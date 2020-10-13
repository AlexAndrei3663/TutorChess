from . import ListaDuplamenteEncadeada

class Pilha(ListaDuplamenteEncadeada.Lista):
    def __init__(self):
        super().__init__()

    # Empilha um novo valor no topo da pilha O(1)
    def empilhar(self, valor):
        self.insere_inicio(valor)

    # Retira o valor do topo da pilha O(1)
    # caso seja passado o segundo atributo, seram retirados n elementos O(n)
    def desempilha(self, quantidade = 1):
        if quantidade == 1:
            self.excluir_inicio()
        else:
            for _ in range(quantidade):
                self.excluir_inicio()

    # Visualiza o elemento do topo O(1)
    def retorna_topo(self):
        if self.tamanho == 0:
            return None
        return self.retorna_elemento(0)

    def altera_topo(self, valor):
        self.altera_valor(valor, 0)