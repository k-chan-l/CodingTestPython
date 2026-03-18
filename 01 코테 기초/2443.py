import sys
input = sys.stdin.readline

def solve() :
    count = int(input())
    for i in range(count) :
        print(' ' * i + '*' * (2 * (count - i) - 1))
solve()