'''EJERCICIO 6: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde.'''

sexo = str.upper(input("Inserta si tu sexo es hombre(H) o mujer(M):"))
nombre = str.capitalize(input("Ingresa tu nombre:"))
letras_hastam = list("A,B,C,D,E,F,G,H,I,J,K,L")

if (sexo == "M" and nombre[0] in letras_hastam) or (sexo =="H" and nombre[0] not in letras_hastam) :
    print("Pertenes al grupo A")
else:
    print("Pertenes al grupo B")   


