import csv
from dataclasses import dataclass

dataset1 = []
dataset2 = []

with open("dwarf_stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1 = dataset1[0]
star1 = dataset1[1:]

header2 = dataset2[0]
star2 = dataset2[1:]

headers = header1+header2
starsdata = []
for index,data_row in enumerate(star1):
    starsdata.append(star1[index]+star2[index])
with open("merge.csv",'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(starsdata)