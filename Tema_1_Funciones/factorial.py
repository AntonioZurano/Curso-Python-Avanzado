'''
Implementa una función recursiva llamada factorial que calcule el factorial de 
un número entero positivo. El factorial de un número n se define como el 
producto de todos los números enteros positivos desde 1 hasta n. '''


def factorial(n):
    """Calcula el factorial de un número entero positivo n."""
    #Parámetros:
    #    n: Es un número entero positivo.
    #Devuelve:
    #    El factorial de n."""
    
    if n < 0:
        return "Error: el número debe ser positivo"
    #Planteamos el caso base
    if n == 0 or n == 1:
        return 1
    #Planteamos la sentencia recursiva
    return n * factorial(n-1)

# caso de uso (Test)    
print(factorial(5)) # 120