'''Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.'''

def cuadrados(muestra):
    lista_cuadrados = []
    for numero in muestra:
        numero_cuadrado = numero**2
        lista_cuadrados.append(numero_cuadrado)
    return lista_cuadrados

print(cuadrados([1,2,5,6,4,8,2]))        