import logging

logging.basicConfig(level=logging.INFO)

def mini_calculator():
    operation = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:'))

    num1 = float(input('Podaj składnik 1.'))
    num2 = float(input('Podaj składnik 2.'))
    if operation == 1:
        logging.info(f'Dodaję {num1} i {num2}')
        return num1 + num2
    elif operation == 2:
        logging.info(f'Odejmuję {num1} i {num2}')
        return num1 - num2
    elif operation == 3:
        logging.info(f'Mnożę {num1} i {num2}')
        return num1 * num2
    elif operation == 4:
        logging.info(f'Dzielę {num1} i {num2}')
        return num1 / num2
    
print(mini_calculator())