import random
list1 = [random.randint(0, 11) for i in range(11)]
print('Исходный список: ', list1)
list2 = [n for n in list1 if list1.count(n) == 1]
print('Конечный список', list2)
