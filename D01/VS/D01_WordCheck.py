# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數
import os
from urllib.request import urlretrieve

f = ''

try:
    with open("./D01//Data/Homework.txt", "r") as fh:
        f = fh.read()
        print(f)
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass

if len('Hello World') == len(f):
    print("YES")
else:
    print("No")