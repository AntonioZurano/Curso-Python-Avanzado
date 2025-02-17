# leer el archivo pi_1000.txt
# guardar el contenido --> .read
# buscar un string dentro de pi --> .find()

def buscar_en_pi(filename, string):
    """ Busca la fecha de nacimiento dentro de los primeros 1000 decimales de pi """
    try:
        # abrimos el archivo en modo lectura
        with open(filename, "r") as file:
            # guardamos el contenido del archivo en una variable
            digitos = file.read()
            # buscamos el string en los primeros 1000 decimales de pi
            posicion = digitos.find(string)
            return posicion
        # si hay un error al abrir el archivo
    except FileNotFoundError:
        print(f"El archivo {filename} no se encuentra disponible.")
        return -1
    except:
        return -1


# llamamos a la función buscar_en_pi
resultado = buscar_en_pi("pi_1000.txt", "1997")
# si la función retorna -1, no se encontró la fecha de nacimiento
if resultado == -1:
    print("La fecha de nacimiento no se encuentra en los primeros 10000 decimales de pi.")
# si la función retorna un número distinto de -1, se encontró la fecha de nacimiento
else:
    print(f"La fecha de nacimiento se encuentra en la posición {resultado} de los primeros 1000 decimales de pi.")

