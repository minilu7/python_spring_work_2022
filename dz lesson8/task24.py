#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = " abcdefghijklmnopqrstuvwxyz"
num =input("Введите цифры: ")#цифры и знаки через пробел
new_num = num.split(" ")
a = "" #временное хранение
for letter in new_num:
    if letter.isdigit(): #функция проверяет есть ли цифры  в написанном сообщении
        n = int(letter)
        a = a + alphabet[n]
    else:
        a = a + letter
print(a)
