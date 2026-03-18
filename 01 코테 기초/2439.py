import sys
input = sys.stdin.readline

def solve():
    count = int(input())
    for i in range(count) :
        for j in range(count - i - 1) :
            print(' ',end='')
        for j in range(i + 1) :
            print('*',end='')
        print('')
solve()