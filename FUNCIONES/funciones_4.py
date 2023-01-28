'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%.'''

def aplica_IVA(base, iva=21):
    ''' calcula el total aplicando el IVA informado sobre la base indicada. Si no tiene IVA indicado,
    se presupone 21%'''
    return base + (base * iva / 100)

print(aplica_IVA(1000,10))     
print(aplica_IVA(1000))