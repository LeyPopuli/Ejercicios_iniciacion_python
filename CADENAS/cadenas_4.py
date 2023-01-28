'''EJERCICIO 4: Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el 
código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte 
por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.'''

numero_telefono = input("Inserta el número de tEsto es una prueba.Esto es una prueba.eléfono en formato +prefijo-número-extension:")

print("{}".format(numero_telefono[4 : -3]))