'''
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una 
estructura de datos adecuada para almacenar la información de las ventas 
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para 
agregar el producto vendido con su precio y otro para mostrar las ventas de 
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: 
precio1}, {“Producto”: producto2, “Precio”: precio2}...])'''

# Definir la función agregar_venta
def agregar_venta(ventas, producto, precio):
    ''' Esta función agrega un producto vendido con su precio a la lista de ventas.'''
    # PARAMETROS
    # ventas: lista de diccionarios
    # Producto: str nombre del producto vendido
    # Precio: float precio del producto vendido
    # RETORNO
    # None
    
    # Crear un diccionario con el producto y el precio
    venta = {"Producto": producto, "Precio": precio}
    
    # Agregar el diccionario a la lista de ventas
    ventas.append(venta)


# Definir la función mostrar_ventas
def mostrar_ventas(ventas):
    ''' Esta función muestra las ventas de productos con sus respectivos precios.'''
    # PARAMETROS
    # ventas: lista de diccionarios
    # RETORNO
    # None
    
    # Iterar sobre la lista de ventas
    for venta in ventas:
        print(f"Producto: {venta['Producto']}, Precio: {venta['Precio']}")
        print("-------------------------")

# Inicializar la lista de ventas
# Nuestra estructura de datos sera una lista de diccionarios
# Cada diccionario tendra la forma {"Producto": producto, "Precio": precio}
# Ejemplo: [{"Producto": "Camisa", "Precio": 20.0}, {"Producto": "Pantalón", "Precio": 30.0}]

ventas = []

# 
# # Agregar ventas
agregar_venta(ventas, "Camisa", 20.0)
agregar_venta(ventas, "Pantalón", 30.0)
agregar_venta(ventas, "Zapatos", 40.0)
#   
# # Mostrar ventas
mostrar_ventas(ventas)
# 
# # Resultado esperado
# # Producto: Camisa, Precio: 20.0
# # Producto: Pantalón, Precio: 30.0
# # Producto: Zapatos, Precio: 40.0
# 
     