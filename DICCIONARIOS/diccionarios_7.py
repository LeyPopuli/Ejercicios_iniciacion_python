'''Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
 el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe 
 mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato'''

compra = {}
   
clave = input("¿Qué artículo quieres introducir? ('Exit' para salir):")

while not (clave == "Exit" or clave == "exit"):
    valor = input("Inserta el precio del elemento ('Exit' para salir):")
    valor = float(valor)
    compra[clave] = valor
    clave = input("¿Qué artículo quieres introducir? ('Exit' para salir):")

print("Lista de la compra:")

total = sum(compra.values())

for clave in compra:
    print(clave, compra[clave])

print ("Total:", total)

