import csv
import random

with open('booksnew.csv','r', encoding='windows 1251') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    book = list(reader)
    count = 0
# -------
print(f'количество записей: {len(book[1:])}')
# -------
for row in book:
    if len(row[1]) > 30: count += 1
print(f'Название строка длиннее 30 символов: {count}')

#-------

nfile = open('booksnew.csv', encoding='windows-1251')
header = nfile.readline()
line = list(nfile)

author = input("Enter the author's name: ")
bookFind = []
x = '2015'
y = '2018'
for i in range(0, len(line[1:])):
    splited = line[i].split(';')  # создавать разделители между категориями
    year = splited[6][6:10]  # выбирать год

    if author in line[i]:
        if x in line[i] or y in line[i]:
            bookFind.append(splited[1] + " " + year)
print(bookFind)
#------
author_file = open('Author.txt', 'wt', encoding='utf8')
start = random.randint(1, len(line) - 20)  # создавать случайные начальные и конечные точки
stop = start + 20
for i in range(start,stop):
    splited = line[i].split(';') #создавать разделители между категориями
    year = splited[6][6:10] #создать разделитель дня, месяца, года
    author_file.write("ФИО: " + splited[4] + "\n" + "Название: " + splited[1] + " " + year + "\n\n")
author_file.close()
#------

with open('booksnew.csv', encoding='windows 1251') as file:
    header = file.readline()
    deleDup = dict.fromkeys(file)
    print("Длина списка книг не дублируется:", len(list(deleDup)))













