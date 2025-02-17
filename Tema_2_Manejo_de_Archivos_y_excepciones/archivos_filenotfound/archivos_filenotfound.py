# Comprobar que nuestros archivos estan disponibles
# Si lo estan imprimimos el contenido de los archivos


filenames = ["gatos.txt", "perros.txt"]

for filename in filenames:
    try:    
        with open(filename, "r") as file:
            print(f"Contenido del {filename}:")
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {filename} no se encuentra disponible.")
        print("\n")
    # cualquier otro error que no sea FileNotFoundError
    except:  
        pass
    # otra forma de manejar el error
    #    print(f"El archivo {filename} no se encuentra disponible.")
    #    print("\n")

print("Proceso terminado")