'''Escribir una función que calcule el área de un círculo y otra 
que calcule el volumen de un cilindro usando la primera función.'''

pi = 3.14159

def area_circulo(radio):
    pi = 3.14159
    return pi*(radio**2)

def area_cilindro(radio, altura):
    return area_circulo(radio) * altura   

print(area_circulo(5))    
print(area_cilindro(3, 5))  
