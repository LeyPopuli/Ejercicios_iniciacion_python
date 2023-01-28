'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''

numero_ganador = []
for i in range(6):
    numero_ganador.append(int(input("Introduce un número ganador: ")))
numero_ganador.sort()
print("Los números ganadores son " + str(numero_ganador))