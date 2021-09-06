my_file = open('text_6.txt', 'r', encoding="utf-8")
out_dict = {}
for stroka in my_file:
    list_1 = stroka.split(':')
    predmet = list_1[0]
    vremya = sum(map(int, ''.join([znak for znak in list_1[1] if znak == ' ' or '9' >= znak >= '0']).split()))
    out_dict[predmet] = vremya
print(out_dict)
my_file.close()
