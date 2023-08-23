import Conta
import cliente

x = Conta.ContaCorrente()
x.saldo = 50
x.numero = 123

x.depositar(500)
x.sacar(600)
print(x.saldo)
