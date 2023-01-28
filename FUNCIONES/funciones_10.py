'''Escribir una función que convierta un número decimal en binario y otra que 
convierta un número binario en decimal.'''

lista_binaria = []

def numero_a_binario(numero):
    '''Convierte un número decimal en binario'''
    while numero != 0:
        digito_binario = numero % 2
        cociente = numero // 2
        lista_binaria.insert(0,digito_binario)       
        numero = cociente
    lista_string ="".join([str(_) for _ in lista_binaria]) #Convertimos la lista en cadena
    return lista_string

def binario_a_numero(numero_binario):
    '''Convierte un número binario en numero decimal'''
    numero_binario_string = str(numero_binario)
    numero_decimal = 0
    for posicion, digito_string in enumerate(numero_binario_string[::-1]):
        digito = int(digito_string)
        multiplicacion = digito * 2 ** posicion
        numero_decimal += multiplicacion
    return numero_decimal    

print(numero_a_binario(22))
print(binario_a_numero(10110))

        