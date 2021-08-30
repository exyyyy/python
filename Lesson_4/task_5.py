from functools import reduce
from random import randrange
list1 = [randrange(100, 1000, 2) for n in range(0, 10)]
print('Сгенерированный список', list1)


def my_func(a, b):
    return a * b


print(f'Произведение элементов списка = {reduce(my_func, list1):.3e}')
