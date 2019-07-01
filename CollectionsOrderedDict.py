# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num = int(input())
dic = {}

def price(line):
    return(''.join(i for i in line if i.isdigit()))

for i in range(num):
    line = input()
    item = line.replace(" "+str(price(line)),"")
    if item in dic.keys():
        total = int(dic[item]) + int(price(line))
        dic[item] = total
    else:
        dic[item] = price(line)

for keys,values in dic.items():
    print(keys, values)

