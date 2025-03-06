'''SISTEMA DE RESERVAS DE VUELOS
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:
- Clase base: `Vuelo`
- Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
- Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
- Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.
'''
class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def verificar_disponibilidad(self):
        return self.capacidad - len(self.pasajeros)

    def agregar_pasajero(self, pasajero):
        if self.verificar_disponibilidad() > 0:
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero} agregado al vuelo {self.numero}")
        else:
            print(f"No hay asientos disponibles en el vuelo {self.numero}")

    def verificar_disponibilidad(self):
        return self.capacidad - len(self.pasajeros)
    
# Clase Hija
# VueloEspecial hereda de Vuelo
# VueloEspecial es una subclase de Vuelo
# Vuelo es una superclase de VueloEspecial
# Y tiene el atributo motivo
class VueloEspecial(Vuelo):
    def __init__(self, numero, origen, destino, capacidad, motivo):
        super().__init__(numero, origen, destino, capacidad)
        self.motivo = motivo


# Ejemplo de uso
vuelo1 = Vuelo("UA30", "Madrid", "Barcelona", 150)
vuelo2 = Vuelo("AW25", "Barcelona", "París", 200)
vuelo_especial1 = VueloEspecial("WA15", "Madrid", "Nueva York", 100, "Vacaciones")
vuelo_especial2 = VueloEspecial("AW", "Barcelona", "Roma", 150, "Trabajo")

vuelo1.agregar_pasajero("Juan")
vuelo1.agregar_pasajero("María")
vuelo1.agregar_pasajero("Pedro")
vuelo1.agregar_pasajero("Ana")

print(vuelo1.verificar_disponibilidad())
print(vuelo2.verificar_disponibilidad())

print(vuelo_especial1.verificar_disponibilidad())
print(vuelo_especial2.verificar_disponibilidad())

