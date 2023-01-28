'''EJERCICIO 7: Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el 
mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.'''

correo_e = input("Escribe tu correo electrónico:")
arroba = '@'
indice_arroba = int(correo_e.index(arroba))

print(correo_e[:indice_arroba] + "ceu.es")