# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".
x= input("Введите четырехзначное число: ")
if x[0:1]==x[3:4] and x[1:2]==x[2:3]:
    print("true")
else: print ("Folse")