import csv

import pandas as pd
my_dic = pd.read_excel('8638.xlsx', index_col=0).to_dict()
dict_2 = pd.read_excel('compare.xlsx', index_col=0).to_dict()

dict_3 = []

for key, value in my_dic.items():
    for things in value.items():
        dict_3.append(things)

dict_4 = []
for key, value in dict_2.items():
    for things in value.items():
        dict_4.append(things)


dict_3 = dict(dict_3)
dict_4 = dict(dict_4)


dict_3.update(dict_4)


with open('output.csv', 'w') as output:
    writer = csv.writer(output, lineterminator = '\n')
    for key, value in dict_3.items():
        writer.writerow([key, value])

























