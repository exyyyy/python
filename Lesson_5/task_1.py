my_file = open('task_1.txt', 'w', encoding='utf-8')
state = True
print('Введите строки из слов через пробел.\nДля выхода введите пустую строку')
while state == True:
    new_str = input()
    if new_str != '':
        my_file.write(new_str + '\n')
    else:
        state = False
my_file.close()
