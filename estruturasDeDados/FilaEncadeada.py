class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def lista_vazia(self):
        return self.primeiro == None

    def insere_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def exclui_inicio(self):
        if self.lista_vazia():
            print('Lista Vazia')
            return None
        
        temp = self.primeiro
        if temp.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

class FilaEncadeada:
    def __init__(self):
        self.fila = ListaEncadeadaExtremidadeDupla()

    def enfileirar(self, valor):
        self.fila.insere_final(valor)

    def desenfileirar(self):
        return self.fila.exclui_inicio()

    def fila_vazia(self):
        return self.fila.lista_vazia()

    def ver_inicio(self):
        if self.fila_vazia():
            return -1
        return self.fila.primeiro.valor