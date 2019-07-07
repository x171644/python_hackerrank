x, y = map(int, input().split()) 

score = []
for _ in range(y):
    score.append(map(float,input().split()))

for i in zip(*score):
    print(sum(i)/len(i))
