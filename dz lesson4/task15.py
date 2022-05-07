#Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
#words = ["оператор", "конструкция", "объект"]
#desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
#Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
#Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
#в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
#либо победы.
import random
d = random.randint(0, 2)
question = ["Это слово обозначает наименьшую автономную часть языка программирования","..", ".."]
answer = ["оператор", "конструкция", "объект"]
print ("Вопрос: ",question[0])
fale = 10
let = []
word = []
for x in range(0, len(answer[d])):
    word.append("*")
while fale > 0:
    if word != list(answer[d]) :
      alfa = input("Введите букву: ")
      start = 0
    if alfa in answer[d]:
        print("Слово содержит букву:", alfa)
        fale += 0
        print(word[])
        while fale < answer[d].count(alfa):
            start = answer[d].index(alfa,word)
            let.append(start-1)
        else:
            for x in let:
                word[x] = alfa
                let.clear()

    else:
        print("Нет такой буквы")
        fale -= 1
        print(fale)
else:
    print(answer[d])
if fale == 0:
        print("Вы проиграли")






