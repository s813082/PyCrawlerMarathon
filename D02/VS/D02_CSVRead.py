import csv
import os
from urllib.request import urlretrieve

List =[]
f = ''
with open('D02\Data\example.csv',newline='',encoding='utf-8')as csvfile:
    f = csv.reader(csvfile)

    for row in f:
        List.append(row)

    print(List[1])
