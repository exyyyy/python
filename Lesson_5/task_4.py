from googletrans import Translator
orig_file = open('text_4.txt', 'r', encoding='utf-8')
trans_file = open('new_4.txt', 'w', encoding='utf-8')
stroka = orig_file.read()
trans_file.write(Translator().translate(stroka, dest='ru').text)
trans_file.close()
orig_file.close()
