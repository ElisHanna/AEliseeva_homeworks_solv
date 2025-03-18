import os

os.system('cls')


def plus_one(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 9:
            lst[i] += 1
            return lst
        else:
            lst[i] = 0
    return [1] + lst


assert plus_one([9]) == [1, 0]
assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([1, 1, 9]) == [1, 2, 0]
assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
