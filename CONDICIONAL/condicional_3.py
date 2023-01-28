'''EJERCICIO 3: Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.'''

divisor1 = int(input("Inserta el primer número:"))
divisor2 = int(input("Inserta el segundo número:"))

if divisor2 == 0:
    print("Error")
else:
    print(divisor1 / divisor2)    