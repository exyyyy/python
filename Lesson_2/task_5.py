rating = [7, 5, 3, 3, 2]
n = 0
m = 0
print("Начальный рейтинг ", rating)
print("Выход по вводу значения, отличного от цифры")
try:
    while (str(n).isdigit() == True) and (m <= 9) and (m >= 0):
        n = input("Введите балл от 0 до 9: ")
        m = int(n)
        i = 0
        for el in rating:
            if m <= el:
                i = i + 1
            else:
                break
        rating.insert(i, m)
        print(rating)
except:
    print("Конечный рейтинг ", rating)
