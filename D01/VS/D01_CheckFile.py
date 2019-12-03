# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
import os
from urllib.request import urlretrieve
path = './D01/Data'
dirs = os.listdir(path)
files = []

for file in dirs:
    files.append(file)

if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')