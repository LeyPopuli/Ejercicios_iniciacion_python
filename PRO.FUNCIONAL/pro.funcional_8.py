'''Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los
inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben 
incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble 
se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5'''

lista_inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def calcular_precio(inmueble):
    precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + int(inmueble['garaje']) * 15000) * (1 - (2020 - inmueble['año']) / 100)
    if inmueble['zona'] == 'B':
        precio *= 1.5
    inmueble['precio'] = precio
    return inmueble  

presupuesto = float(input("Inserta un presupuesto:"))    
    
def buscar_inmueble(lista_inmuebles, presupuesto):
    def filtro(inmueble):
        return inmueble['precio'] <= presupuesto
    return list(filter(filtro,map(calcular_precio,lista_inmuebles)))

print(buscar_inmueble(lista_inmuebles, presupuesto))        
