'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.'''

numero = int(input("Inserta un número entero positivo:"))

for i in range(1, numero + 1, 2): #SOLUCION 1
    print(i)


for i in range(1, numero + 1): #SOLUCION 2
    if i % 2 != 0:
        print(i)
