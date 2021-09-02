my_file = open('text_3.txt', 'r', encoding='utf-8')
i = 0
sum = 0
for line in my_file:
    list_1 = line.split(' ')
    if float(list_1[1]) < 20000:
        print(list_1[0])
    i += 1
    sum = sum + float(list_1[1])
print(f'Средняя зарплата {sum / i:.2f}')
my_file.close()
