import re

num = int(input())

for i in range(num):
    reg=input()
    try:
        re.compile(reg)
        is_valid=True
    except:
        is_valid=False
    print(is_valid)
