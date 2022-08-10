import math


class Model:
    #Criar um metodo construtor
    def __init__(self):
        pass

    def soma(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def divisao(self, num1, num2):
        if num2 <= 0:
            return -1
        else:
            return num1 / num2

    def multipicacao(self, num1, num2):
        return num1 * num2

    def potencia(self, base, expoente):

        if expoente == 0:
            return 1
        elif expoente == 1:
            return base
        return math.pow(base, expoente)

    def raiz(self, num):
        if float(num) < float(0):
            return -1
        else:
            return math.sqrt(num)

    def tabuada(self, num):
        msg = ""
        for i in range(10):# vai ser a quantidade de vezes que vai fazer a operação
            msg = msg + "\n{} * {} = {}".format(num, i, num * i)

        return msg



