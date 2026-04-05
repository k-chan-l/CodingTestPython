'''
골목 대장 효성 효율성-2
N개의 노드를 시작값에서 목적지로 갈때 전체금액이 c원 이하일때, 한 간선의 최대값의 최소비용을 사용해서 가는 방법

이분탐색으로 각 골목별 최대 건널 수 있는 금액 x를 구한다.
x의 기본값은 c의 절반, 다익스트라로, 건널수 있는지여부를 확인한다. 건널수 있으면 x값을 내리고, 건널수 없으면 x값을 올린다.

'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def is_possible(n, st_node, ed_node, c, mid, links):
    # 다익스트라 우선순위 큐로 거리별로 정렬해서 비용계산, 최소비용이 아니면 패스
    dists = [INF]*(n+1) # 거리배열
    pq = []
    dists[st_node] = 0
    heapq.heappush(pq, (0, st_node))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost != dists[cur_node]:
            continue

        for next_node, add_cost in links[cur_node]:
            if add_cost > mid: #이 값이랑 같거나 작은 값만 통과 가능
                continue
            next_cost = add_cost + cur_cost
            if next_cost >= dists[next_node]:
                continue
            if next_cost > c:
                continue
            dists[next_node] = next_cost
            heapq.heappush(pq, (next_cost, next_node))
    return dists[ed_node] <= c

def solve():
    n, m, a, b, c = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]
    
    st = INF
    ed = 0

    for i in range(m):
        s_node, e_node, cost = map(int, input().rstrip().split())
        links[s_node].append((e_node, cost))
        links[e_node].append((s_node, cost))
        st = min(st, cost)
        ed = max(ed, cost)
    
    answer = -1
    while st <= ed:
        mid = (ed-st)//2 + st
        if is_possible(n, a, b, c, mid, links):
            answer = mid
            ed = mid - 1
        else:
            st = mid + 1
    print(answer)

solve()
