'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''

cantidad_invertir = float(input("Inserta la cantidad que deseas invertir:"))
interes_anual = float(input("Inserta el interés anual:"))
numero_años = int(input("Inserta el número de años:"))

for i in range(numero_años):
    cantidad_invertir *= 1 + (interes_anual / 100)
    print(round(cantidad_invertir,2))