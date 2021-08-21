def main():
    #escribe tu código abajo de esta línea
    pass

import math

number = input('Introduce a number with 4 digits(starting without 0): ')
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
                    
print('The number of pairs is: ', str(pair))
