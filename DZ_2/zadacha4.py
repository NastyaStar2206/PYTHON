# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него)
# можно (нужно) использовать библиотеку Random

import random

example_arr = [random.randint(0, 20) for i in range(random.randint(3, 10))] 
print(f"Изначальный список: {example_arr}")

def result_arr(example_arr):
    arr = example_arr[:]
    for i in range(len(arr)):
        index = random.randint(0, len(arr) - 1)
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp
    return arr
new_arr = result_arr(example_arr)
print(f"Перемешанный список: {new_arr}")