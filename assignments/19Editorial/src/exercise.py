def main():
    #escribe tu código abajo de esta línea
    import math

    words = int(input('Dame el número de palabras: '))
    cost = float
    pages = int
    descount = float

    pages = (math.ceil(words/475))*60
    descount = pages*0.10
    cost = pages-descount

    print('El costo de la publicación es: ', cost)
    pass
