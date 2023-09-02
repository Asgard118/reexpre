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

pattern = re.compile(r"(\+?(\d{1,4}?)[-.\s]?\(?(\d{3}?)\)?[-.\s]?(\d{1,4})[-.\s]?(\d{2})[-.\s]?(\d{2})[-.\s]?)")
pattern2 = re.compile(r"(\+?(\d{1,4}?)[-.\s]?\(?(\d{3}?)\)?[-.\s]?(\d{1,4})[-.\s]?(\d{2})[-.\s]?(\d{2})[-.\s]?\(?\(?доб\.\s?(\d{4})\)?)")
subs_pattern = r"+7(\3)\4-\5-\6"
subs_pattern2 = r"+7(\3)\4-\5-\6 доб.\7"
for el in contacts_list:
    el[5] = re.sub(pattern, subs_pattern, el[5])
    el[5] = re.sub(pattern2, subs_pattern2, el[5])    
unique_dict = {}

for item in contacts_list:
    key = tuple(item[:2])

    if key in unique_dict:
        unique_dict[key].extend(item[2:])
    else:
        unique_dict[key] = item

almost_done = list(unique_dict.values())

for sublist in almost_done:
    sublist[:] = [item for item in sublist if item != '']

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(almost_done)