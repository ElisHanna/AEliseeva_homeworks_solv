import os
import logging
import sys

os.system('cls')


logger = logging.getLogger('best_logger')
if not logger.hasHandlers():
    logger.setLevel(logging.DEBUG)
    stream = logging.StreamHandler(stream=sys.stdout)
    file = logging.FileHandler('actions_log.log', 'a')
    stream.setLevel(logging.INFO)
    file.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream.setFormatter(formatter)
    file.setFormatter(formatter)
    logger.addHandler(stream)
    logger.addHandler(file)


def my_division():
    a = input('Введите a: ')
    b = input('Введите b: ')
    logger.info(f'a={a}, b={b}')
    return int(a) / int(b)


try:
    logger.info(f'Successful division with result {my_division()}')
except ZeroDivisionError:
    logger.error('ZeroDivisionError', exc_info=False)
