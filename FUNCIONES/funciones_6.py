'''Escribir una función que reciba una muestra de números en una lista y devuelva su media.'''

def media(*numeros):
    tmp = 0
    for n in numeros:
        tmp += n 
    return tmp / len(numeros)
        

print(media(3,5,7,8,9))  
 

def media2(muestra):
    return sum(muestra) / len(muestra)

print(media2([3,5,7,8,9]))      