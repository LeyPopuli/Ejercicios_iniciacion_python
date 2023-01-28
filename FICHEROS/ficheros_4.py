'''Escribir un programa que acceda a un fichero de internet mediante su url y 
muestre por pantalla el número de palabras que contiene.
'''

from urllib import request

#FORMA 1

fichero = request.urlopen("https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md")
palabras = fichero.read()
print(len(palabras.split()))
fichero.close()

#FORMA 2

def contador_palabras(url):
    from urllib import request
    from urllib.error import URLError
    try:
        fichero = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = fichero.read()
        return len(contenido.split())

print(contador_palabras('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md'))
print(contador_palabras('https://no-existe.txt'))