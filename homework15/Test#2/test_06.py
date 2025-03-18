import os
import string

os.system('cls')


def readfile(file):
    with open(file) as myfile:
        content = myfile.readlines()

    numb = len(content)
    words = 0
    letters = 0
    for line in content:
        line = line.translate(str.maketrans('', '', string.punctuation))
        work_list = line.split()
        words += len(work_list)
        line = line.replace(' ', '')
        letters += len(line)

    with open(file, 'a') as f:
        f.write(f'Text contains {numb} strings\n')
        f.write(f'Text contains {words} words\n')
        f.write(f'Text contains {letters} letters\n')

        print(f'Text contains {numb} strings')
        print(f'Text contains {words} words')
        print(f'Text contains {letters} letters')

filename = 'lorem.txt'
readfile(file=filename)
