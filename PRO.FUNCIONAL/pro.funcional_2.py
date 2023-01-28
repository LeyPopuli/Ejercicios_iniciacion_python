'''Escribir una función que reciba otra función y una lista, y devuelva
 otra lista con el resultado de aplicar la función dada a cada uno de los elementos 
 de la lista.'''

def cuadrado(numero):
    return numero * numero

resultados = []

def lista(funcion, lista):
    for i in lista:
        resultados.append(funcion(i))
    return resultados

print(lista(cuadrado,[1, 2, 3, 4]))    


