def main():
    #escribe tu código abajo de esta línea
    pass
    
    balance = float(input('Introduce the balance from the previous month: '))
    incomes = float(input('Introduce the incomes: '))
    expenses = float(input('Introduce the expenses: '))
    check = int(input('Introduce the number of the checks: '))
    checks = int
    nterest = float
    addition = float
    end_balance = float

    checks = check*13
    addition = ((incomes+balance)-(checks+expenses))
    interest = addition*(7.5/100)
    end_balance = addition-interest

    print('The end balance is: ', end_balance)
