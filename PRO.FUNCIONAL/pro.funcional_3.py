'''Escribir una función que reciba otra función booleana y una lista, y 
devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.
'''

contraseña = ""

def es_segura(contraseña):
    return len(contraseña) > 5

print(es_segura("Alohomora"))

lista_resultados = []

def comprobar_contraseñas(funcion,lista):
    for contraseña in lista:
        if funcion(contraseña):
            lista_resultados.append(contraseña)
    return lista_resultados

print(comprobar_contraseñas(es_segura,["Alohomora", "Prueba", "No", "Casi", "Estasí"]))        
   