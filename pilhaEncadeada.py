class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def exclui_inicio(self):
        if self.lista_vazia():
            print('Lista Vazia.')
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

class PilhaEncadeada:
    def __init__(self):
        self.pilha = ListaEncadeada()

    def empilhar(self, valor):
        self.pilha.insere_inicio(valor)

    def desempilha(self):
        return self.pilha.exclui_inicio()

    def pilha_vazia(self):
        return self.pilha.lista_vazia()

    def ver_topo(self):
        if self.pilha_vazia():
            return -1
        return self.pilha.primeiro.valor