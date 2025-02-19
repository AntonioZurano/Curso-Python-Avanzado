# leer el archivo pi_1000.txt
# guardar el contenido --> .read
# buscar un string dentro de pi --> .find()

def buscar_en_pi(filename, string):
    """ Busca la fecha de nacimiento dentro de los primeros 10000 decimales de pi """
    try:
        with open(filename, "r") as file:
            digitos = file.read()
            posicion = digitos.find(string)
            
            if posicion == -1:
                return None  # Indicar que no se encontró la cadena
            return posicion  # Devolver la posición si se encuentra
        
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encuentra disponible.")
        return -2  # Código de error para archivo no encontrado
    except Exception as e:
        print(f"Error inesperado: {e}")
        return -3  # Código de error para cualquier otro problema


# Llamamos a la función buscar_en_pi
resultado = buscar_en_pi("pi_10000.txt", "1782")

if resultado is None:
    print("La fecha de nacimiento no se encuentra en los primeros 10000 decimales de pi.")
elif resultado == -2:
    print("No se pudo abrir el archivo, verifique que existe y el nombre es correcto.")
elif resultado == -3:
    print("Ocurrió un error inesperado durante la ejecución.")
else:
    print(f"La fecha de nacimiento se encuentra en la posición {resultado} de los primeros 10000 decimales de pi.")

