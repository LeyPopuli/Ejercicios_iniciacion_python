'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
número de veces que contiene cada vocal.'''

vocales = list("aeiou")
palabra = input("Inserta una palabra:")
palabra = palabra.lower()
vocales_detectadas = []

for letra in palabra:
    if letra in vocales:
        if letra not in vocales_detectadas:
            vocales_detectadas.append(letra)
        else:
            pass        
    else:
        pass

print(vocales_detectadas)

for vocal in vocales:
    recuento = palabra.count(vocal)
    print(vocal, "x", recuento, "veces")

