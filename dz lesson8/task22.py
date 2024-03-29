# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

f = open("message.txt", "r", encoding="utf-8")
text = f
alfawit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
encrypted = "" #временные данные
for letter in text:
    nam = alfawit.find(letter) #функция обращается к переменной алфавить ищет совпадения, возвращает индекс этой буквы
    new_nam = nam + 1
    if letter in alfawit: #если буква в алфавите, сохранили в инкриптед и приплюсовали новый номер(new_nam)
        encrypted = encrypted + alfawit[new_nam] #здесь буква после смещения
    else:
        encrypted = encrypted + letter #если буквы в алфавите нет, то просто присплюсовали значение которое есть значально в сообщении. Выдаст цифру символ, который был изначально в сообщении

print("Ваше сообщение: ",encrypted)

