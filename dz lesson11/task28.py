# #todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# # Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import datetime
count = int()
def decorator_sort(func):
    count = 0
    count += 1
    print(count)
    def wrapper(name):
            global count
            file = open("debug.log", "a")
            a = datetime.datetime.now() #вызываем дату и время
            print(a)
            func(name) #сама функция
            b = func.__name__ #записываем только название функции
            file.write(str(b) + ", " + str(a) + "\n" )
    return wrapper

@decorator_sort
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