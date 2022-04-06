import csv
import re

b=""
with open('E://EnWords.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i in reader:
        Sum = 0
        s = ""
        for char in i[0]:
            Sum += ord(char)-96
        if Sum == 100:
            print(i[0]+"("+re.sub('[^\u4e00-\u9fa5]+','',i[1])+")")
            b= b+ re.sub('[^\u4e00-\u9fa5]+','',i[1])+"/"
            for char in i[0]:
                s=s+"+"+str(char.upper())
            print(s[1:])
            s=""
            for char in i[0]:
                s = s + "+" + str(ord(char)-96)
            print(s[1:]+"=100%")
            print(re.sub('[^\u4e00-\u9fa5]+','',i[1])+"能夠 100％ 的影響我們的生活，或者說能夠使我們的生活達到 100% 的圓滿！")
            s=""
print(b)

