'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''

multiplo = int(input("Inserta un número entero como múltiplo:"))

for i in range(1,(10+1)):
    print(i, "x", multiplo, "=", i*multiplo)