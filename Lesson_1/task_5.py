vyr = int(input("Веедите выручку фирмы: "))
izd = int(input("Введите издержки фирмы: "))
if vyr == izd:
    print("Фирма вышла в ноль")
elif vyr < izd:
    print("Фирма ушла в убыток")
elif vyr > izd:
    print("Фирма вышла в прибыль!")
    rent = (vyr - izd) / vyr
    print("Рентабельность фирмы {:.0f}%".format(rent * 100))
    sotr = int(input("Сколько сотрудников в фирме? "))
    print("Прибыль фирмы на одного сотрудника равна {:.2f} у.е.".format((vyr - izd) / sotr))
