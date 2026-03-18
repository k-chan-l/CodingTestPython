import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    girls = [0] * 6; boys = [0] * 6
    count = 0
    for i in range(n):
        s, y = map(int, input().split())
        if s == 0 :
            girls[y - 1] += 1
        else :
            boys[y - 1] += 1
    for i in girls :
        count += (i + k - 1) // k
    for i in boys :
        count += (i + k - 1) // k
    print(count)
solve()