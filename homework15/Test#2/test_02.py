import os

os.system('cls')


def square(n):
    return n**2


num = int(input('Enter your number: '))
print(square(num))


def honest_or_odd(m):
    if m % 2 == 0:
        return f'{m} is honest'
    else:
        return f'{m} is odd'


number = int(input('Enter your number: '))
print(honest_or_odd(number))
