# 1. Дан массив целых чисел. Найти максимальный элемент массива и его порядковый номер.
n = int(input('Введите длину массива: '))
arr = []

for k in range(n):
    arr.append(int(input(f'Введите {k + 1} элемент массива (целое число): ')))

print(f'Вы заполнили массив {arr}')

maxEl = max(arr)
print(f'Максимальный элемент равен {maxEl}, его номер в массиве {arr.index(maxEl) + 1}')


# 2. Дан одномерный массив целого типа. Получить другой массив, состоящий только из нечетных
# чисел исходного массива или сообщить, что таких чисел нет. Полученный массив вывести в порядке убывания элементов.

odd = []
for el in arr:
    if el % 2 == 1:
        odd.append(el)

if len(odd):
    print(f'Нечетные элементы {sorted(odd)}')
else:
    print('Нечетных элементов нет')
