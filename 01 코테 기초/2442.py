import sys
input = sys.stdin.readline

def solve():
    count = int(input())
    for i in range(1, count + 1) :
        print(' '*(count - i) + '*' * i + '*' * (i - 1))
solve()