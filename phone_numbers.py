import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    next(rows)
    contacts_list = list(rows)

name_list = []

for el in contacts_list:
    name = el[:3]
    f_name = ' '.join(name)
    l_name = f_name.split(' ')
    while '' in l_name:
        l_name.remove('')
    name_list.append(l_name)

for el in range(len(name_list)):
    contacts_list[el][:3] = name_list[el][:3]

print(name_list)
