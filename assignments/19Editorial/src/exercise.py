def main():
    #escribe tu código abajo de esta línea
    import math

    words = int(input('Introduce the number of words: '))
    cost = float
    pages = int
    descount = float

    pages = (math.ceil(words/475))*60
    descount = pages*0.10
    cost = pages-descount

    print('The publishing cost is: ', cost)
    pass
