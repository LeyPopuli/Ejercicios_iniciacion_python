'''Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario 
con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario 
para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.'''

diccionario = {}

traducciones = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par de palabra-traducción separados por comas:")

combo = traducciones.split(",")

for palabra in combo:
    traduccion = palabra.split(":")
    español = traduccion[0]
    ingles = traduccion[1]
    diccionario[español] = ingles

frase_input = input("Inserta una frase para traducir:")

frase = frase_input.split(" ")

frase_traducida = ""

for palabra in frase:
    if frase_traducida != "":
         frase_traducida += " "
    if palabra in diccionario.keys():
        frase_traducida += diccionario[palabra]
    else:
        frase_traducida += "*"
        
print("Traducción:", frase_traducida)


