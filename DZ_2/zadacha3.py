# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элементов этой последовательности 
# (для проверки сумма для 4 элементов = 9,06 (примерно))

num = int(input("Введите число: "))
sum = 0
num_arr = [round(((1 + 1/i)**i),2) for i in range (1, num+1)]
for i in num_arr:
    sum += i
print(f'В последовательности {num_arr} сумма элементов равна {sum}')