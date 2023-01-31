import csv

lists = []
sumCol = [0,0,0]
listB = []


""" with open("./Input.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    sumRow = int(row[0])+int(row[1])
    sumCol[0]+=int(row[0])
    sumCol[1]+=int(row[1])
    sumCol[2]+=sumRow
    lists.append(f'{row[0]+row[1]}{sumRow}')

lists.append(sumCol)
print(lists) """

with open("./Input.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    sumRow = int(row[0])+int(row[1])
    sumCol[0]+=int(row[0])
    sumCol[1]+=int(row[1])
    sumCol[2]+=sumRow
    listB.append(int(row[0]))
    listB.append(int(row[1]))
    listB.append(int(row[0])+int(row[1]))
    #print(listB)
    lists.append(listB)
    listB.clear

    

lists.append(sumCol)
print(lists)

with open('./Output.csv', 'w') as file:
    writer = csv.writer(file)
    for row in lists:
        writer.writerow(row)

