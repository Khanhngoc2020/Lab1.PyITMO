file = open('booksnew.csv', encoding='windows-1251')
header = file.readline()

bookName = []
amount = []

line = file.readline()
while line != "":

    line_list = line.split(';')
    bookName.append(line_list[1])
    amount.append(line_list[10])
    line = file.readline()

for i in range(len(amount)):
    if amount[i] == "": amount[i] = "0"
for i in range(0,len(amount) - 1):
    for j in range(i + 1, len(amount)):
        if int(amount[i]) > int(amount[j]):
            tmp = amount[i]
            amount[i] = amount[j]
            amount[j] = tmp

            bname = bookName[i]
            bookName[i] = bookName[j]
            bookName[j] = bname
print("Записка самых популярных 20 книг:")
for i in range(20):
    print(bookName[i] + " - Инвентарный номер: " + amount[i])
file.close()