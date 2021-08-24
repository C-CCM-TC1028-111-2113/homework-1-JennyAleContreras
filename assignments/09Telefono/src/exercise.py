def main():
    #escribe tu código abajo de esta línea
    messages = int(input('Dame el número de mensajes: '))
    megas = float(input('Dame el número de megas: '))
    minutes = float(input('Dame el número de minutos: '))
    cost_message = float
    cost_mega = float
    cost_minute = float
    cost = float

    cost_message = 0.80*messages
    cost_mega = 0.80*megas
    cost_minute = 0.80*minutes
    cost = cost_message+cost_mega+cost_minute

    print('El costo mensual es:',cost)
    pass
if __name__ == '__main__':
    main()
