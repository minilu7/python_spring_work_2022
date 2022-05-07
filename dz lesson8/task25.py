#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

#Input             	            Output
#apple	                        aple
#25.04.2022 Good morning !!	    godmrni
text = input("Введите слово: ") # вводим слово где нужно убрать повторяющиеся символы
x = ''.join(sorted(set(text), key=text.index)) #set удаляет все повторения(выдает их в разнобой).sorted возвращает новый отсортированый список, который был получен из объекта(в нашем случает text). key возвращает индекс элементов в text, что бы sorted выдал их в том же порядке.
print(x)
text2 = input("Введите ключевую фразу, по которой будет строиться часть алфавита: ")
text2 = text2.lower() #перевели все в нижний регистр
new_text = "" #запись результата
for letter in text2: #перебераем каждый символ в text2. letter новая переменная
    if letter.isalpha(): #проверям является ли символ буквой.
        if letter not in new_text:
            new_text = new_text + letter
print(new_text)

