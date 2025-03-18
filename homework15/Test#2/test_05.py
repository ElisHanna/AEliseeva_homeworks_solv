import os
import string

os.system('cls')


def is_palindrome(line):
    if isinstance(line, int) or\
       isinstance(line, float):
        line = str(line)
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
numb = 535
print(is_palindrome(strin))
print(is_palindrome(strin_2))
print(is_palindrome(numb))
