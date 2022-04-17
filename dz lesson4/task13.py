#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
mass = [1,3,5,7,9,11,13,15,17,19]
z=0
result = []
for x in mass:
    x = mass[z]
    out = int(x)+int(1)
    z += 1
    result.append(out)
print(result)
