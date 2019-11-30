# 「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址：https://www.w3.org/TR/PNG/iso_8859-1.txt 或任一個 .txt 的檔案網址
import os
from urllib.request import urlretrieve

os.makedirs('.\D01\Data', exist_ok=True)
try:
    urlretrieve("https://www.w3.org/TR/PNG/iso_8859-1.txt",".\D01\Data\Homework.txt")
except:
    print("error!")



