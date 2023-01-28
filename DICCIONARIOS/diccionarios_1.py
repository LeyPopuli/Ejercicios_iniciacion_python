'''Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje 
de aviso si la divisa no está en el diccionario.'''

divisas = {'euro':'€', 'dollar':'$', 'yen':'¥'}

print("Divisas disponibles:", divisas)
divisa_seleccionada = input("Selecciona una divisa:")
divisa_seleccionada = str.lower(divisa_seleccionada)

if divisa_seleccionada in divisas:
    print(divisas[divisa_seleccionada])
else:
    print("AVISO: Divisa no disponible")
