import sys
input = sys.stdin.readline

def solve() :
    count = int(input())
    for i in range(count) :
        print(' ' * (count - i - 1)  + '*' * (2 * i + 1))
    for i in range(count - 1) :
        print(' ' * (i + 1) + '*' * (2 * (count - i - 1) - 1))
solve()