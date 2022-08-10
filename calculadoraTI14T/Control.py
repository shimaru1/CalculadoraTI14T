from Model import Model


class Control:
    def __init__(self):
        self.opcao = -1  # Declaração de variável global
        self.num1 = 0
        self.num2 = 0
        self.modelo = Model()  # conectando com a classe model

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getOpcao(self):  # consulto o conteudo
        return self.opcao

    def setOpcao(self, opcao):  # modifico o conteudo
        set.opcao = opcao

    def setNum1(self, num1):
        set.num1 = num1

    def setNum2(self, num2):
        set.num2 = num2

    def Coletar(self):
        print("informe um numero: ")
        self.setNum1(float(input()))

        print("informe um numero: ")
        self.setNum2(float(input()))

    def menu(self):
        print('Escolha uma das opções abaixo: \n' +
              '1. Soma\n' +
              '2. Subtração\n' +
              '3. Divisão\n' +
              '4. Multiplicação\n' +
              '5. Potencia\n' +
              '6. Raiz\n' +
              '7. Tabuada\n' +
              '0. Sair\n\n')
        self.opcao = int(input())  # Entrada de dados

    def operacao(self):
        while (self.getOpcao != 0):
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado")
                break
            elif self.getOpcao() == 1:
                self.Coletar()
                print("A Soma do dois números é: {}".format(self.modelo.soma(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 2:
                self.Coletar()
                resultado = self.modelo.subtrair(self.getNum1(), self.getNum2())
                if resultado == -1:
                    print("O Impossivel de dividir por zero")
                else:

                    print("A Subtração do dois números é: {}".format(
                        self.modelo.subtrair(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 3:
                self.Coletar()
                print("A Divisao do dois números é: {}".format(self.modelo.divisao(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 4:
                self.Coletar()
                print("A Multiplicação do dois números é: {}".format(
                    self.modelo.multipicacao(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 5:
                self.Coletar()
                print("A Potencia do dois números é: {}".format(self.modelo.potencia(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 6:
                print("Informe um número para calcular a raiz: ")
                resultado = self.modelo.raiz(float(input()))
                if resultado == -1:
                    print("Impossivel calcular a Raiz!")
                else:
                    print("O resultado é {}".format(resultado))
            elif self.getOpcao() == 7:
                print("Informe um número: ")
                print(self.modelo.tabuada(float(input())))
            else:
                print("opção invalida!")
