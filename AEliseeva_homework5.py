import os
import string

os.system('cls')

# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

first_str = 'www.my_site.com#about'
print(first_str.replace('#', '/'))


# Напишите программу, которая добавляет ‘ing’ к словам

# Easy

word = 'hardlywork'
print(word + 'ing')

# Interesting

work_string = input('Enter your words:')
work_string = work_string.translate(str.maketrans('', '', string.punctuation))
work_string = work_string.translate(str.maketrans('', '', string.digits))
temp_list = work_string.split()

if temp_list == []:
    print('Why are you so silent?')
else:
    work_string = ('ing '.join(temp_list)) + 'ing'

print(work_string)


# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

line = 'Ivanou Ivan'
print(line.split()[1] + ' ' + line.split()[0])


# Напишите программу которая удаляет пробел в начале, в конце строки

test_string = ' Empty place cannot be saint  '
print(test_string.lstrip())  # Удаление пробела в начале строки
print(test_string.rstrip())  # Удаление пробела в конце строки
print(test_string.strip())   # Удаление пробелов в начале и в конце строки


# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало
# этому утверждению. "pARiS" >> "Paris"

print(str.capitalize('pARiS'))


# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]

print(str.split('Robin Singh'))

# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(str.split('I love arrays they are my favorite'))


# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
print(f'Привет, {name[0]} {name[1]}! Добро пожаловать в {city} {country}')


# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

words_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(words_list))


# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

team = ['Kili', 'Fili', 'Balin', 'Dvalin', 'Oin', 'Gloin', 'Bifur', 'Bofur', 'Bombur', 'Torin']
team.insert(2, 'Ori')
del team[6]
print(team)
