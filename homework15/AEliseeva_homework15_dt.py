import os
from datetime import date, datetime

os.system('cls')


def days_difference():
    first_point = input('Enter the first date format YYYY-MM-DD:')
    second_point = input('Enter the second date format YYYY-MM-DD:')
    first_date = datetime.strptime(first_point, '%Y-%m-%d')
    second_date = datetime.strptime(second_point, '%Y-%m-%d')
    difference = second_date - first_date
    return abs(difference.days)


def past_or_future():
    today = date.today()
    my_point = input('Enter the second date format YYYY-MM-DD:')
    my_date = datetime.strptime(my_point, '%Y-%m-%d').date()
    differ = my_date - today
    if differ.days > 0:
        return f'{my_date} is the future date'
    elif differ.days == 0:
        return f'{my_date} is today'
    else:
        return f'{my_date} is in past'
