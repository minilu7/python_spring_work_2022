# #todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
#
#
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||
def transpose(matrix):
    couples= len(matrix)
    line = len(matrix[1])
    matrix2 = [[matrix[j][i] for j in range(couples)] for i in range(line)]
    return matrix2
m = [[1, 2, 3], [4, 5, 6]]
print(transpose(m))