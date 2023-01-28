'''Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

def factorial(numero):
    ''' Funcion que devuelve el factorial de un número entero positivo'''
    tmp = 1
    for n in range (1, numero + 1):
        tmp *= n
    return tmp    

print(factorial(5))        