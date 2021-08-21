def main():
    #escribe tu código abajo de esta línea
    new_vg = int(input('Introduce the number of new videogames: '))
    old_vg = int(input('Introduce the number of old videogames: '))
    cost = int
    cost_old = int
    cost_new = int

    cost_old = old_vg*350
    cost_new = new_vg*1000
    cost = cost_new+cost_old

    print('The total cost is: ', cost)
    pass
