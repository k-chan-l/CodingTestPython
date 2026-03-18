import sys
input = sys.stdin.readline

def solve() :
    count = int(input())
    for a in range(count) :
        print(' ' * a + '*' * (2 * (count - a) - 1))
    for a in range(1, count) :
        print(' ' * (count - a - 1) + '*' * (2 * a + 1))
solve()
