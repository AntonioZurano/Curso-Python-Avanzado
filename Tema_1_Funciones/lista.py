'''
Crea una función recursiva llamada suma_lista que calcule la suma de todos 
los elementos de una lista de enteros. Puedes asumir que la lista no está 
vacía.'''

def suma_lista(lista):
    """Calcula la suma de todos los elementos de una lista de enteros."""
    # Parámetros:
    #    lista: Es una lista de numeros enteros.
    # Devuelve:
    #    La suma de todos los elementos de la lista."""
    
    #Planteamos el caso base
    if len(lista) == 1:
        return lista[0]
    #Planteamos la sentencia recursiva
    return lista[0] + suma_lista(lista[1:])

# caso de uso (Test)
print(suma_lista([1, 2, 3, 4, 5])) # 15
'''
1 + suma_lista([2, 3, 4, 5])
1 + 2 + suma_lista([3, 4, 5])
1 + 2 + 3 + suma_lista([4, 5])
1 + 2 + 3 + 4 + suma_lista([5])
1 + 2 + 3 + 4 + 5
'''