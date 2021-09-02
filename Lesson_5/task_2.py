i = 0
my_file = open('task_1.txt', 'r', encoding='utf-8')
for line in my_file:
    i += 1
    slova = line.split(" ")
    while slova.count('') != 0:
        slova.remove('')
    while slova.count('\n') != 0:
        slova.remove('\n')
    print(f'В {i} строке {len(slova)} слов(о/а)')
my_file.close()
