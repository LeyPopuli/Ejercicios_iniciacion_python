'''Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y 
muestre por pantalla su media y desviación típica.'''

lista_numeros = []

numeros = input("Inserta un número o 'exit' para terminar:")

while numeros != "exit":
    numeros = float(numeros)
    lista_numeros.append(numeros)
    numeros = input("Inserta un número o vacío para terminar:")

sumatorio = 0
for numeros in lista_numeros:
    sumatorio += numeros
media = sumatorio / len(lista_numeros)

dt_sumatorio = 0

for numero in lista_numeros:
    dt_numero = (numero - media)**2
    dt_sumatorio += dt_numero

dt_total = (dt_sumatorio / len(lista_numeros))**0.5 

print("La media es:", media)
print("La desviación típica es:", round(dt_total, 2))



