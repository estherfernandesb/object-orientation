class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construido objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

##numero da conta e nome do titular nao são alterados, por tanto, não é necessário o uso do GET e SET

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
        

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} excedeu o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular 

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def codigo_banco(self):
        return self.__codigo_banco