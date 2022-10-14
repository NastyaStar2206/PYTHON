# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
list = [i for i in range(-n,n+1)]
print(f' Список -> {list}')

with open('file.txt','w') as data:
    data.write('0 \n')
    data.write('2 \n')
    data.write('3 \n')
    data.write('1 \n')
    data.write('4 \n')
    data.write('-1 \n')

patch = 'file.txt'
data = open(patch, 'r')
total = 1
for line in data:
    position = int(line)
    total *= list[position]
print(f"Произведение указанных элементов -> {total}")