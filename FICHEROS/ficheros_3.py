'''Escribir una función que pida dos números n y m entre 1 y 10, lea 
el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por 
pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por 
pantalla informando de ello.'''

n = int(input("Introduce un número del 1 al 10:"))
m = int(input("Introduce la línea del fichero:"))

nombre_fichero = "tabla_multiplicar" + str(n) + ".txt"

try:
    with open(nombre_fichero, "r") as fichero:
        lineas = fichero.readlines()
    print(lineas[m-1])
except FileNotFoundError:
    print ("Fichero no encontrado")        
