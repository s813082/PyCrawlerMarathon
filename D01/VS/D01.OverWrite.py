# 將「Hello World」字串覆寫到 Homework.txt 檔案
import os
from urllib.request import urlretrieve

f = ''

with open("./D01/Data/Homework.txt", "w") as fh:
    fh.write("Hello World")

try:
    with open("./D01//Data/Homework.txt", "r") as fh:
        f = fh.read()
        print(f)
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass    