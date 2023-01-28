'''Escribir un programa que reciba una cadena de caracteres y devuelva 
un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia.'''

def frecuencia_palabras(frase):
    lista_frase = frase.split()
    palabras = {}
    for i in lista_frase:
        if i in palabras:
            palabras[i] += 1
        else:    
            palabras[i] = 1     
    return palabras

def palabra_mas_repetida(palabras):
    max_palabra = ""
    max_frecuencia = 0
    for palabra, frecuencia in palabras.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia        


frase = "Hola mundo mundo"

print(frecuencia_palabras(frase))    
print(palabra_mas_repetida(frecuencia_palabras(frase)))