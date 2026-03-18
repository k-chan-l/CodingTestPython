import sys
input = sys.stdin.readline

def solve():
    count = int(input())

    for a in range(1, count + 1) :
        print('*' * a + ' ' * (count - a) * 2+ '*' * a)
    for a in range(count) :
        print('*' * (count -1 - a) + ' ' * (a + 1) * 2 + '*' * (count - 1 - a))
solve()