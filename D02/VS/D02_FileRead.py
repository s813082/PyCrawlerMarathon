# 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異
import csv
import os
from urllib.request import urlretrieve

f = ''
with open("D02\Data\example.csv", "r",encoding="utf-8") as fh:
    f = fh.read()
    print(f)