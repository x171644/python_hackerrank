# Enter your code here. Read input from STDIN. Print output to STDOUT

ls = []
for i in range(3):
    num = [int(x) for x in input().split()]
    ls.extend(num)

print(pow(ls[0],ls[1]))
print(pow(ls[0],ls[1],ls[2]))
