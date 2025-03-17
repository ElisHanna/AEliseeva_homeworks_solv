import os
import re

os.system('cls')

with open('regexp.txt') as testfile:
    text = testfile.readlines()

def looking_for_dates(doc):
    pattern = r"(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})"
    res = []
    for lines in doc:
        result = re.search(pattern, lines)
        if result is not None:
            res.append(result.group())
    return res


looking_for_dates(text)


def password_check(password):
    if re.search(r'[A-Z]+', password) is not None and\
       re.search(r'[a-z]+', password) is not None and\
       re.search(r'\d+', password) is not None and\
       re.search(r'\S\S\S\S+', password) is not None:
        return 'Good password!'
    else:
        return 'Unreliable password'


line = 'Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова.\
        Смешно, не не правда ли? Не нужно портить хор хоровод.'
pattern = r'\b(\w+)\b(?=\s+\b\1|\s+\b\w*\1\w*\b)'

final = re.sub(pattern, '', line)
print(final)
