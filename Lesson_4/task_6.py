from itertools import count, cycle

try:
    string = input('Введите строку для повтора: ')
    n = input('Введите стартовое число: ')
    count_1 = count(int(n))
    cycle_1 = cycle(string)
    for x in range(5):
        print(next(count_1), ' ', next(cycle_1))
except:
    print('Ошибка входных данных!')