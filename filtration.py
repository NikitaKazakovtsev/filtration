import re
from pprint import pprint
import csv

phon = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phon1 = r'+7(\2)-\3-\4-\5 \6\7'


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
def main(contact_list: list):
    list1 = list()
    for item in contact_list:
        name = ' '.join(item[:3]).split(' ')
        res = [name[0], name[1], name[2], item[3], item[4],re.sub(phon, phon1, item[5]),item[6]]
        list1.append(res)
    return union(list1)


def union(data: list):
    for con in data:
        first = con[0]
        last = con[1]
        for con1 in data:
            new_f = con1[0]
            new_l = con1[1]
            if first == new_f and last == new_l:
                if con[2] == "": con[2] = con1[2]
                if con[3] == "": con[3] = con1[3]
                if con[4] == "": con[4] = con1[4]
                if con[5] == "": con[5] = con1[5]
                if con[6] == "": con[6] = con1[6]
    res = list()
    for a in data:
        if a not in res:
            res.append(a)
    return res


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))