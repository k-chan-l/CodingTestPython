import sys
input = sys.stdin.readline


def solve() :
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    count = 0
    end = n-1
    arr.sort()
    for i in range(n-1):
        num = x - arr[i]
        for j in range(end,0,-1):
            if i >= j :
                break
            if num == arr[j] :
                count += 1
                end = j - 1
                break
            elif num > arr[j] :
                end = j
                break

    print(count)
solve()