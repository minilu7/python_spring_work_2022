# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.
x = int(5)
y = int(3)
z = int(15)
if x>y and x>z:
    print("Наибольшее число",x)
if y>z and y>x:
    print("Наибольшее число",y)
if z>x and z>y:
    print("Наибольшее число",z)