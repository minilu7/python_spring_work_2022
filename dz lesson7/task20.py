f = open("import_this.txt", "r", encoding="utf-8")
stroki = f.readlines()
revers = stroki[::-1]

for i in revers:
    print(i)
f.close()