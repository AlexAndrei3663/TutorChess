import math
import numpy as np

class conexao:
    def __init__(self, neuronio):
        self.neuronio = neuronio

        #Sino de Gauss para valores iniciais
        self.peso = np.random.normal()
        self.peso_var = 0.0

class neuronio:
    eta = 0.001
    alpha = 0.01

    def __init__(self, camada):
        self.dendronios = []
        self.erro = 0.0
        self.gradiente = 0.0
        self.saida = 0.0
        if camada is not None:
            for neuronio in camada:
                con = conexao(neuronio)
                self.dendronios.append(con)

    def erro_add(self, erro_num):
        self.erro = self.erro + erro_num

    def sigmoid(self, k):
        return math.exp(k)/(1+math.exp(k))

    def sigmoid_inv(self, k):
        return k*(1-k)

    def set_erro(self, erro_num):
        self.erro = erro_num

    def set_saida(self, saida):
        self.saida = saida

    def get_saida(self):
        return self.saida

    #Vê oq dá
    def propagacao_forward(self):
        saida_total = 0
        if len(self.dendronios) == 0:
            return
        for dendronio in self.dendronios:
            saida_total = saida_total + dendronio.neuronio.get_saida() * dendronio.peso
        self.saida = self.sigmoid(saida_total)

    #Aprendizado
    def propagacao_back(self):
        self.gradiente = self.erro * self.sigmoid_inv(self.saida);
        for dendronio in self.dendronios:
            dendronio.peso_var = neuronio.eta * (
            dendronio.neuronio.saida * self.gradiente) + self.alpha * dendronio.peso_var;
            dendronio.peso = dendronio.peso + dendronio.peso_var;
            dendronio.neuronio.erro_add(dendronio.peso * self.gradiente);
        self.erro = 0;

class rede_neural:
    def __init__(self, topologia):
        self.camadas = []
        for neuronio_num in topologia:
            camada = []
            for i in range(neuronio_num):
                if (len(self.camadas) == 0):
                    camada.append(neuronio(None))
                else:
                    camada.append(neuronio(self.camadas[-1]))
            camada.append(neuronio(None)) # bias neuronio
            camada[-1].set_saida(1) # bias neuronio como 1
            self.camadas.append(camada)

    def set_entrada(self, entrada):
        for i in range(len(entrada)):
            self.camadas[0][i].set_saida(entrada[i])

    def get_erro(self, alvo):
        erro_num = 0
        for i in range(len(alvo)):
            e = (alvo[i] - self.camadas[-1][i].get_saida())
            erro_num = erro_num + e ** 2
        erro_num = erro_num / len(alvo)
        erro_num = math.sqrt(erro_num)
        return erro_num

    def propagacao_forward(self):
        for camada in self.camadas[1:]:
            for neuronio in camada:
                neuronio.propagacao_forward()

    def propagacao_back(self, alvo):
        for i in range(len(alvo)):
            self.camadas[-1][i].set_erro(alvo[i] - self.camadas[-1][i].get_saida())
        for camada in self.camadas[::-1]: #inverter a ordem
            for neuronio in camada:
                neuronio.propagacao_back()

    def get_resultado(self):
        saida = []
        for neuronio in self.camadas[-1]:
            saida.append(neuronio.get_saida())
        saida.pop() # remover o neuronio bias
        return saida

def main():
    topologia = []
    topologia.append(2)
    topologia.append(3)
    topologia.append(2)
    rede = rede_neural(topologia)
    neuronio.eta = 0.09
    neuronio.alpha = 0.015
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = [[0, 0], [1, 0], [1, 0], [0, 1]]
    while True:
        erro_num = 0
        for i in range(len(entrada)):
            rede.set_entrada(entrada[i])
            rede.propagacao_forward()
            rede.propagacao_back(saidas[i])
            erro_num = erro_num + rede.get_erro(saidas[i])
        print("erro: ", erro_num)
        if erro_num<0.1:
            break

    while True:
        a = int(input("type 1st input :"))
        b = int(input("type 2nd input :"))
        rede.set_entrada([a, b])
        rede.propagacao_forward()
        print(rede.get_resultado())

if __name__ == '__main__':
    main()