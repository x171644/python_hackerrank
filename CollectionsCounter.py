import collections

snum = int(input())
shoes = collections.Counter(map(int, input().split()))
cust = int(input())
total = 0

for i in range(cust):
    size, price = map(int, input().split())
    if shoes[size]: 
        total += price
        shoes[size] -= 1

print(total)
