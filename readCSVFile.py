import csv
import re

target_my = open('x.txt', 'w')
with open('problems.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print line_count
        line_count = line_count + 1
        string = " ".join(row).replace('\r', ' ').replace('\n', ' ')
        string = re.sub(' +', ' ', string)
        target_my.write(string + "\n")
target_my.close()
