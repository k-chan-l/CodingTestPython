import sys
input = sys.stdin.readline

def solve() :
    count = int(input())
    for i in range(count) :
        for j in range(count) :
            if i <= j :
                print('*', end='')
        print('')
solve()