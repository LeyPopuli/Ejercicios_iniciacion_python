'''EJERCICIO 3: Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de 
letras que tienen el nombre.'''

user_name = input("Inserta un nombre de usuario:")

print("El nombre {} tiene {} letras".format(user_name.upper(), len(user_name)))