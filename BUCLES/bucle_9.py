'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
contraseña = "Leyre"
valida_contraseña = input("Introduce la contraseña:")

while contraseña != valida_contraseña:
    valida_contraseña = input("Contraseña incorrecta. Introduce la contraseña:")

print("Contraseña correcta.")