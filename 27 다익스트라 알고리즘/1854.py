'''
K번째 최단경로 찾기

k번째 최단경로를 구하는문제
일반적인 다익스트라다와 다르게, 그 다음 해를 구할수 있는 방법을 구해야한다.
어떻게? 값이 커지면 넘기지 말고 다음 값으로 넘긴다? -> 이걸 힙으로 구현? 최대큐로 구하고, 20개 넘어가면 컷,
n번째 값을 구하려면?
1. costs 내부를 pq 최대큐로 구현
2. 
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**8

def solve():
    n, m, k = map(int, input().rstrip().split())
    costs = [[] for i in range(n+1)]
    links = [[] for i in range(n+1)]

    for i in range(m):
        s_node, e_node, cost = map(int, input().rstrip().split())
        links[s_node].append((e_node, cost))
    
    pq = []
    heapq.heappush(pq,(0, 1)) # cost, s_node
    heapq.heappush(costs[1],0) # costs에 최소값 구현

    while pq:
        cost, cur_node = heapq.heappop(pq)
        if len(costs[cur_node]) >= k and -costs[cur_node][0] < cost:
            continue
        
        for i in links[cur_node]:
            next_node, add_cost = i
            next_cost = add_cost + cost

            if len(costs[next_node]) >= k and -costs[next_node][0] <= next_cost:
                continue
            heapq.heappush(costs[next_node], -next_cost)
            if len(costs[next_node]) > k:
                heapq.heappop(costs[next_node])
            heapq.heappush(pq, (next_cost, next_node))
    for i in costs[1:]:
        if len(i) != k:
            print(-1)
        else :
            print(-i[0])
solve()
