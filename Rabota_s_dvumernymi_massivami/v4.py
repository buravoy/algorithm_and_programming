# Вариант 4.
# 1. Дана прямоугольная матрица.
# Найти строку с наибольшей и строку с наименьшей суммой элементов.
# Вывести на печать найденные строки и суммы их элементов.

matrix = [
    [1, 3, 5, -2, -17],
    [-6, 8, 4, -2, 0],
    [7, -3, 9, -8, 12],
    [9, 0, -2, 6, -7],
]

summaryArr = []
print('Матрица:')
for row in matrix:
    print(row)
    summaryArr.append(sum(row))

maxSum = max(summaryArr)
minSum = min(summaryArr)
print(f'Максимальная сумма: {maxSum}. В строке {matrix[summaryArr.index(maxSum)]}')
print(f'Минимальная сумма: {minSum}. В строке {matrix[summaryArr.index(minSum)]}')


# 2. Дана квадратная матрица A[N, N].
# Записать на место отрицательных элементов матрицы нули, а на место положительных — единицы.
# Вывести на печать нижнюю треугольную матрицу в общепринятом виде,

squareMatrix = [
    [1, 3, 5, -2],
    [-6, 8, 4, -2],
    [7, -3, 9, -8],
    [9, 0, -2, 6],
]

print('Квадратная матрица:')
for row in squareMatrix:
    print(row)

for row in range(len(squareMatrix)):
    for el in range(len(squareMatrix[row])):
        if squareMatrix[row][el] < 0:
            squareMatrix[row][el] = 0
        else:
            squareMatrix[row][el] = 1

triangle = []
for i in range(0, len(squareMatrix)):
    triangle.append(squareMatrix[i][:i+1])

print('Нижняя треугольная матрица из 0 и 1, в общепринятом виде:')
for row in triangle:
    print(row)
