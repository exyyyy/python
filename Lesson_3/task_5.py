summ = 0
print("Для завершения программы в строке введите quit")
def number_list():
    global summ
    input_string = str(input("Введите список целых чисел через пробел: "))
    list1 = input_string.split(" ")
    while list1.count('') != 0:
        list1.remove('')
    for i in list1:
        try:
            i = int(i)
            summ = summ + int(i)
        except ValueError:
            print("Error! В строке присутствуют символы, отличные от цифр и пробелов!")
    print(summ)
    if input_string.find('quit') == -1:
        number_list()
    else:
        return print('Программа завершена.')

number_list()
