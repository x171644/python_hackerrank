num = int(input())

def compare():
    a = int(input())
    x = set([i for i in input().split(" ")])
    b = int(input())
    y = set([i for i in input().split(" ")])
    print(x.issubset(y))

for i in range(num):
    compare()
