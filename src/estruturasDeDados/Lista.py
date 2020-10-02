class No:
    # Construtor da classe Nó
    def __init__(self, valor = None):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    # Apenas printa o valor desse Nó
    def __str__(self):
        return str(self.valor)

class Lista:
    # Construtor da lista
    def __init__(self):
        # Primeiro elemento (No) da lista
        self.primeiro = None
        # Ultimo elemento (No) da lista
        self.ultimo = None
        # Tamanho da lista
        self.__tamanho = 0
    
    @property
    def tamanho(self):
        return self.__tamanho

    # Retorna se a lista está vazia
    def __lista_vazia(self):
        return self.primeiro == None

    # Insere um termo em cima dos outros (no inicio da lista)
    def insere_inicio(self, valor):
        # Cria um novo nó
        novo = No(valor)
        
        # Caso a lista esteja vazia, esse nó será o ultimo
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            # Caso ele nao seja o primeiro elemento inserido,
            # Então o ultimo da lista vai apontar para esse novo elemento
            self.primeiro.anterior = novo
        
        # Agora, esse novo elemento é o primeiro da lista
        novo.proximo = self.primeiro
        self.primeiro = novo
        self.__tamanho += 1

    # Insere um novo elemento no fim da lista
    def insere_final(self, valor):
        novo = No(valor)

        # Caso a lista esteja vazia, esse será o primeiro termo
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            # Apontar o "ponteiro" do nosso ultimo valor para o novo
            self.ultimo.proximo = novo
            

        # Agora, o novo é o ultimo elemento da lista
        novo.anterior = self.ultimo
        self.ultimo = novo
        self.__tamanho += 1
    
    # Insere valor na posição desejada
    def insere_posicao(self, valor, posicao):
        # Valor temporário que recebe o endereço do primeiro
        temp = self.primeiro

        # Se a lista estiver vazia e não quiser inserir na primeira posição, erro
        if self.__lista_vazia() and posicao != 0:
            print('Lista vazia')
            return
        
        # Posição de insereção é a primeira O(1)
        if posicao == 0:
            self.insere_inicio(valor)
        # Posição de inserção é a última O(1)
        elif posicao == self.__tamanho - 1:
            self.insere_final(valor)
        # Posição no meio da Lista O(n)
        else:
            indice = 0
            while temp != None:
                if indice == posicao:
                    insere = No(valor)
                    insere.anterior = temp
                    insere.proximo = temp.proximo
                    temp.proximo.anterior = insere
                    temp.proximo = insere
                temp = temp.proximo
                indice += 1
        
        # Aumenta o tamanho da Lista
        self.__tamanho += 1

    # Exclução do Início O(1)
    def excluir_inicio(self):
        # Criar uma variavel temporaria para guardar o primeiro elemento (vai ser apagado)
        temp = self.primeiro

        # Se o primeiro elemento não aponta pra ninguem, apenas esvaziar a lista, não tem um proximo (1 elemento)
        if self.primeiro.proximo == None:
            self.ultimo = None
        # Resetar o ponteiro do próximo termo que apontava pra ele
        else:
            self.primeiro.proximo.anterior = None
        
        # Agora o primeiro termo é o próximo
        self.primeiro = self.primeiro.proximo

        # Retornar o elemento excluido
        self.__tamanho -= 1
        return temp

    # Exclui o elemento final da lista O(1)
    def excluir_final(self):
        # Criar uma variavel temporaria para guardar o ultimo elemento (vai ser apagado)
        temp = self.ultimo

        # Se o ultimo elemento não é aponta por ninguem, apenas esvaziar a lista, não tem um anterior (1 elemento)
        if self.ultimo.anterior == None:
            self.primeiro = None
        # Resetar o ponteiro do anterior termo que apontava pra ele
        else:
            self.ultimo.anterior.proximo = None
        
        # Depois de resetar o ultimo, lembrar de sincronizar o ponteiro
        self.ultimo = self.ultimo.anterior
        self.__tamanho -= 1
        return temp
    
    # Exclui o elemento na posicao O(n)
    def excluir_posicao(self, valor):
        # Elemento temporário, começa do inicio da lista
        excluir = self.primeiro

        # Encontrar o elemento
        while excluir.valor != valor:
            # Elemento não encontrado
            if excluir == None:
                return None
            excluir = excluir.proximo

        # Verificar se esse termo é o primeiro da lista
        # Sincronizar os ponteiros (esquerda)
        if excluir == self.primeiro:
            self.primeiro = excluir.proximo
        else:
            excluir.anterior.proximo = excluir.proximo

        # Sincronizar os ponteiros (direita)
        if excluir == self.ultimo:
            self.ultimo = excluir.anterior
        else:
            excluir.proximo.anterior = excluir.anterior
        
        # Retornar o valor removido
        self.__tamanho -= 1
        return excluir
    
    # Printa do primeiro elemento ao ultimo
    def mostrar_frente(self):
        # Começar do primeiro elemento e ir até o ultimo
        atual = self.primeiro

        while atual != None:
            print(atual)
            atual = atual.proximo

    # Printa do ultimo elemento ao primeiro
    def mostrar_tras(self):
        # Começar do ultimo elemento e ir até o primeiro
        atual = self.ultimo

        while atual != None:
            print(atual)
            atual = atual.anterior

    # Verifica se a Lista contem o valor indicado
    def contem_valor(self, valor):
        atual = self.primeiro

        while atual != None:
            if atual.valor == valor:
                return True
            
            atual = atual.proximo
        
        return False