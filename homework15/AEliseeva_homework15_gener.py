import os
import logging

os.system('cls')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )


def sum_numbers(n):
    array = [i for i in range(1, n+1)]
    return sum(array)


def is_psrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def prime_numbers(start, end):
    for number in range(start, end+1):
        if number > 2:
            if is_psrime(number) is True:
                yield number


gen = prime_numbers(1, 1000)
for i in range(10):
    logging.info(next(gen))
