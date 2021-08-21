def main():
    #escribe tu código abajo de esta línea
    pass

import math

messages = int(input('Introduce the number of messages: '))
megas = float(input('Introduce the number of megas: '))
minutes = float(input('Introduce the number of minutes: '))
cost_message = float
cost_mega = float
cost_minute = float
cost = float

cost_message = 0.80*messages
cost_mega = 0.80*megas
cost_minute = 0.80*minutes
cost = cost_message+cost_mega+cost_minute

print('The monthly cost is: ', cost)
