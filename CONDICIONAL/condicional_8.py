'''En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 
0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una 
tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es 
de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de 
rendimiento, así como la cantidad de dinero que recibirá el usuario.'''

puntuacion_obtenida = float(input("Inserta la puntuación obtenida:"))
base = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntuaciones_validas = [inaceptable,aceptable,meritorio]

if puntuacion_obtenida in puntuaciones_validas or puntuacion_obtenida > meritorio:
    if puntuacion_obtenida == inaceptable:
        nivel = "Inaceptable"
    elif puntuacion_obtenida == aceptable:
        nivel = "Aceptable"
    elif puntuacion_obtenida >= meritorio:
        nivel = "Meritorio"
    print("Has obtenido un nivel", nivel,". Recibirás", base * puntuacion_obtenida,"€.")

else:
    print("Error, introduce un valor válido")
   

