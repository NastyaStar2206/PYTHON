#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#1й способ (рандомное число):
from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(f'Число: {(n)}')
print(f'Сумма цифр: {sum_digit(n)}')


#2-й способ (Ввод по запросу)

num = float(input("ВВедите число: "))
sum = 0
for i in str(num): #через строку
    if i != ".":
        sum += int(i)
print(f"Сумма цифр {num} числа равна {sum} ")