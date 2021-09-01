def fact(z):
    for el1 in range(1, z+1):
        yield el1


try:
    f = 1
    n = int(input('Введите целое число > 0: '))
    if n > 0:
        for el in fact(n):
            f = f * el
            print(f'{el}! = {f}')
    else:
        print('Отрицательное число!')
except ValueError:
    print('Некорректные входные данные!')