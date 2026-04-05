'''
멀티버스 II
M개의 우주에는 행성이 N개 있다.
균등한 우주의 쌍이 몇개인지 확인하려 한다.

균등한 쌍의 개수 x를 구해야한다. 각 쌍들의 순위를 매긴다. 이걸 튜플로 만들어서 딕셔너리에 넣는다. 2개 이상인 개수만 센다
'''
import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().rstrip().split())
    multiverse = []
    for i in range(m):
        multiverse.append(list(map(int, input().rstrip().split())))
    ordered = {}
    for i in range(m):
        uni_order = sorted(list(set(multiverse[i])))
        rank = {v:idx for idx, v in enumerate(uni_order)}
        order = tuple(rank[j] for j in multiverse[i])
        ordered[order] = ordered.get(order, 0) + 1
    count = 0
    for i in ordered.values():
        count += (i * (i-1))//2
    print(count)
solve()