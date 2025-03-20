import os

os.system('cls')


def summary(n):
    a = 0
    for i in range(n+1):
        a += i
    return a


assert summary(1) == 1
assert summary(8) == 36
assert summary(22) == 253
assert summary(100) == 5050
