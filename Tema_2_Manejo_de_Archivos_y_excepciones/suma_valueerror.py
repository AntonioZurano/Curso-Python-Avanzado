'''
Un problema común al solicitar una entrada numérica ocurre cuando las personas ingresan texto en lugar de números. 
Cuando intentas convertir la entrada a un entero (int), obtendrás un ValueError. Escribe un programa que solicite dos
números. Suma los números y muestra el resultado. Captura el ValueError si alguno de los valores de entrada no es un 
número e imprime un mensaje de error amigable. Prueba tu programa ingresando dos números y luego ingresando texto en 
lugar de un número. Envuelve tu código del en un bucle while para que el usuario pueda continuar 
ingresando números incluso si comete un error ingresando texto en lugar de un número.'''

# envolver en bucle while infinito - break
# pedir dos numeros al usuario
# controlas el error: string en vez de int
# sumar los dos numeros

while True:

    # Comprobamos que los numeros ingresados sean enteros
    try:
        # pedimos los numeros por pantalla
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        # realizamos el resultado
        result = num1 + num2
        # indicamos por pantalla el resultado
        print(f"La suma de {num1} y {num2} es {result}")
        #interrumpimos el programa
        break
        # Si no son numeros enteros manejamos el error
    except ValueError:
        # imprimimos el mensaje de error personalizado
        print("Por favor, ingrese solo números enteros")
