import os
import string

os.system('cls')


def is_palindrome(line):
    line = str.upper(line)
    line = line.replace(' ', '')
    line = line.translate(str.maketrans('', '', string.punctuation))
    line.replace
    enil = line[::-1]
    if enil == line:
        return 'String is palindrome'
    else:
        return 'String is not a palindrome'


strin = 'Гни, комсомол, лом о смокинг.'
strin_2 = 'Три мухомора на полянке'
print(is_palindrome(strin))
print(is_palindrome(strin_2))
