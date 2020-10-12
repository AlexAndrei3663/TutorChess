import math
import numpy as np

class conexao:
    def __init__(self, neuronio):
        self.neuronio = neuronio

        #Sino de Gauss para valores iniciais
        self.peso = np.random.normal()
        self.peso_var = 0.0

class Neuron:
    eta = 0.001
    alpha = 0.01

    def __init__(self, camada):
        self.dendrons = []
        self.erro = 0.0
        self.gradiente = 0.0
        self.saida = 0.0
        if camada is not None:
            for neuronio in camada:
                con = conexao(neuronio)
                self.dendrons.append(con)

    def erro_add(self, erro_num):
        self.erro = self.erro + erro_num

    def sigmoid(self, k):
        return math.exp(k)/(1+math.exp(k))

    def sigmoid_inv(self, k):
        return k * (1.0 - k)

    def set_erro(self, erro_num):
        self.erro = erro_num

    def set_saida(self, saida):
        self.saida = saida

    def get_saida(self):
        return self.saida

    #Vê oq dá
    def forward_propagation(self):
        saida_total = 0
        if len(self.dendrons) == 0:
            return
        for dendron in self.dendrons:
            saida_total = saida_total + dendron.neuronio.get_saida() * dendron.peso
        self.saida = self.sigmoid(saida_total)

    #Aprendizado
    def back_propagation(self):
        self.gradiente = self.erro * self.sigmoid_inv(self.saida);
        for dendron in self.dendrons:
            dendron.peso_var = Neuron.eta * (
            dendron.neuronio.saida * self.gradiente) + self.alpha * dendron.peso_var;
            dendron.peso = dendron.peso + dendron.peso_var;
            dendron.neuronio.erro_add(dendron.peso * self.gradiente);
        self.erro = 0;

class rede_neural:
    def __init__(self, topologia):
        self.camadas = []
        for neuronio_num in topologia:
            camada = []
            for i in range(neuronio_num):
                if (len(self.camadas) == 0):
                    camada.append(Neuron(None))
                else:
                    camada.append(Neuron(self.camadas[-1]))
            camada.append(Neuron(None)) # bias neuronio
            camada[-1].set_saida(1) # setting saida of bias neuronio as 1
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

    def forward_propagation(self):
        for camada in self.camadas[1:]:
            for neuronio in camada:
                neuronio.forward_propagation()

    def back_propagation(self, alvo):
        for i in range(len(alvo)):
            self.camadas[-1][i].set_erro(alvo[i] - self.camadas[-1][i].get_saida())
        for camada in self.camadas[::-1]: #reverse the order
            for neuronio in camada:
                neuronio.back_propagation()

    def get_resultado(self):
        saida = []
        for neuronio in self.camadas[-1]:
            saida.append(neuronio.get_saida())
        saida.pop() # removing the bias neuronio
        return saida

def main():
    topologia = []
    topologia.append(2)
    topologia.append(3)
    topologia.append(2)
    rede = rede_neural(topologia)
    Neuron.eta = 0.09
    Neuron.alpha = 0.015
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saidas = [[0, 0], [1, 0], [1, 0], [0, 1]]
    while True:
        erro_num = 0
        for i in range(len(entrada)):
            rede.set_entrada(entrada[i])
            rede.forward_propagation()
            rede.back_propagation(saidas[i])
            erro_num = erro_num + rede.get_erro(saidas[i])
        print("erro: ", erro_num)
        if erro_num<0.1:
            break

    while True:
        a = int(input("type 1st input :"))
        b = int(input("type 2nd input :"))
        rede.set_entrada([a, b])
        rede.forward_propagation()
        print(rede.get_resultado())

if __name__ == '__main__':
    main()