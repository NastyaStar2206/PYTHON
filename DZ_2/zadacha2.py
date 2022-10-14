# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("Введите число: "))
factorial = 1
fact_arr= [] 
for i in range(1, num+1):
    factorial *= i
    fact_arr.append(factorial)
print(f'N = {num} -> {fact_arr}')
