# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

x, y = input().split()
comb = list(combinations_with_replacement(''.join(sorted(x)), int(y)))

for i in range(len(comb)):
    for j in range(int(y)):
        print(comb[i][j], end='')
    print()

