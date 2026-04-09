'''
휴게소 세우기

휴게소를 n개 가지고 있는데 고속도로의 시작에서 떨어져있는지로 주어진다.
휴게소를 m개 더 세우려고 하는데, 이때 휴게소 사이의 거리의 최대값을 최소로 하려고한다면 어떻게 해야하는가?

떨어진 거리의 최대값을 정하고 그값에 맞춰서 배치
{200, 701, 800}

'''
import sys
input = sys.stdin.readline

def is_possible(x, dist, limit): # 가능해도 x를 줄여야함
    count = 0
    for i in dist:
        count += (i+x-1)//x #x가 줄어들면 count가 커짐
    return limit >= count # 구간의 개수가 작냐? 구간을 늘려야돼냐? 구간을 늘릴려면 x를 줄여야한다. 구간과 같아도 거리를 줄이기 위해서, 통제할 필요가 있다.

def solve():
    n, m, l = map(int, input().rstrip().split())
    arr = sorted(list(map(int, input().rstrip().split())), reverse=True)
    dist = []
    for a in arr:
        dist.append(l-a)
        l = a
    dist.append(l)

    st = 1
    ed = max(dist)
    mid = (ed-st)//2 +st
    # x의 값을 구하기
    while st <= ed: # 모든 구간을 x로 통일했을때, 구간의 개수가 작냐? 구간을 늘려야돼냐?
        if is_possible(mid, dist, n+m+1):
            ed = mid-1
            mid = (ed-st)//2 +st
        else:
            st = mid+1
            mid = (ed-st)//2 +st
    print(st)
solve()
