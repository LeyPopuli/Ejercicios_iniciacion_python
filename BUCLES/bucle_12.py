'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el 
usuario escriba “salir” que terminará.'''

eco = input("Inserta la frase/palabra a repetir, o escribe 'salir' para cerrar:")

while eco != "salir":
    print(eco)
    eco = input("Inserta la frase/palabra a repetir, o escribe 'salir' para cerrar:")

