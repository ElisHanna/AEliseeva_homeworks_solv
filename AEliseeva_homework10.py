import os

os.system('cls')


def desharping(line):

    if not isinstance(line, str):
        return 'String expected. Review the data.'

    while '#' in line:
        a = line.index('#')
        if line != '#':
            line = line.replace(line[a-1]+line[a], '')
        else:
            line = line.replace('#', '')

    return line


def candles(candles_number, make_new):

    if not isinstance(candles_number, int) or\
       not isinstance(make_new, int):
        return 'I need integers to count. Please check your data.'

    result = candles_number
    new_candles = candles_number // make_new

    while new_candles > 0:
        candles_number = candles_number % make_new + new_candles
        result += new_candles
        new_candles = candles_number // make_new

    return result


def letters_counter(text):

    if not isinstance(text, str):
        return 'String data type expected'

    length = len(text)
    newstr = ''
    worm_tail = 0
    worm_head = 0

    for worm_head in range(length):
        if (worm_head == length - 1) or (text[worm_head + 1] != text[worm_head]):
            if worm_head - worm_tail == 0:
                newstr = newstr + text[worm_tail]
            else:
                newstr = newstr + text[worm_tail] + str(worm_head - worm_tail + 1)
            worm_tail = worm_head + 1

    return newstr
