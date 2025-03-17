import os
import logging

os.system('cls')


logging.basicConfig(
    level=logging.INFO,
    filename='user_actions.log',
    filemode="a", format="%(asctime)s - %(levelname)s - %(message)s"
    )


def my_division():
    a = input('Введите a: ')
    b = input('Введите b: ')
    logging.info(f'a={a}, b={b}')
    return int(a) / int(b)


try:
    logging.info(f'Successful division with result {my_division()}')
except ZeroDivisionError as e:
    logging.error('ZeroDivisionError', exc_info=False)
