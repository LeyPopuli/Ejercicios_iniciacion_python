'''EJERCICIO 10: Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta.'''

compra = input("Introduce los productos que desees comprar separados por ',':")

compra = compra.replace(" ", "")

print(compra.replace(",", "\n"))