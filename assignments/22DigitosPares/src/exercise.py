def main():
    #escribe tu código abajo de esta línea
    number = input('Dame un número: ')
    pair = int

    for i in range(0, 10):
        pair = 0
        if int(number[0])%2 == 0:
            pair = pair + 1
        if int(number[1])%2 == 0:
            pair = pair + 1
        if int(number[2])%2 == 0:
            pair = pair + 1
        if int(number[3])%2 == 0:
            pair = pair + 1
                    
    print('El número de dígitos pares es: ',str(pair))
    pass
if __name__ == '__main__':
    main()
