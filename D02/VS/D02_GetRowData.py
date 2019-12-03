import csv

# 開啟 CSV 檔案
with open('D02\data\example.csv', newline='', encoding = 'utf-8') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    Array = []
    Class1 = []
    Class2 = []
    Class3 = []
    Class4 = []
    Class5 = []
    ClassTime1 = []
    ClassTime2 = []
    ClassTime3 = []
    ClassTime4 = []
    ClassTime5 = []
    # 以迴圈輸出每一列
    for row in rows:
        # print(row)
        Array.append(row)
        
    Class1 = Array[1]
    Class2 = Array[2]
    Class3 = Array[3]
    Class4 = Array[4]
    Class5 = Array[5]
    
    for i in range(5,15):
        ClassTime1.append(Class1[i])
        ClassTime2.append(Class2[i])
        ClassTime3.append(Class3[i])
        ClassTime4.append(Class4[i])
        ClassTime5.append(Class5[i])