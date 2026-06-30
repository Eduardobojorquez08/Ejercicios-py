texto = ("el perro corre el gato corre el perro")

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo
print(contar_palabras(texto))
