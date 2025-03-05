'''TIENDA ONLINE
Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Tienda:
    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto):
        self.productos.append(producto) 

    def mostrar_inventario(self):
        print("Inventario:")
        for producto in self.productos:
            print(f"{producto.nombre} - Precio: {producto.precio} EU - Stock: {producto.stock}")

    def comprar_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Compra realizada: {cantidad} unidades de {nombre}")
                else:
                    print(f"No hay suficiente stock de {nombre}")
                return
        print(f"Producto no encontrado: {nombre}")

# Ejemplo de uso
tienda = Tienda()
producto1=Producto("Camiseta", 20, 100)
producto2=Producto("Pantalón", 40, 50)
producto3=Producto("Zapatillas", 60, 30)
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.mostrar_inventario()
tienda.comprar_producto("Camiseta", 10)
tienda.comprar_producto("Pantalón", 60)
tienda.comprar_producto("Zapatos", 10)
tienda.mostrar_inventario()