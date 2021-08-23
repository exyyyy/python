spisok = str(input("Введите строку:")).split(" ")
for i, element in enumerate(spisok, 1):
    print(i, element[:10])
