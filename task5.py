# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math
ax = int(input('Введите координату Х точки А: '))
ay = int(input('Введите координату Y точки А: '))
bx = int(input('Введите координату Х точки В: '))
by = int(input('Введите координату Y точки В: '))

len_ab = ((ax - bx)**2 + (ay - by)**2)**0.5
# len_ab = math.sqrt((ax - bx)**2 + (ay - by)**2)
# print(type(len_ab))

print(round(len_ab, 2))