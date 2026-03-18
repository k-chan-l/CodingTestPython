import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    arr = list(map(int, input().split()))
    v = int(input())
    count = 0
    for a in arr :
        if a == v :
            count += 1
    print(count)
solve()