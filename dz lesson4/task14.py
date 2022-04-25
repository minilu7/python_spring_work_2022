


mass = [1,2,17,16,30,51,2,70,3,2]
result= []
index = 0
a = int(input ("Введите число: "))

for i in mass:
    index =  index + 1
    if a == i:
        result.append(index - 1)
    if (mass.count(a) == 1)| (mass.count (a) == 0):
        print ("Количество вхождений в массив меньше требуемого")
    else:
        if len(result) > 2:
            print(result[1], result[2])



