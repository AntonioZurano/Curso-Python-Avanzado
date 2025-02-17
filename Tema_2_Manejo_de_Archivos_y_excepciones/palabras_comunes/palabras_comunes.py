# Contar apariciones de una palabra en un texto de un archivo
# abrir el archivo de texto
# leer el contenido del archivo, guardarlo en una variable
# contar las apariciones de la palabra en el texto

def contar_apariciones(filename, palabra):
    """ Contar las apariciones de una palabra 
        en un archivo de texto """
    try:
        with open(filename, "r") as file:
            # guardamos el contenido del archivo en una variable
            texto = file.read()
            # contamos el numero de apariciones de la palabra
            count = texto.count(palabra)
            return count
    except FileNotFoundError:
        print(f"El archivo {filename} no se encuentra disponible.")
        return 0
    except:
        return 0
    

    # Ejemplo de uso
filename = "texto.txt"
palabra_contar = "Clara"
    
ocurrencias = contar_apariciones(filename, palabra_contar)
    
print(f"La palabra '{palabra_contar}' aparece {ocurrencias} veces en el archivo {filename}.")