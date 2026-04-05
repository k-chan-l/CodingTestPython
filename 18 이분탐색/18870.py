'''
좌표압축
현재 값보다 작은 값들의 종류수(중복을 제외 한)
1. 정렬한다.
2. 중복을 제거한다. list로 변환
3. 이분탐색으로 해당값보다 작은 값들의 좌표를 구한다.
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    answer = []
    table = []
    for i in sorted(arr):
        if not table or table[-1] != i:
            table.append(i)
    for i in arr:
        answer.append(bisect.bisect_left(table, i))
    print(' '.join(map(str,answer)))
solve()