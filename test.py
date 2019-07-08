import csv

with open('./data/executive_prep.csv', 'r', encoding='utf-8') as file:
    con = csv.reader(file, delimiter=',')
    for i, c in enumerate(con):
        print(i,c)