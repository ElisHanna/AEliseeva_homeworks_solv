import os

os.system('cls')


class ResultError(Exception):
    pass


def validate_arguments(func):
    def wrapper(*args):

        for item in args:
            if not isinstance(item, int) and\
               not isinstance(item, float):
                raise ValueError("Some argument isn't a number!")
            else:
                if item <= 0:
                    raise ValueError("Some argument isn't a positive number!")

        return func()
    return wrapper


@validate_arguments
def my_great_func(*args):
    return 'have a nice day!'


try:
    print(my_great_func(1, 2, 10, 3, 2.5))
except ValueError as e:
    print(e)

try:
    print(my_great_func((1, 2), 10, 3, 2.5))
except ValueError as e:
    print(e)


def is_number(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not isinstance(res, int) and\
           not isinstance(res, float):
            raise ResultError("The function can return only numbers!")
        else:
            return func(*args, **kwargs)
    return wrapper


@is_number
def random_function(a, b):
    return a+b


try:
    print(random_function('1', '2'))
except ResultError as m:
    print(m)

try:
    print(random_function(1, 2))
except ResultError as m:
    print(m)


def typed(type):
    def dec(func):
        def wrapper(*args):
            new_args = []
            for item in args:
                if not isinstance(item, type):
                    item = type(item)
                    new_args.append(item)
                else:
                    new_args.append(item)

            new_args = tuple(new_args)
            return func(*new_args)
        return wrapper
    return dec


@typed(type = float)
def add(a, b, c):
    return a + b + c


print(add(0.1, 0.2, 0.4))


archive = {}

def cache(record):
    def dec(func):
        def wrapper(x):
            if record.get(x) == None:
                record.update({x:func(x)})
                return func(x)
            else:
                return record[x]
        return wrapper
    return dec

@cache(archive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
