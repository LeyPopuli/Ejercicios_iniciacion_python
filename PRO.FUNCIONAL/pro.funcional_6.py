'''Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro 
diccionario con las asignaturas en mayúsculas y 
las calificaciones correspondientes a las notas.'''

diccionario_notas = {"Matemáticas": 4, "Lengua": 10, "E.f.": 6, "Naturales": 7, "Inglés": 8}

def transf_calificacion(diccionario):
    diccionario_calificaciones = {}
    for item in diccionario:
        score = diccionario.get(item)
        if score < 5:
            result = 'SS'
        elif score < 7:
            result = 'AP'
        elif score < 9:
            result = 'NT'
        elif score < 10:
            result = 'SB'
        else:
            result = 'MH'
        diccionario_calificaciones[item] = result
    return diccionario_calificaciones

def calificaciones(diccionario):
    diccionario_callificaciones = {}
    for clave, valor in diccionario.items():
        clave_mayuscula = str.upper(clave)
        diccionario_callificaciones[clave_mayuscula] = valor
    return diccionario_callificaciones

print(calificaciones(transf_calificacion(diccionario_notas)))


       


