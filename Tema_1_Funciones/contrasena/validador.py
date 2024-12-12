

def validar_contrasena(contrasena):
    """ Esta función valida la contraseña dada como argumento.
    Valida si la contraseña cumple con los siguientes requisitos:
    - Al menos 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un caracter especial
    """

    longitud_minima = 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    # Al menos 8 caracteres
    if len(contrasena) < longitud_minima:
        return False

    # Al menos una letra mayúscula, una letra minúscula, un número y un caracter especial
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():    
            tiene_numero = True
        elif caracter in "!@#$%^&*()-+":
            tiene_caracter_especial = True

    # devolveremos True si todos los requisitos se cumplen
    # de lo contrario, devolveremos False
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial