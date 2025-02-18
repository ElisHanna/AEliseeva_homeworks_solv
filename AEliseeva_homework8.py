import os
from random import sample

os.system('cls')

# Pyramide

rows = int(input('How much rows do you wish? '))
fact = 1
for j in range(rows):
    print(str.center('*'*fact, rows*2))
    fact += 2

# Through the function


def pyramide(n):

    n = int(n)
    x = 1
    i = 0
    while i < n:
        print(str.center('*'*x, n*2))
        x += 2
        i += 1


pyramide(10)


# Statues

stat_highs = input('What high statues have you got? Enter separated by commas: ')
highs = stat_highs.split(',')
stat_sizes = []
for values in highs:
    stat_sizes.append(int(values))

stat_sizes.sort()
count = 0
row_lenght = len(stat_sizes)
for j in range(row_lenght):
    if stat_sizes[j] - stat_sizes[j-1] > 1:
        count += stat_sizes[j] - stat_sizes[j-1] - 1

print(count)

# Through the function


def statues(sizes):  # list of integers expected

    sizes.sort()
    d = 0
    sizes_lenght = len(sizes)
    for i in range(sizes_lenght):
        if sizes[i] - sizes[i-1] > 1:
            d += sizes[i] - sizes[i-1] - 1

    print(d)


statues([6, 2, 3, 8])


# Cows and bulls

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
begin = sample(nums[1:], 1)
nums.remove(begin[0])
secret = begin + sample(nums, 3)

bulls = 0
while bulls < 4:
    cows = 0
    bulls = 0
    my_guess = input('Guess the number(4 different chars): ')
    my_num = [int(chars) for chars in my_guess]
    num_lenght = len(my_num)
    secret_lenght = len(secret)

    for k in range(secret_lenght):
        for j in range(num_lenght):
            if secret[k] == my_num[j] and k == j:
                bulls += 1
            elif secret[k] == my_num[j] and k != j:
                cows += 1
    if bulls == 4:
        print('You won!')

    else:
        print(f'{bulls} bulls, {cows} cows, try again!')
