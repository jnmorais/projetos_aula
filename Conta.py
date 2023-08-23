class ContaCorrente:
    def __int__(self):
        self.numero = 0
        self.saldo = 0

    def depositar(self,valor):
        self.saldo += valor
        print("operação concluida")
    def sacar(self,valor):
        if valor > self.saldo:
            print("Operação invalida")
        else:
            self.saldo -= valor
            print("operação concluida")
