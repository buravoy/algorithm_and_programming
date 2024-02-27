from math import e, tan, sin, sqrt

# задание 1
print('Задание 1, вариант 4')

print('Вычисляем равенство: \n'
      '          3 + e^y-1\n'
      'b = --------------------\n'
      '     1+x^2 * |y - tg(z)|')

x = float(input('Введите X: '))
y = float(input('Введите Y: '))
z = float(input('Введите Z: '))

numerator = (3 + (e ** (y - 1)))
module = (y - tan(z))

if module < 0:
    module = module * (-1)

denominator = ((1 + (x ** 2)) * module)

if denominator == 0:
    print('Деление на "0"')
else:
    print(f'b = {numerator / denominator}')

# задание 2
print('Задание 2, вариант 4')

print('Вычисляем равенство, в зависимости от условия: \n'
      '     | sin(x+y) + 2*2(x+y)^2, x-y > 0\n'
      'b = /  sin(x-y) + (x-y)^3, x-y < 0\n'
      '    \\  |x^2 + sqrt(y)|, y != 0, x = 0 \n'
      '     | 0, y = 0')

x1 = float(input('Введите X: '))
y1 = float(input('Введите Y: '))

if y1 == 0:
    print(f'b = {0}')
elif y1 != 0 and x1 == 0:
    module1 = x1 ** 2 + sqrt(y1)
    if module1 < 0:
        module1 = module1 * (-1)
    print(f'b = |x^2 + sqrt(y)| {module1}')
elif x1 - y1 > 0:
    print(f'b = sin(x+y) + 2*(x+y)^2 = {(sin(x1 + y1)) + (2 * ((x1 + y1) ** 2))}')
elif x1 - y1 < 0:
    print(f'b = sin(x-y) + (x-y)^3 = {(sin(x1 - y1)) + ((x1 - y1) ** 3)}')
else:
    print('не найдено')
