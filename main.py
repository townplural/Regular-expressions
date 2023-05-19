from pprint import pprint
import re
import csv
from regular_expressions import pattern_fio, pattern_phone, subst_phone, pattern_add_phone, subst_add_phone

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    order = contacts_list.pop(0)
pprint(contacts_list)
list_of_lists = []
contacts_dict = {}
list_of_rows = []
names_list = []
duplicates = []

for i in contacts_list:
    i[-2] = re.sub(pattern_phone, subst_phone, i[-2])  # Приведение телефонов к нормальному виду
    i[-2] = re.sub(pattern_add_phone, subst_add_phone, i[-2])  # Приведение добавочных телефонов к нормальному виду
    text = ''
    for a in i:
        text += a
        text += ' '
    list_of_rows.append(text)
# Обнаружение ФИО по заданному параметру
for i in list_of_rows:
    contacts_dict[re.findall(pattern_fio, i)[0]] = []
# добавление всех ФИО в список
for i in contacts_dict:
    names_list.append(i)
# Обнаружение повторений и добавление их в список
for i in range(len(names_list)-1):
    for j in range(i+1, len(names_list)):
        if names_list[i][0] == names_list[j][0] and names_list[i][1] == names_list[j][1]:
            duplicates.append(names_list[j])
# Удаление повторяющихся ФИО из словаря
for i in duplicates:
    contacts_dict.pop(i)
# Присвоение ФИО остальной информации
for a, c in contacts_dict.items():
    for b in contacts_list:
        if a[0] in b[0]:
            c.append(b[3:])
# присвоение первому списку значений которые есть во втором но нет в первом
for key, value in contacts_dict.items():
    if len(value) > 1:
        for i in range(4):
            if value[0][i] == '' and value[1][i] != '':
                value[0][i] = value[1][i]
# Удаление не нужных списков
for i in contacts_dict:
    if len(contacts_dict[i]) > 1:
        contacts_dict[i].pop(1)
# Составление списка списков
for keys, values in contacts_dict.items():
    end_list = []
    for a in keys:
        end_list.append(a)
    for b in values:
        for c in b:
            end_list.append(c)
    list_of_lists.append(end_list)


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(list_of_lists)
