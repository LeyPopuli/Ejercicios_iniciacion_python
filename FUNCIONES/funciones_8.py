'''Escribir una función que reciba una muestra de números en una lista y 
devuelva un diccionario con su media, varianza y desviación típica.'''

def media(muestra):
    return sum(muestra) / len(muestra)

def desviacion_tipica(muestra):
    suma = 0
    for n in muestra:
        tmp = (n - media(muestra))**2
        suma += tmp
    return (suma / len(muestra))**0.5    

def varianza(muestra):
    return desviacion_tipica(muestra) ** 2

def diccionario_estadisticos(muestra):
    diccionario = {}
    diccionario["media"] = media(muestra)
    diccionario["desviacion típica"] = desviacion_tipica(muestra)
    diccionario["varianza"] = varianza(muestra)
    return print(diccionario)

diccionario_estadisticos(([1, 2, 3, 4, 5]))
