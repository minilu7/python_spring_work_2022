#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.
import random
d = random.randint(0, 2)
question = ["Это слово обозначает наименьшую автономную часть языка программирования"]
answer = ["оператор", "конструкция", "объект"]
print ("Вопрос: ",question[0])
fale = 10 #количество попыток
let = []
word = answer[d]
x = ['*']*len(word)#заменяет звездочками буквы в ответе
print("".join(x)) #напечатали звездочки
while fale > 0:
      alfa = input("Введите букву: ")
      start = 0
      for i in range(len(word)): #берет каждый символ в переменной word. len считает количество символов в ворд и возвращает это кол-во. Считай проиндексировали и теперь знаем где какая буква в слове, повторяются ли они, на каком месте стоят
        if word[i] == alfa:
            x[i] = alfa
            fale += 0
      s = "".join(x)
      print(s)
      if s == word:
          print("вы выйграли")
          break
      if word[i] != alfa:
          print("Нет такой буквы")
          fale -= 1
          print(fale)
if fale == 0:
        print("Вы проиграли")