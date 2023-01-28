'''EJERCICIO 11: Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades 
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

nombre_producto = input("Nombre del producto:")
precio_producto = float(input("Precio del producto por unidad:"))
unidades_producto = int(input("Número de unidades del producto:"))

print("El producto '{nombre_producto}' tiene un coste/unidad de {precio_producto:6.2f}€ y se han informado de {unidades_producto:3d} unidades. El coste total asciende a {total:8.2f}€.".format(nombre_producto = nombre_producto, 
precio_producto = precio_producto, unidades_producto = unidades_producto, total = precio_producto * unidades_producto))
