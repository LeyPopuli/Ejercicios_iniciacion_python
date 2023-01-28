'''EJERCICIO 5: Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que tributar o no.'''

edad_minima = 16
ingresos_minimos = 1000

edad = int(input("Inserta tu edad:"))
ingresos_menusales = float((input("Inserta tus ingresos mensuales:")))

if edad > edad_minima and ingresos_menusales >= ingresos_minimos:
    print("Debe tributar")
else:
    print("No tributa")




