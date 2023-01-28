'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre 
por pantalla el número de veces que aparece la letra en la frase.
'''
frase = input("Inserta una frase:")
letra = input("Inserta una letra:")
veces = 0

for i in frase:
    if i == letra:
        veces += 1

print(veces)    