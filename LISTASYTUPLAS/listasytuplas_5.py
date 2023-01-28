''''Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.'''

lista = list(range(1,10 + 1))

lista = sorted(lista, reverse=True)

print(lista)