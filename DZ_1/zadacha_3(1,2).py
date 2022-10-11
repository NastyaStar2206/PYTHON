# 1. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

from random import randint

quarter = randint(1, 4)
diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']

def show_diapasone (quart, diapasones):
    return diapasones[quart-1]

print (f'{quarter}: {diapasones[quarter-1]}')



# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from random import randint
import math

def Get_coordinates(num_plan, left, right):     # координаты точек
    return tuple([randint(left, right) for i in range(num_plan)])

def Find_dist(a, b):    # расстояние между точками
    return round(math.sqrt(sum((x - y)**2 for x, y in zip(a, b))), 3)

num_plan = 3    # количество осей координат
left = -10
right = 10

point_A = Get_coordinates(num_plan, left, right)
point_B = Get_coordinates(num_plan,left, right)

print(f'A {point_A}, B {point_B}')
print (f'Расстояние между точками: {Find_dist(point_A, point_B)}')