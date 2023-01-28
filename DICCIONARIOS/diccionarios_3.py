'''Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de 
kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70'''

frutas = {
'platano':1.35,
'manzana':0.80,
'pera':0.85,
'naranja':0.70
}

fruta_seleccionada = input("Inserta la fruta:")
fruta_seleccionada = str.lower(fruta_seleccionada)

if fruta_seleccionada in frutas:
    kilos_seleccionados = float(input("indica los kilos:"))
    print("El coste total de", fruta_seleccionada, "es", (round(kilos_seleccionados*frutas[fruta_seleccionada],2)), "€.")
else:
    print("Fruta no disponible")    

