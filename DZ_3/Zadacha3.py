# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная
# часть не считается за 0 и оно (число) в сравнении не участвует
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
# my_list = list(map(float, input("Введите числа в строку через пробел: ").split()))

res_list = []
for i in my_list:
    if i % 1 > 0:
        num = round((i % 1), 2)
        res_list.append(num)

result = round((max(res_list) - min(res_list)), 2)

print(f"{my_list} => {result}")