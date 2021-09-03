from random import randint
my_file = open('task_5.txt', 'w+', encoding='utf-8')
list_1 = []
summ = 0
for i in range(5):
    list_1.append(str(randint(1, 10)))
my_file.write(" ".join(list_1))
my_file.seek(0)
list_2 = my_file.read().split(' ')
for i in list_2:
    summ = summ + int(i)
print(f'Сумма чисел в файле {my_file.name} = {summ}')
my_file.close()
