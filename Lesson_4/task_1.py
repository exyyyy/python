from sys import argv

try:
    script_name, vyrabotka, stavka, premiya = argv
    if 0 < float(vyrabotka) < 744:
        if float(stavka) > 0:
            if float(premiya) >=0:
                zp = (float(vyrabotka) * float(stavka)) * (100 + float(premiya)) / 100
                print(f'Заработная плата сотрудника: {zp:.2f} у.е.')
            else:
                print('Некорректное значение премиальных. Введите премиальные в %')
        else:
            print('Некорректная ставка')
    else:
        print('Некорректная выработка. Человек не может столько работать в месяц!')
except ValueError:
    print("Некорректные входные параметры!")
