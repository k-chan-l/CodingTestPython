import sys
input = sys.stdin.readline

def solve() :
    arr = [0] * 10
    a = int(input())
    b = int(input())
    c = int(input())
    mul = a * b * c
    for a in str(mul) :
        arr[int(a)] += 1
    for a in arr :
        print(a)
solve()