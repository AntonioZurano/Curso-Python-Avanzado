import random
import string

def generar_contrasena_segura(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, 
                                incluir_caracteres_especiales=True):
    """ Esta función genera una contraseña segura dada una longitud."""
    # longitud: numero de caracteres de la contraseña
    # incluir_mayusculas: si se incluyen letras mayúsculas
    # incluir_minusculas: si se incluyen letras minúsculas
    # incluir_numeros: si se incluyen números
    # incluir_caracteres_especiales: si se incluyen caracteres
    # especiales

    caracteres = ""

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase

    if incluir_minusculas:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de caracter para generar la contraseña")

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena
    