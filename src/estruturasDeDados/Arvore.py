class Node:
    def __init__(self, data=None, pos=None, left=None, right=None):
        self.data = data
        self.pos = pos
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"{self.left} <- {self.data} -> {self.right}"
    
    def __str__(self):
        return str(self.pos)

        
class BinarySearchTree:
    def __init__(self, data=None, pos=None, node=None):
        if node:
            self.root = node
        if data:
            self.root = Node(data, pos)
        else:
            self.root = None
        
    def inOrder(self, node="root"):
        """ Imprime na tela a arvore em ordem simetrica """
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
            
        # Se node não for vazia, eh impimido o no em ordem simetrica
        if node:
            self.inOrder(node.left)
            print(node,end=" ")
            self.inOrder(node.right)
    
    def preOrder(self, node="root"):
        """ Imprime na tela a arvore em pre ordem """
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
        
        # Se node não for vazia, eh impimido o no em pre ordem
        if node:
            print(node,end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)
     
    def posOrder(self, node="root"):
        """ Imprime na tela a arvore em ordem simetrica """
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
            
        # Se node não for vazia, eh impimido o no em pos ordem
        if node:
            self.posOrder(node.left)
            self.posOrder(node.right)
            print(node,end=" ")
    
    def height(self, node="root"):
        """ Retorna a altura da arvore """
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
            
        h_left = 0
        h_right = 0
        
        # Descobre qual o maior ramo
        if node.left:
            h_left = self.height(node.left)
        if node.right:
            h_right = self.height(node.right)
            
        #Retorna o valor do maior ramo mais um pelo atual
        if h_left < h_right:
            return h_right + 1
        return h_left + 1
        
    def min(self, node="root"):
        """ Retorna o no com o valor minimo na arvore """
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
            
        # Encontra o no mais a esquerda
        while node.left:
            node = node.left
        return node.data, node.pos
    
    def max(self, node="root"):
        """ Retorna o no com o valor maximo na arvore """
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
            
        # Encontra o no mais a direita
        while node.right:
            node = node.right
        return node.data, node.pos
        
    def insert(self, data, pos):
        """ Insersao do dado na arvore """
        
        # Finaliza se não houver valor
        if data is None:
            return
        if pos is None:
            return
        
        # Encontra o local para alocar o dado
        current = self.root
        parent = None
        while current:
            parent = current
            # Vai para a esquerda se for menor e direita se for maior
            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        # Aloca o dado no local encontrado
        # Se nao houver raiz, insere na raiz
        if parent is None:
            self.root = Node(data, pos)
        # Insere a esquerda se for menor e a direita se for maior
        elif data < parent.data:
            parent.left = Node(data, pos)
        else:
            parent.right = Node(data, pos)
            
    def search(self, data, node="root"):
        "Busca o no referente ao valor inserido"
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
        # Se nao encontrar o valor retorna None
        elif node is None:
            return node
        # Se achar o valor, retorna seu no
        if node.data == data:
            return node
        # Continua procurando
        # A esquerda se for menor e a direita se for maior
        if node.data > data:
            return self.search(data, node.left)
        return self.search(data, node.right)
    
    def remove(self, data, node="root"):
        "Remove o no com o dado especificado"
        
        # Se não for inserido um no
        # a raiz da arvore eh inserida como no inicial
        if node == "root":
            node = self.root
        
        elif node is None:
            return node
        
        if data < node.data:
            node.left = self.remove(data, node.left)
        elif data > node.data:
            node.right = self.remove(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                sub = self.min(node.right)
                node.data, node.pos = sub
                node.right = self.remove(sub[0], node.right)
        
        return node
