'''Escribir una función reciba una lista de notas y devuelva la
 lista de calificaciones correspondientes a esas notas.'''

diccionario = {"A":10,"B":8,"C": 5,"D":3}

def calificaciones(lista_notas):
    lista_calificaciones = []
    for nota in lista_notas:
        if nota in diccionario.keys():
            lista_calificaciones.append(diccionario[nota])
        else:
            pass
    return lista_calificaciones

print(calificaciones(["B","A","C","A","B"]))       

