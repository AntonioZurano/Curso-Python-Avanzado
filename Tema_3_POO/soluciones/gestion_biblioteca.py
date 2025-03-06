'''SISTEMA DE GESTION DE BIBLIOTECA
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:

1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.

2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.

3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.'''

class Libro:
    def __init__(self, titulo, autor, ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.ejemplares_disponibles > 0:
                    libro.ejemplares_disponibles -= 1
                    usuario.libros_prestados.append(libro)
                    print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
                else:
                    print(f"Lo siento, no hay ejemplares disponibles del libro '{libro.titulo}'.")
                return

    def devolver_libro(self, usuario, titulo):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                libro.ejemplares_disponibles += 1
                usuario.libros_prestados.remove(libro)
                print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
                return
        print(f"Lo siento, el usuario {usuario.nombre} no tiene prestado el libro '{titulo}'.")

    def mostrar_inventario(self):
        print("Inventario de la biblioteca:")
        for libro in self.libros:
            print(f"- '{libro.titulo}' por {libro.autor} ({libro.ejemplares_disponibles} ejemplares disponibles)")

# Ejemplo de uso
biblioteca = Biblioteca()
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 3)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 2)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_inventario()

usuario1 = Usuario("Alice", 12345)
usuario2 = Usuario("Bob", 54321)

biblioteca.prestar_libro(usuario1, "El Señor de los Anillos")  # El libro 'El Señor de los Anillos' ha sido prestado a Alice.
biblioteca.prestar_libro(usuario2, "El Señor de los Anillos")  # Lo siento, no hay ejemplares disponibles del libro 'El Señor de los Anillos'.

biblioteca.prestar_libro(usuario2, "Cien años de soledad")  # El libro 'Cien años de soledad' ha sido prestado a Bob.
biblioteca.mostrar_inventario()
# Inventario de la biblioteca:
# - 'El Señor de los Anillos' por J.R.R. Tolkien (2 ejemplares disponibles)     
# - 'Cien años de soledad' por Gabriel García Márquez (1 ejemplares disponibles)

biblioteca.devolver_libro(usuario1, "El Señor de los Anillos")  # El libro 'El Señor de los Anillos' ha sido devuelto por Alice.
biblioteca.mostrar_inventario()
# Inventario de la biblioteca:
# - 'El Señor de los Anillos' por J.R.R. Tolkien (3 ejemplares disponibles)
# - 'Cien años de soledad' por Gabriel García Márquez (1 ejemplares disponibles)
#
biblioteca.devolver_libro(usuario1, "El Señor de los Anillos")  # Lo siento, el usuario Alice no tiene prestado el libro 'El Señor de los Anillos'.
biblioteca.prestar_libro(usuario1, "El Señor de los Anillos")  # El libro 'El Señor de los Anillos' ha sido prestado a Alice.
biblioteca.mostrar_inventario()
# Inventario de la biblioteca:
# - 'El Señor de los Anillos' por J.R.R. Tolkien (2 ejemplares disponibles)
# - 'Cien años de soledad' por Gabriel García Márquez (1 ejemplares disponibles)
#