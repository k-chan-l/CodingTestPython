'''
겹치는 건 싫어

같은 원소가 k개 이하로 들어있는 최장 연속 부분 수열의 길이를 구하라.
각 종류마다 최대 k개 이하
'''
import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    dup = [0]*100001

    ed = 0
    answer = 0
    count = 0

    for st in range(n):
        while ed < n and count <= k:
            dup[arr[ed]] += 1
            count = max(dup[arr[ed]], count)
            ed += 1
        dup[arr[st]] -= 1
        
        if ed == n and count > k:
            answer = max(answer, ed - st-1)
        elif ed == n and count <= k:
            answer = max(answer, ed - st)
        elif count > k:
            answer = max(answer, ed - st -1)
            if arr[ed-1] == arr[st]:
                count -= 1
        else:
            answer = max(answer, ed - st)
            if arr[ed] == arr[st]:
                count -= 1

    print(answer)
solve()