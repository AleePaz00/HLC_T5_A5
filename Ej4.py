# Crea una clase CuentaBancaria con un atributo saldo. 
# Implementa métodos para consultar el saldo 
# (ver_saldo()), depositar (depositar(monto)) y 
# retirar (retirar(monto)) con validaciones.

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def ver_saldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Has depositado {monto}. El nuevo saldo es: {self.saldo}."
        else:
            return "El monto a depositar debe ser positivo."

    def retirar(self, monto):
        if monto > self.saldo:
            return "Fondos insuficientes."
        elif monto <= 0:
            return "El monto a retirar debe ser positivo."
        else:
            self.saldo -= monto
            return f"Has retirado {monto}. El nuevo saldo es: {self.saldo}."
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.ver_saldo())
