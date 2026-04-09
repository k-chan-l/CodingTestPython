'''
수직선 상에 있는 n개의 구간 에서 
A와 B사이에 포함되지 않은 부분을 모두 잘라냈을 때 남는 부분들의 길이의 합을 구하라
(a,b)구간의 값의 합이 k가 되는 ab를 구하라
a를 늘린다 값을 줄인다.
b를 늘린다 값을 늘린다.
투포인터로 가능하다.
시간을 줄이기 위해서는? 모든 라인의 구간별 합을 따로 정리
'''
import sys
input = sys.stdin.readline
INF = 10**6
def solve():
    n, k = map(int, input().rstrip().split())
    diff = [0]*(INF+1)
    min_line = (INF+1)
    max_line = 0
    for _ in range(n):
        st,ed = map(int, input().rstrip().split())
        diff[st] += 1
        diff[ed] -= 1
        min_line = min(min_line, st)
        max_line = max(max_line, ed)
    lines = []
    length = 0
    for i in diff[:max_line]:
        length += i
        lines.append(length)
    st = 0
    ed = 0
    size = 0
    while ed <= max_line and st <= ed:
        if size == k:
            print(st, ed)
            return
        elif size > k:
            size -= lines[st]
            st += 1
        else:
            if ed == max_line:
                break
            size += lines[ed]
            ed += 1
    print(0, 0)
solve()