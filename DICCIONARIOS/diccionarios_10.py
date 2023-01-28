'''Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se 
guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario 
con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor 
True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente 
menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar 
clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

1.Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3.Preguntar por el NIF del cliente y mostrar sus datos.
4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6.Terminar el programa.'''

bbdd_clientes = {}

nif_cliente = "nif"
nombre = "nombre"
direccion = "direccion"
telefono = "telefono"
correo = "correo"
preferente = "preferente"
operacion = "operacion"


while operacion != "":
    operacion = input("Inserta el código de la operación que desees realizar (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar:")   
    if operacion == "1": #OK
        nif_cliente = input("Inserta el NIF del cliente:")
        bbdd_clientes[nif_cliente]= {}
        bbdd_clientes[nif_cliente][nombre] = input("Inserta el nombre del cliente:")
        bbdd_clientes[nif_cliente][direccion] = input("Inserta la dirección del cliente:")
        bbdd_clientes[nif_cliente][telefono] = input("Inserta el teléfono del cliente:")
        bbdd_clientes[nif_cliente][correo] = input("Inserta el correo electrónico del cliente:")
        bbdd_clientes[nif_cliente][preferente] = bool(input("¿Se trata de un cliente preferente? (Vacío si NO es preferente):"))
    elif operacion == "2": #OK
        nif_cliente = input("Inserta el NIF del cliente:")
        bbdd_clientes.pop(nif_cliente)
    elif operacion == "3": #OK
        nif_cliente = input("Inserta el NIF del cliente:")
        print(bbdd_clientes[nif_cliente])
    elif operacion == "4": #NOK
        for nif_cliente in bbdd_clientes.keys():
            print(nif_cliente, bbdd_clientes[nif_cliente][nombre])
    elif operacion == "5":
        for nif_cliente in bbdd_clientes.keys():
            if bbdd_clientes[nif_cliente][preferente] == True:
                print(nif_cliente, bbdd_clientes[nif_cliente][nombre])
    elif operacion == "6":
        print("Se ha finalizado el programa.")            
        break


                


