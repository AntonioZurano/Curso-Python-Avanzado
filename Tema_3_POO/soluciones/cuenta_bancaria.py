'''CUENTA BANCARIA - EJERCICIO 1
Crear una clase CuentaBancaria que tenga los siguientes atributos:
- cuenta (str)
- saldo (float)
# Solución
'''
'''# Clase CuentaBancaria
'''
class CuentaBancaria:
    '''Clase CuentaBancaria 
    Atributos:
    - cuenta (str)
    - saldo (float)
    Métodos:
    - depositar(monto)
    - retirar(monto)
    '''
    def __init__(self, cuenta, saldo=0):
        self.cuenta = cuenta
        self.saldo = saldo

    def depositar(self, monto):
        '''Método depositar
        Permite depositar un monto en la cuenta
        Parámetros:
        - monto: float
        '''
        self.saldo += monto
        print(f"Depósito de {monto} EU. Saldo actual: {self.saldo} EU")

    def retirar(self, monto):
        '''Método retirar
        Permite retirar un monto de la cuenta
        Parámetros:
        - monto: float
        ''' 
        if self.saldo < monto:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto
            print(f"Retiro de {monto} EU. Saldo actual: {self.saldo} EU")


# Pruebas   
cuenta = CuentaBancaria("123456")
cuenta.depositar(100)
cuenta.retirar(50)
cuenta.retirar(100)
cuenta.depositar(200)
cuenta.retirar(150)
cuenta.retirar(200)

