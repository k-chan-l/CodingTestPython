'''
용액
산성 =  양의 정수
알칼리 = 음의 정수

임의의 두종류의 용액을 선택해 두 값의 합이 가장 0에 가까운 혼합용액을 만들어라
정렬해서 값을 하나 고르고 2진탐색으로 그 값이 0에 가까워지는 다른 숫자를 하나 찾는다.
그값을 다른 값이랑 비교해서 맞으면 갱신 아니면 날린다.
'''
import sys
import bisect
input = sys.stdin.readline
INF = 10**10
def solve():
    n = int(input())
    liquids = list(map(int, input().rstrip().split()))
    new_liquid = INF
    liquid = ()
    for idx, v in enumerate(liquids[:-1]):
        x = bisect.bisect_left(liquids, -v, idx+1)
        # x가 n을 넘겼다 -> 해당 목록에는 겹치는게 없다.
        if x >= n:
            x -= 1
        # 같다 -> 0이 되는 값을 찾았다.
        elif -v == liquids[x]:
            print(v, liquids[x]) #정렬 되어있기 때문에 v는 항상 x보다 작다
            return
        elif x-1 > idx and abs(liquids[x-1]+v) < abs(liquids[x]+v):
            x -= 1
        if abs(v+liquids[x]) < new_liquid:
            new_liquid = abs(v+liquids[x])
            liquid = (v, liquids[x])
    print(liquid[0], liquid[1])
solve()