import json
file_1 = open('text_7.txt', encoding='utf-8')
file_out = open('task_7.json', 'w', encoding='utf-8')
my_dict = {line_of_file.split()[1] + ' ' + line_of_file.split()[0]:
               int(line_of_file.split()[2]) - int(line_of_file.split()[3]) for line_of_file in file_1}
aver = sum([int(znach) for znach in my_dict.values() if int(znach) > 0]) / len([znach for znach in my_dict.values() if int(znach) > 0])
my_list =[my_dict, {'average_profit':round(aver)}]
json.dump(my_list, file_out, ensure_ascii=False, indent=4)
file_1.close()
file_out.close()
