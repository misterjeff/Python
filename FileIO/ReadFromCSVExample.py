import csv

with open('C:\\Users\\POSITIVITY6510\\Desktop\\StackDetailExample.csv', newline='') as csvfile:
##    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
##    for row in spamreader:
##        print(' | '.join(row))
    data = list(csv.reader(csvfile))

for x in range(1, 100):
    row = ''
##    for y in range(len(data[x])):
##        row = row + data[x][y] + ' | '
##    print(row)
    print(data[x])
