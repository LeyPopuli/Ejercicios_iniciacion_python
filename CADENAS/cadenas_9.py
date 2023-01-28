'''EJERCICIO 9:Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.'''

fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato'dd/mm/aaaa': ")

dia = fecha_nacimiento[:fecha_nacimiento.find("/")]
mesyaño = fecha_nacimiento[fecha_nacimiento.find("/") + 1 :]
mes = mesyaño [:mesyaño.find("/")]
año = mesyaño[mesyaño.find("/") + 1 :]

print(dia, mes, año)