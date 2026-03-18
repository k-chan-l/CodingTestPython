import sys
input = sys.stdin.readline

def solve():
    k = int(input())
    arr = []
    for a in range(k) :
        x = int(input())
        if x == 0 :
            arr.pop()
        else :
            arr.append(x)
    print(sum(arr))
solve()
