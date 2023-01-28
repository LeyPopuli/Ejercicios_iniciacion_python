'''Escribir una función que calcule el 
máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
'''

def minimo_comun_mul(numero1, numero2):
    if numero1 > numero2:
        mayor = numero1
    else:
        mayor = numero2
    while (mayor % numero1 != 0) or (mayor % numero2 != 0):
        mayor +=1
    return mayor    

def maximo_comun_div(numero1, numero2):
    resto = 0
    while (numero2 > 0):
        resto = numero2
        numero2 = numero1 % numero2
        numero1 = resto
    return numero1    

print(minimo_comun_mul(24,36))
print(maximo_comun_div(24,36))