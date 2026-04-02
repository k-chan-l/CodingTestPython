'''
준영이는 매일 서울에서 포천까지 출퇴근을 한다. 하지만 잠이 많은 준영이는 늦잠을 자 포천에 늦게 도착하기 일쑤다.
돈이 많은 준영이는 고민 끝에 K개의 도로를 포장하여 서울에서 포천까지 가는 시간을 단축하려 한다.

문제는 N개의 도시가 주어지고 그 사이 도로와 이 도로를 통과할 때 걸리는 시간이 주어졌을 때 최소 시간이 걸리도록 하는 K개의 이하의 도로를 포장하는 것이다.
도로는 이미 있는 도로만 포장할 수 있고, 포장하게 되면 도로를 지나는데 걸리는 시간이 0이 된다.
또한 편의상 서울은 1번 도시, 포천은 N번 도시라 하고 1번에서 N번까지 항상 갈 수 있는 데이터만 주어진다.

1번에서 N번 까지 가는데 걸리는 시간을 최소화 하는문제, 단, K번 포장을 할수 있는 기회가 주어지는데, 이걸하면 걸리는 시간을 0으로 만들 수 있다.
포장을 한 후 거리 비용을 계산 but 우선순위 계산이 필요하다.
K번 포장이 변수, 이걸 어떻게 해야하나?
다익스트라 내부에 포장을 넘긴다. 우선순위큐 + BFS 이것 말고는 없을듯
 수 N(1 ≤ N ≤ 10,000)과 도로의 수 M(1 ≤ M ≤ 50,000)과 포장할 도로의 수 K(1 ≤ K ≤ 20)가 공백으로 구분되어 주어진다.
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def solve():
    n, m, k = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]
    costs = [[INF]*(n+1) for i in range(k+1)]
    for i in range(m):
        s_node, e_node, cost = map(int, input().rstrip().split())
        links[s_node].append((e_node, cost))
        links[e_node].append((s_node, cost))
    
    pq = []
    costs[0][1] = 0
    heapq.heappush(pq, (0, 0, 1)) # cost, 포장횟수, 현재위치

    while pq:
        cost, cover, cur = heapq.heappop(pq)
        if cost > costs[cover][cur]:
            continue
        
        for i in links[cur]:
            next_node, add_cost = i
            next_cost = add_cost + cost

            if cover + 1 <= k and cost < costs[cover+1][next_node]:
                costs[cover+1][next_node] = cost
                heapq.heappush(pq, (cost, cover+1, next_node))

            if next_cost >= costs[cover][next_node]:
                continue
            costs[cover][next_node] = next_cost
            heapq.heappush(pq, (next_cost, cover, next_node))
    result = INF
    for i in costs:
        if result > i[n]:
            result = i[n]
    print(result)
solve()