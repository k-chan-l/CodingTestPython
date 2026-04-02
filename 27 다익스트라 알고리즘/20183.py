'''
골목 대장 효성 효율성-2
N개의 노드를 시작값에서 목적지로 갈때 최대값의 최소비용을 사용해서 가는 방법

다익스트라 알고리즘을 이용해서 최소값을 구한다.
첫 줄에 교차로 개수 N, 골목 개수 M, 시작 교차로 번호 A, 도착 교차로 번호 B, 가진 돈 C 가 공백으로 구분되어 주어진다.
이어서 M 개의 줄에 걸쳐서 각 골목이 잇는 교차로 2개의 번호와, 골목의 수금액이 공백으로 구분되어 주어진다.
같은 교차로를 잇는 골목은 최대 한 번만 주어지며, 골목은 양방향이다.

이분탐색으로 각 골목의 최대 비용을 정의하고, 다익스트라로 그 비용만큼 순회, 실패하면 오른쪽, 성공하면, 왼쪽으로 넘긴다.
왼쪽으로 갔는데 실패했으면 오른쪽 값, 오른쪽 끝까지 갔는데 실패하면-1을 출력한다.
이분탐색 공부후 다시 보자
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def solve():
    n, m, a, b, c = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]
    

    for i in range(m):
        s_node, e_node, cost = map(int, input().rstrip().split())
        links[s_node].append((e_node, cost))
        links[e_node].append((s_node, cost))
    
    result = INF
    limit = c // 2
    div = limit
    while limit <= c and div != 0:
        costs = [INF] * (n+1)
        pq = []
        heapq.heappush(pq, (0, a)) # cost, start_node
        costs[a] = 0
        while pq:
            cost, s_node = heapq.heappop(pq)
            if costs[s_node] < cost:
                continue
            for i in links[s_node]:
                next_node, add_cost = i
                next_cost = cost + add_cost
                if next_cost > limit:
                    continue
                if costs[next_node] <= next_cost :
                    continue
                costs[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))
        div = div + 1 // 2
        if costs[b] == INF:
            limit += div
        else:
            result = limit
            limit -= div
    if result == INF:
        result = -1
    print(result)
solve()
