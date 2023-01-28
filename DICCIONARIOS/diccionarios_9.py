'''Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de 
factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir 
una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará 
por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará 
por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por 
pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''

facturas ={}

pregunta_inicial = input("Si desea añadir una nueva factura pulse '1', para pagar una existente pulse '2' y para terminar pulse '3':")

clave_factura = ""
coste_factura = 0
total_saldado = 0

while pregunta_inicial != "":    
    if pregunta_inicial == '1':
        clave_factura = input("Inserte el número de factura:")
        coste_factura = float(input("Inserte el coste de la factura:"))
        facturas[clave_factura] = coste_factura
        pendiente_saldar = sum(facturas.values())
        print("La cantidad saldada asciende a:", total_saldado)
        print("Pendiente de saldar:", pendiente_saldar)
        pregunta_inicial = input("Si desea añadir una nueva factura pulse '1', para pagar una existente pulse '2' y para terminar pulse '3':")       
    elif pregunta_inicial == '2':
        clave_factura = input("Inserte el número de la factura que desee saldar:")
        facturas.pop(clave_factura)
        total_saldado += coste_factura
        pendiente_saldar = sum(facturas.values())
        print("La cantidad saldada asciende a:", total_saldado)
        print("Pendiente de saldar:", pendiente_saldar)
        pregunta_inicial = input("Si desea añadir una nueva factura pulse '1', para pagar una existente pulse '2' y para terminar pulse '3':")
    elif pregunta_inicial == '3':
        pendiente_saldar = sum(facturas.values())   
        print("La cantidad saldada asciende a:", total_saldado)
        print("Pendiente de saldar:", pendiente_saldar)
        break
    else: 
        print("ERROR, CÓDIGO NO VÁLIDO") 
        break
     

   

