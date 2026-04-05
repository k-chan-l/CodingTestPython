'''
부분합

10000이하의 자연수로 이루어진 수열 중 연속된 수들의 부분합중에 그합이 S이상이 되는것중 가장 길이가 짧은것의 길이를 반환
'''
import sys
input = sys.stdin.readline

def solve():
    n, s = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    ed = 0
    sum = 0
    answer = n+1
    for st in range(n):
        if st > 0:
            sum -= arr[st-1]
        while ed < n and sum < s:
            sum += arr[ed]
            ed += 1
        if sum >= s:
            length = ed - st
            if answer > length:
                answer = length
    if answer == n+1:
        print(0)
    else:
        print(answer)
solve()