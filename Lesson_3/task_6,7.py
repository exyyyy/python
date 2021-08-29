def chk_word(word):
    tr = True
    for letter in list(word):
        if (letter >= 'a') and (letter <= 'z'):
            pass
        else:
            tr = False
        continue
    return tr


def int_func(string):
    word_list = string.split(" ")
    while word_list.count('') != 0:
        word_list.remove('')
    for word in word_list:
        if chk_word(word):
            word_list2.append(word)
    string = (' '.join(word_list2)).title()
    return string

word_list2 = []
print('Строка после обработки: ', int_func(input('Введите строку: ')))
