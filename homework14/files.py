import os

os.system('cls')


with open('students.txt', 'w') as myfile:
    myfile.write('Ivanov Ivan, 130, 9\n')
    myfile.write('Petrov Petr, 130, 7\n')
    myfile.write('Sidorov Sidor, 131, 8\n')
    myfile.write('Agrafova Agrafena, 131, 9\n')
    myfile.write('Lampovaya Evlampiya, 131, 6\n')

with open('students.txt') as file:
    content = file.readlines()

analys = []
for line in content:
    line = line.replace('\n', '')
    splitted = line.split(', ')
    analys.append(splitted)

students_count = len(analys)

count_130 = 0
count_131 = 0
sum_130 = 0
sum_131 = 0

for stud in analys:
    if stud[1] == '130':
        count_130 += 1
        sum_130 += int(stud[2])
    else:
        count_131 += 1
        sum_131 += int(stud[2])

common_130 = round((sum_130/count_130), 2)
common_131 = round((sum_131/count_131), 2)

with open('students.txt', 'a') as f:
    f.write(f'List contains {students_count} students\n')
    f.write(f'In group 130 are {count_130} students, common mark is {common_130} \n')
    f.write(f'In group 131 are {count_131} students, common mark is {common_131} \n')
    