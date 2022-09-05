# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num_quarta = int(input('Введите номер четверти: '))
if num_quarta == 1:
    print('X > 0 , Y > 0')
elif num_quarta == 2:
    print('X < 0 , Y > 0')
elif num_quarta == 3:
    print('X < 0 , Y < 0')
elif num_quarta == 4:
    print('X > 0 , Y < 0')
else:
    print('Неверный номер четверти')