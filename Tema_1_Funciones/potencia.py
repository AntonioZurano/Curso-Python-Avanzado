'''Implementa una función recursiva llamada potencia que calcule el resultado 
de elevar un número a una potencia dada. Puedes asumir que tanto el 
número como la potencia son enteros no negativos.'''

def potencia(base, exponente):
    """Calcula el resultado de elevar un número a una potencia dada."""
    # Parámetros:
    #    base: Es un número entero positivo.
    #    exponente: Es un número entero positivo.
    # Devuelve:
    #    El resultado de elevar base a la potencia exponente."""
    
    if base < 0 or exponente < 0:
        return "Error: los números deben ser positivos"
    #Planteamos el caso base
    if exponente == 0:
        return 1
    #Planteamos la sentencia recursiva
    return base * potencia(base, exponente-1)

# caso de uso (Test)
print(potencia(10, 2)) # 100

"""
10 * potencia(10, 1) 
10 * 10  * potencia(10, 0)
10 * 10 * 1
"""