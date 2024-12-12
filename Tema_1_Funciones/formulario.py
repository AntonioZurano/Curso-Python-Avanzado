'''Crea un programa que valide un formulario de registro. Crea una función 
llamada validar_formulario que reciba diferentes campos de un formulario 
(nombre, correo electrónico y número de teléfono) y verifique si los valores 
ingresados cumplen con los requisitos especificados, siendo estos: 
1. Que el nombre tenga una longitud minima de 3 caracteres 
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 
caracteres 
3. Que el email contenga un “@“ y un “.”'''

# Definir la función validar formularios
def validar_formulario(nombre, email, telefono):
    ''' Esta funcion valida si los datos ingresados en el formulario tienen 
    el formato correcto.'''
    # PARAMETROS
    # nombre: str
    # email: str
    # telefono: str de longitud 9
    # RETORNO
    # bool
    
    # Verificar si el nombre tiene una longitud mínima de 3 caracteres
    # Verificar si el teléfono está conformado por dígitos y tiene una longitud de 9 caracteres
    # Verificar si el email contiene un "@" y un "."
    if len(nombre) >= 3 and telefono.isdigit() and len(telefono) == 9 and "@" in email and "." in email:
        return True
    else:
        return False
    
# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
email = input("Ingrese su email: ")
telefono = input("Ingrese su teléfono: ")

#Realizar la validación
## Si la función retorna True, el formulario es válido
## Si la función retorna False, el formulario es inválido
valido=validar_formulario(nombre, email, telefono)

# Comprobamos el resultado de la validacion
if valido:
    print("Formulario válido")
else:
    print("Formulario inválido")


    