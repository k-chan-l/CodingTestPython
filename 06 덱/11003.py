import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, l = map(int, input().rstrip().split())
    a = list(map(int,input().rstrip().split()))
    dq = deque()
    for i, x in enumerate(a):
        if dq and dq[0][1] < i - l + 1:
            dq.popleft()
        while dq and dq[-1][0] > x:
            dq.pop()
        dq.append([x, i])
        print(dq[0][0], end=' ')
solve()
    # d1 = A(1-l+1) ~ A1 
    # 1 2 3 4 5 6
    # 0 
    # 0 0
    # 0 0 0 
    # 0 0 0 0
    #   0 0 0 0
    #     0 0 0 0
    # 모노톤으로 낮은거만 살리기(인덱스 같이 저장해서 날리기)