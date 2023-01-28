'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le 
pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''

diccionario = {}
   
clave = input("¿Qué elemento quieres introducir? ('Exit' para salir):")

while not (clave == "Exit" or clave == "exit"):
    valor = input("Inserta el valor del elemento ('Exit' para salir):")
    diccionario[clave] = valor
    print(diccionario)
    clave = input("¿Qué elemento quieres introducir? ('Exit' para salir):")

    print(diccionario)    





