# #todo: I вариант (алгоритм сортировки вставками)
# Реализовать на Python алгоритм сортировки вставками представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 57 - 63.
#
# Задача.
# Перепишите процедуру INSERTION_SORT и отсортируйте последовательность
# A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7] по убыванию.


def insertionSort(array): #Пишем функцию сортировки в массиве
    for step in range(1, len(array)):
        key = array[step]
        a = step - 1

        while a >= 0 and key < array[a]:
            array[a + 1] = array[a]
            a = a - 1

        array[a + 1] = key
data = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7]
insertionSort(data)
print("Сортированный список: ")
print(data)