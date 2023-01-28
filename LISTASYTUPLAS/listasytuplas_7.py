'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''

abecedario = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
abecedario_multiplos = []

for indice_letra in range(len(abecedario)):
    if (indice_letra + 1) % 3 == 0:
        abecedario_multiplos.append(abecedario[indice_letra])
    else:
        pass

for letra in abecedario_multiplos:
    abecedario.remove(letra)

print(abecedario)




