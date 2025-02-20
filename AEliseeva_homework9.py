import os

os.system('cls')


def rising_row(*args):

    if len(args) == 0:
        return 'Please, give me some arguments'

    for items in args:
        if isinstance(items, list):
            array = list.copy(items)
        else:
            array = list(args)

    if len(array) == 0:
        return "Array for check can't be empty"

    for argument in array:
        if not isinstance(argument, int):
            return "Sorry, I can compare only integers"

    new_array = [array[0]]

    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            new_array.append(array[i])

    control_array = [array[0]]

    for j in range(1, len(new_array)):
        if new_array[j] > new_array[j-1]:
            control_array.append(new_array[j])

    if len(array) - len(control_array) > 1:
        return False
    else:
        return True


def cirkle(n, number):

    ruler = []
    for h in range(0, n):
        ruler.append(h)

    motion = ruler.index(number) - int(n/2)
    return ruler[motion]


def luhn(number):

    number = str(number)
    number = number.replace(' ', '')

    if len(number) == 0:
        return 'Give me your number'
    elif len(number) < 10 or len(number) > 19:
        return 'Wrong lehgth, I do not trust you -_-'

    for compon in number:
        if not compon.isdigit():
            return 'Number contains wrong symbols'

    number = [int(symb) for symb in number]
    number.reverse()
    odd = []
    honest = []
    x = len(number)

    for k in range(x):
        if k % 2 == 0:
            odd.append(number[k])
        elif k % 2 == 1:
            honest.append(number[k] * 2)

    for char in honest:
        if char < 9:
            odd.append(char)
        else:
            odd.append(char // 10 + char % 10)

    ctrl_sum = 0

    for nums in odd:
        ctrl_sum += nums

    return bool(ctrl_sum % 10 == 0)
