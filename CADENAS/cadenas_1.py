'''EJERCICIO 1: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.'''

nombre = input("Inserta tu nombre:")
numero = input("Inserta un número entero:")

numero = int(numero)

print((nombre + "/n") * numero)