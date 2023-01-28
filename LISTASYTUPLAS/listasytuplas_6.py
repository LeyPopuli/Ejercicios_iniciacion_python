'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura
y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas 
que el usuario tiene que repetir.'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
asignaturas_aprobadas = []

for asignatura in asignaturas:
    nota = int(input("Inserta la nota correspondiente a la asignatura " + asignatura +":"))
    notas.append(nota)

for i in range(len(notas)):
    if notas[i]>=5:
        asignaturas_aprobadas.append(asignaturas[i])

for asignatura_aprobada in asignaturas_aprobadas:
   asignaturas.remove(asignatura_aprobada)   

print(asignaturas)       








       
