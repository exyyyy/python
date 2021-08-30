list1 = [n**3 if n % 2 == 0 else n * 100 for n in range(10, 21)]
print('Исходный список: ', list1)
list2 = [n for n in list1[1:] if n > list1[list1.index(n)-1]]
print('Конечный лист: ', list2)
