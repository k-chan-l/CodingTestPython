odds = []
for i in range(7) :
    a = int(input())
    if a % 2 == 1 :
        odds.append(a)
if len(odds) == 0 :
    print(-1)
else :
    print(sum(odds))
    odds.sort()
    print(odds[0])