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
    for i in range(n):
        print(str.center('*'*x, n*2))
        x += 2

pyramide(10)


# Statues

highs = input('What high statues have you got? Enter separated by commas: ')
highs = highs.split(',')
stat_sizes = []
for values in highs:
    stat_sizes.append(int(values))

stat_sizes.sort()
count = 0
for i in range(len(sizes)):
    if stat_sizes[i] - stat_sizes[i-1] > 1:
        count += stat_sizes[i] - stat_sizes[i-1] - 1

print(count)

# Through the function

def statues(sizes):  #list of integers expected
    sizes.sort()
    d = 0
    for i in range(len(sizes)):
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

    for i in range(len(secret)):
        for j in range(len(my_num)):
            if secret[i] == my_num[j] and i == j:
                bulls += 1
            elif secret[i] == my_num[j] and i != j:
                cows += 1
    if bulls == 4:
        print('You won!')

    else:
        print(f'{bulls} bulls, {cows} cows, try again!')
