def main():
    #escribe tu código abajo de esta línea
    pass

import math

balance = float(input('Introduce the balance from: he previous month: '))
incomes = float(input('Introduce the incomes: '))
expenses = float(input('Introduce the expenses: '))
check = int(input('Introduce the number of the checks: '))
checks = int
interest = float
addition = float
end_balance = float

checks = check*13
addition = ((incomes+balance)-(checks+expenses))
interest = addition*0.075
end_balance = addition-interest

print('The end balance is: ', end_balance)
