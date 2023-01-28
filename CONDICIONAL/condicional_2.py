'''EJERCICIO 2: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

contraseña = str.lower(input("Escribe una contraseña:"))
repite_contraseña =  str.lower(input("Repite la contraseña:"))


if contraseña == repite_contraseña:
    print("Las contraseñas coinciden.")
else:
    print("Las contraseñas no coinciden.")    