'''Escribir una función que reciba una frase y devuelva un diccionario con las 
palabras que contiene y su longitud.'''

def longitud_palabras(frase):
    diccionario = {}
    lista_frase = frase.split()
    for palabra in lista_frase:
        diccionario[palabra] = len(palabra)
    return diccionario

print(longitud_palabras("Esto es una frase de prueba"))   

def length_words(sentence):
    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(length_words('Welcome to Python'))