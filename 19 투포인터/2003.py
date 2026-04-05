'''
수들의 합 2

n개의 수로된 수열에서 연속된 수열의 합이 m이되는 경우의 수를 구하기
'''
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    ed = 0
    sum = 0
    answer = 0
    for st in arr:
        while ed < n and sum < m:
            sum += arr[ed]
            ed += 1
        if sum == m:
            answer += 1
        sum -= st
    print(answer)
solve()