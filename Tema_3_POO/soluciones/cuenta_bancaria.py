'''CUENTA BANCARIA - EJERCICIO 1
Crear una clase CuentaBancaria que tenga los siguientes atributos:
- titular (str)
- cantidad (float)
Y los siguientes métodos:
- __init__(): que reciba el titular y la cantidad. Si la cantidad es menor que 0, lanzar una excepción ValueError 
    y mostrar el mensaje "La cantidad no puede ser menor que 0".
- mostrar(): que muestre el mensaje "Titular: {titular} - Cantidad: {cantidad}".
- ingresar(cantidad): que incremente la cantidad de la cuenta en la cantidad que se indique. 
Si se intenta ingresar una cantidad negativa, mostrar un mensaje de error.
- retirar(cantidad): que decremente la cantidad de la cuenta en la cantidad que se indique, 
    pero antes se debe comprobar que hay suficiente cantidad. Si no es así, mostrar un mensaje de error.'''
# Solución
# Clase CuentaBancaria
class CuentaBancaria:
    '''Clase que representa una cuenta bancaria'''
    '''
    Atributos:
    - titular (str)
    - cantidad (float)   

    Métodos:
    - __init__(): que reciba el titular y la cantidad. Si la cantidad es menor que 0, lanzar una excepción ValueError
    y mostrar el mensaje "La cantidad no puede ser menor que 0".
    - mostrar(): que muestre el mensaje "Titular: {titular} - Cantidad: {cantidad}".
    - ingresar(cantidad): que incremente la cantidad de la cuenta en la cantidad que se indique.
    Si se intenta ingresar una cantidad negativa, mostrar un mensaje de error.
    - retirar(cantidad): que decremente la cantidad de la cuenta en la cantidad que se indique,
    pero antes se debe comprobar que hay suficiente cantidad. Si no es así, mostrar un mensaje de error.
    '''

    def __init__(self, titular, cantidad):
        self.titular = titular
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser menor que 0")
        self.cantidad = cantidad    

    def mostrar(self):
        '''Muestra el titular y la cantidad de la cuenta'''
        print(f"Titular: {self.titular} - Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        '''Ingresa una cantidad en la cuenta'''
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser menor que 0")
        self.cantidad += cantidad

    def retirar(self, cantidad):
        '''Retira una cantidad de la cuenta'''
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser menor que 0")
        if cantidad > self.cantidad:
            raise ValueError("No hay suficiente cantidad")
        self.cantidad -= cantidad

# Pruebas
cuenta = CuentaBancaria("Juan", 1000)
cuenta.mostrar()
cuenta.ingresar(500)
cuenta.mostrar()
cuenta.retirar(200)
cuenta.mostrar()
cuenta.retirar(2000) # Debe lanzar una excepción
cuenta.mostrar()
cuenta.ingresar(-100) # Debe lanzar una excepción
cuenta.mostrar()
cuenta.retirar(-100) # Debe lanzar una excepción
cuenta.mostrar()
cuenta = CuentaBancaria("Ana", -1000) # Debe lanzar una excepción
cuenta.mostrar 
# Salida esperada
# Titular:
# Juan - Cantidad: 1000
# Titular:
# Juan - Cantidad: 1500
# Titular:
# Juan - Cantidad: 1300
# Traceback (most recent call last):
#   File "cuenta_bancaria.py", line 37, in <module>
#     cuenta.retirar(2000) # Debe lanzar una excepción
#   File "cuenta_bancaria.py", line 24, in retirar
#     raise ValueError("No hay suficiente cantidad")
# ValueError: No hay suficiente cantidad

