#todo: Написать игру , где программа загадывает число от 0 до 100 (через функцию random) , а пользователь
#пытается его отгадать(через консоль). При успехе выводится поздравление в победе и результат попыток.
#По истечении 10 неудачных попыток выводится проигрышь.

#Для получения функции числа из диапазона от 0 до 100 подключать библиотеку
#import random
#random.randint(0,100)
import random
z = random.randint(0,100)
fale = 0
while fale < 10:
    a = int(input("Введите предпологаемое число: "))
    if a < z:
        print("Больше")
        fale +=1
    if a > z:
        print("Меньше")
        fale += 1
    if a == z:
        print("Вы угадали")
        break
    if fale == 10:
        print("Вы проиграли")
        break