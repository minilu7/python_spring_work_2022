f = open("message.txt", "r", encoding="utf8")
text = f
alfawit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

n = len(alfawit)
for letter in range(n):
    shifr = ""

    for c in f:
        if c != " ":
            shifr += alfawit[(alfawit.index(c)+letter)%33]
        else:
            shifr += c
print (letter, t)