def main():
    #escribe tu código abajo de esta línea
    new_vg = int(input('Dame la cantidad de juegos nuevos: '))
    old_vg = int(input('Dame la cantidad de juegos usados: '))
    cost = int
    cost_old = int
    cost_new = int

    cost_old = old_vg*350
    cost_new = new_vg*1000
    cost = cost_new+cost_old

    print('El total de la compra es: ', cost)
    pass
