'''
Crea una función recursiva llamada numero_triangular que calcule el n-ésimo 
número triangular. Un número triangular se obtiene al sumar todos los 
números naturales desde 1 hasta n. Por ejemplo, el número triangular de 4'''

def numero_triangular(n):
    """Calcula el n-ésimo número triangular."""
    #Parámetros:
    #    n: Es un número entero positivo.
    #Devuelve:
    #    El n-ésimo número triangular."""
    
    if n < 0:
        return "Error: el número debe ser positivo"
    #Planteamos el caso base
    if n == 0:
        return 0
    #Planteamos la sentencia recursiva
    return n + numero_triangular(n-1)

# caso de uso (Test)
print(numero_triangular(4)) # 10
'''
1 + numero_triangular(3)
1 + 2 + numero_triangular(2)
1 + 2 + 3 + numero_triangular(1)
1 + 2 + 3 + 4
'''
# caso de uso (Test)
print(numero_triangular(5)) # 15
'''
1 + numero_triangular(4)
1 + 2 + numero_triangular(3)
1 + 2 + 3 + numero_triangular(2)
1 + 2 + 3 + 4 + numero_triangular(1)
1 + 2 + 3 + 4 + 5
'''