import logging

logging.basicConfig(level=logging.INFO)

def choose_operation():
    operation = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:'))

    num1 = float(input('Podaj składnik 1.'))
    num2 = float(input('Podaj składnik 2.'))
    return operation, num1, num2


def mini_calc(x, n1, n2):
    if x == 1:
        logging.info(f'Dodaję {n1} i {n2}')
        return n1 + n2
    elif x == 2:
        logging.info(f'Odejmuję {n1} i {n2}')
        return n1 - n2
    elif x == 3:
        logging.info(f'Mnożę {n1} i {n2}')
        return n1 * n2
    elif x == 4:
        logging.info(f'Dzielę {n1} i {n2}')
        if n2 != 0:
            return n1 / n2
        else:
            raise ZeroDivisionError("Nie można dzielić przez zero!")


# main do flow które się uruchamia

if __name__ == '__main__':
    opr, num1, num2  = choose_operation()
    print(mini_calc(opr, num1, num2))