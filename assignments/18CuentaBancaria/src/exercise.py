def main():
    #escribe tu código abajo de esta línea
    balance = float(input('Dame el saldo del mes anterior: ',"%.2f"%))
    incomes = float(input('Dame los ingresos: '))
    expenses = float(input('Dame los egresos: '))
    check = int(input('Dame el número de cheques: '))
    checks = int
    nterest = float
    addition = float
    end_balance = float

    checks = check*13
    addition = ((incomes+balance)-(checks+expenses))
    interest = addition*(7.5/100)
    end_balance = addition-interest

    print('El saldo final de la cuenta es:',end_balance)
    pass
if __name__ == '__main__':
    main()
