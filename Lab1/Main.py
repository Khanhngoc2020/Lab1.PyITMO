import csv
import random
import array as arr
import re

with open('booksnew.csv','r', encoding='windows 1251') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    book = list(reader)
    count = 0
# # -------
    print(f'количество записей: {len(book[1:])}')
# # -------
    for row in book:
        if len(row[1]) > 30: count += 1
    print(f'Название строка длиннее 30 символов: {count}')

# #-------
    nfile = open('booksnew.csv', encoding='windows-1251')
    header = nfile.readline()
    line = list(nfile)
    author = input("Enter the author's name: ")
    bookFind = []
    x = str('2015')
    y = str('2018')
    for i in range(1, 9409):
        splited = line[i].split(';')  # создавать разделители между категориями
        take_date = splited[6].split()  # создать разделитель даты и времени в категории «Дата получения»
        year = take_date[0].split('.')  # создать разделитель дня, месяца, года

        if author in line[i]:
            if x in line[i] or y in line[i]:
                bookFind.append(splited[1] + " " + str(year[2]))
    print(bookFind)
#------
    author_file = open('Author.txt', 'wt', encoding='utf8')
    start = random.randint(1, 3000)  # создавать случайные начальные и конечные точки
    stop = random.randint(3001, 9409)
    count = 1
    for i in range(start,stop):
        splited = line[i].split(';') #создавать разделители между категориями
        take_year = splited[6].split() #создать разделитель даты и времени в категории «Дата получения»
        year = take_year[0].split('.') #создать разделитель дня, месяца, года
        author_file.write(str(count) + " " + "ФИО:" + splited[4] + "\n" + "Название:" + splited[1] + " " + year[2] + "\n\n")
        count += 1
        if count == 21: break #Если список дойдет до 21-го, цикл остановится.
    author_file.close()
#------
with open('booksnew.csv', encoding='windows 1251') as file:
    header = file.readline()
    deleDup = dict.fromkeys(file)
    print("Длина списка книг не дублируется:", len(list(deleDup)))















