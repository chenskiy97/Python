# **Задачи домашней работы:**

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#     Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

def dey_week(day):
    if day >= 1 and day <= 7:
        if day >= 1 and day <=5:
            print('не является выходным днем')
        if day >= 6 and day <= 7:
            print('является выходным днем')
    else:
        print('такого дня не существует')

# dey_week(int(input('Введите день недели от 1 до 7: ')))



# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def to_bool(x):
    if x == 0:
        return False
    return True


def Ex2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(to_bool(x) or to_bool(y) or to_bool(z)) == (not(to_bool(x)) and not(to_bool(y)) and not(to_bool(z)))) == False:
                    return False
    return True

# print(Ex2())



# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#     Пример: 
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3

def quarter_number(x,y):
    if x == 0 and y == 0:
        print('Данная точка является началом координат.')
    elif x !=0 and y == 0:
        print('Данная точка лежит на оси X')
    elif x == 0 and y != 0:
        print('Данная точка лежит на оси Y')
    elif x > 0 and y > 0:
        print('Данная точка лежит в четверти 1')
    elif x < 0 and y > 0:
        print('Данная точка лежит в четверти 2')
    elif x < 0 and y < 0:
        print('Данная точка лежит в четверти 3')
    elif x > 0 and y < 0:
        print('Данная точка лежит в четверти 4')
    else:
        print('Данные введены не верно')

# x = int(input('Введите координату X: '))
# y = int(input('Введите координату Y: '))
# quarter_number(x,y)



# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def coordinate_range(num):
    if num == 1:
        print('В данной четверти координаты могут быть в следующем диапазоне: x > 0, y > 0')
    elif num == 2:
        print('В данной четверти координаты могут быть в следующем диапазоне: x < 0, y > 0')
    elif num == 3:
        print('В данной четверти координаты могут быть в следующем диапазоне: x < 0, y < 0')
    elif num == 4:
        print('В данной четверти координаты могут быть в следующем диапазоне: x > 0, y < 0')
    else:
        print('Данной четверти не существует')

# coordinate_range(int(input('Введите номер четверти: ')))



# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     Пример:
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А:')
x_A = float(input('x = '))
y_A = float(input('y = '))
print('Введите координаты точки B:')
x_B = float(input('x = '))
y_B = float(input('y = '))

AB = round((((x_A - x_B)**2 + (y_A - y_B)**2) ** 0.5),3)
print(AB) 