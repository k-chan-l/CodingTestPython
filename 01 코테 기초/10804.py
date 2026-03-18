def solve() :
    cards = list(range(1, 21))
    for i in range(10) :
        a, b = map(int, input().split())
        change = cards[a-1:b]
        change.reverse()
        cards[a-1:b] = change
    for i in cards :
        print(i, end=' ')
solve()