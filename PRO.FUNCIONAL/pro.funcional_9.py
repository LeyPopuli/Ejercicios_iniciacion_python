'''Escribir una función que reciba una muestra de números y devuelva los valores atípicos, 
es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación 
típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.'''

muestra_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]
 

def media(muestra):
    return sum(muestra) / len(muestra)

def desviacion_tipica(muestra):
    suma = 0
    for n in muestra:
        tmp = (n - media(muestra))**2
        suma += tmp
    return (suma / len(muestra))**0.5

lista_atipicos = []    

def es_atipico(item, muestra):
    resultado = (item - media(muestra)) / desviacion_tipica(muestra) 
    return (resultado > 3) or (resultado < -3)

def deteccion_atipicos(muestra):
    for item in muestra:       
        if es_atipico(item, muestra):
            lista_atipicos.append(item)
    return lista_atipicos

print(deteccion_atipicos(muestra_numeros))            
