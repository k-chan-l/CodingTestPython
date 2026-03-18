def solve() :
    a, b = map(int, input().split())
    if a > b :
        b, a = a, b
    elif a == b:
        print(0)
        return
    print(b - a - 1)
    for i in range(a + 1, b) :
        print(i, end=' ')
solve()