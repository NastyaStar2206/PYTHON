# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

from calendar import weekday
from datetime import datetime


week_days = ('Понедельник', 'Вторник', 'Среда', 'Четверг',
             'Пятница', 'Суббота', 'Воскресенье')
number = int(input('Введите номер дня недели: '))


def Find_day(list, num):
    if 0 < num < 6:
        return week_days[num-1]
    elif 5 < num <= 7:
        return f'{week_days[num-1]}, выходной день'

day_name = Find_day(week_days, number)
print(day_name)