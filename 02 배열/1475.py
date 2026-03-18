import sys
input = sys.stdin.readline

def solve():
    arr = [0] * 10
    num = input().rstrip()
    for a in num :
        arr[int(a)] += 1
    max_num = max(arr[:6]+arr[7:9])
    aver = (arr[6] + arr[9] + 1)// 2
    if max_num >= aver:
        print(max_num)
    else :
        print(aver)
solve()