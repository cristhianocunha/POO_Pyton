

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("contruindo obejeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if (valor <= self.saldo):
            self.__saldo -= valor
        else:
            print("saldo baixo")