from math import sqrt

# # Задание №1
# 4. Написать алгоритм проверки условия: могут ли три данных числа быть длинами сторон треугольника?

a1 = float(input('Сторона A: '))
b1 = float(input('Сторона B: '))
c1 = float(input('Сторона C: '))

if (a1 + b1 > c1) and (a1 + c1 > b1) and (b1 + c1 > a1):
    print(f'Треугольник со сторонами {a1}, {b1}, {c1} существует.')
else:
    print(f'Треугольника со сторонами {a1}, {b1}, {c1} не существует')


# Задание №2
# 4. Дана точка А (х1,у1). Верно ли, что расстояние от точки до начала координат ровно C см.

x = float(input('Ведите координату точки (X): '))
y = float(input('Ведите координату точки (Y): '))
distance = float(input('Ведите введите расстояние до начала координат: '))

actualDistance = sqrt((x**2) + (y**2))

if actualDistance == distance:
    print(f'Расстояние от точки ({x}, {y}) до начала координат ровно {distance}. Вы ввели верное расстояние')
else:
    print(f'Расстояние от точки ({x}, {y}) до начала координат {actualDistance}. Вы ввели {distance},'
          f'это НЕ верное расстояние')


# Дополнительные задачи
# 4. Напишите программу, которая получает с клавиатуры возраст человека (целое число, не превышающее 120)
# и выводит этот возраст со словом «год», «года» или «лет».
# Например, «21 год», «22 года», «25 лет».

age = int(input('Ведите введите возраст (max 120): '))

if (age > 4) and (age < 21):
    print(f'Возраст {age} лет.')
elif age > 120:
    print('Не больше 120')
elif age < 0:
    print('Возраст не может быть меньше 0')
elif age < 1:
    print('Возраст меньше 1 года')
else:
    res = age % 10
    if res == 1:
        print(f'Возраст {age} год')
    elif res < 5:
        print(f'Возраст {age} года')
    else:
        print(f'Возраст {age} лет')
