
# solicitar una contraseña al usuario y verificar si es correcta
# validar la contraseña
## contraseña no valida --> sugerir nueva contraseña

#importamos los módulos
import validador
import generador

def solicitar_contrasena():
    contrasena = input("Ingrese su contraseña: ")
    valida = validador.validar_contrasena(contrasena)

    if valida:
        print("Contraseña segura")
    else:
        print("Contraseña no es segura. Se sugiere una nueva contraseña")
        sugerencia = generador.generar_contrasena_segura(9)
        print(f"Su nueva contraseña sugerida es: {sugerencia}")

# Ejemplo de uso
solicitar_contrasena()

