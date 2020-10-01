class No:
    #Construtor da classe Nó
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    #Apenas printa o valor desse Nó
    def mostra_no(self):
        print(self.valor)

class Lista:
    #Construtor da lista
    def __init__(self):
        self.primeiro = None #primeiro elemento (No) da lista
        self.ultimo = None #ultimo elemento (No) da lista
    
    #Retorna se a lista está vazia
    def lista_vazia(self):
        return self.primeiro == None

    #insere um termo em cima dos outros (no inicio da lista)
    def insere_inicio(self, valor):
        #cria um novo nó
        novo = No(valor)
        
        #Caso a lista esteja vazia, esse nó será o ultimo
        if self.lista_vazia():
            self.ultimo = novo
        else:
            #Caso ele nao seja o primeiro elemento inserido,
            #Então o ultimo da lista vai apontar para esse novo elemento
            self.ultimo.anterior = novo
        
        #Agora, esse novo elemento é o primeiro da lista
        novo.proximo = self.primeiro
        self.primeiro = novo

    #Insere um novo elemento no fim da lista
    def insere_final(self, valor):
        novo = No(valor)

        #Caso a lista esteja vazia, esse pserá o primeiro termo
        if self.lista_vazia():
            self.primeiro = novo
        else:
            #Apontar o "ponteiro" do nosso ultimo valor para o novo
            self.ultimo.proximo = novo
            #Aopntar o "ponteiro" do novo valor para o nosso antigo ultimo
            novo.anterior = self.ultimo

        #Agora, o novo é o ultimo elemento da lista
        self.ultimo = novo
    
    def excluir_inicio(self):
        #criar uma variavel temporaria para guardar o primeiro elemento (vai ser apagado)
        temp = self.primeiro

        if self.primeiro.proximo == None:
            #Se o primeiro elemento não aponta pra ninguem, apenas esvaziar a lista, não tem um proximo
            self.ultimo = None
        else:
            #Resetar o ponteiro do próximo termo que apontava pra ele
            self.primeiro.proximo.anterior = None
        
        #Agora o primeiro termo é o próximo
        self.primeiro = self.primeiro.proximo

        #retornar o elemento excluido
        return temp

    #Exclui o elemento final da lista
    def excluir_final(self):
        temp = self.ultimo

        #decicir qual ponteiro resetar
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        
        #Depois de resetar o ultimo, lembrar de sincronizar o ponteiro
        self.ultimo = self.ultimo.anterior
        return temp
    
    #Exclui o elemento na posicao
    def excluir_posicao(self, valor):
        #elemento temporário, começa do inicio da lista
        atual = self.primeiro

        #encontrar o elemento
        while atual.valor != valor:
            atual = atual.proximo
            
            #Elemento não encontrado
            if atual == None:
                return None

        #Verificar se esse termo é o primeiro da lista
        #Sincronizar os ponteiros
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        
        #retornar o valor removido
        return atual
    
    #Printa do primeiro elemento ao ultimo
    def mostrar_frente(self):
        #Começar do primeiro elemento e ir até o ultimo
        atual = self.primeiro

        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    #Printa do ultimo elemento ao primeiro
    def mostrar_tras(self):
        atual = self.ultimo

        while atual != None:
            atual.mostra_no()
            atual = atual.anterior
    
    #Verifica se a Lista contem o valor indicado
    def contem_valor(self, valor):
        atual = self.primeiro

        while atual != None:
            if atual.valor == valor:
                return True
            
            atual = atual.proximo
        
        return False
