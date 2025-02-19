import json

#pedir el numero favorito
#guardar el numero favorito en un archivo
#comprobar si tenemos guardado el numero favorito
#imprimir el numero favorito

def comprobar_num_fav():
    """ Comprobar si existe un número favorito guardado en un archivo JSON 
    y devolverlo si es así. """
    try:
        with open("numero_fav.json", "r") as file:
            num_fav = json.load(file)
            return num_fav
    except FileNotFoundError:
        return None

def guardar_numer_fav(numero_favorito):
    """ Guarda el número favorito en un archivo JSON """
    try:
        #abrimos archivo en modo escritura
        with open("numero_fav.json", "w") as file:
            #Guardar el número favorito en un archivo
            json.dump(numero_favorito, file)
    except Exception as e:
        print(f"Error al guardar el número favorito: {e}")

def preguntar_numero_fav():
    """ Pide al usuario que ingrese su número favorito y lo guarda en un archivo """

    # Pedir al usuario que ingrese su número favorito
    numero_favorito = int(input("Ingrese su número favorito: "))
    # Guardar el número favorito en un archivo
    guardar_numer_fav(numero_favorito)
    return numero_favorito
    print("Número favorito guardado con éxito.")

def print_num_fav():
    print(f"Tu número favorito es: {comprobar_num_fav()}")


# Programa principal
numero_favorito = comprobar_num_fav()

if numero_favorito:
    print_num_fav(numero_favorito)
else:
    numero_favorito = preguntar_numero_fav()
    print_num_fav(numero_favorito)