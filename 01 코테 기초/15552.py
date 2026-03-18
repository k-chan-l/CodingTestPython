import sys
input = sys.stdin.readline

def solve() :
    count = int(input())
    for i in range(count):
        a, b = map(int, input().split())
        print(a + b)
solve()