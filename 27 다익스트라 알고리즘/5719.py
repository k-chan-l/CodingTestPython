'''
최단경로에 포함되지 않는? 다익스트라를 2번해야 되네, 그냥 한번 + 경로 추적 그다음 한번더
중간에 모아지는게 빠진거 같으니, paths를 각 노드수마다 기록하고, 노드에 모으는 작업이 필요
집합을 사용해서 메모리관리
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def solve():
    while True:
        n, m = map(int, input().rstrip().split())
        if n == 0 and m == 0:
            break
        start_node, end_node = map(int, input().rstrip().split())
        costs = [INF]*n
        links = [[] for i in range(n)]
        paths = [set() for i in range(n)]

        for i in range(m):
            s_node, e_node, cost = map(int, input().rstrip().split())
            links[s_node].append((cost, e_node))
        
        pq = []
        costs[start_node] = 0
        heapq.heappush(pq, (0, start_node))
        #최단 경로 계산
        while pq:
            cost, cur_node = heapq.heappop(pq)
            if costs[cur_node] < cost:
                continue

            for add_cost, next_node in links[cur_node]:
                next_cost = add_cost + cost
                if next_cost == costs[next_node]:
                    paths[next_node].update(paths[cur_node])
                    paths[next_node].add((cur_node, next_node))
                if costs[next_node] <= next_cost :
                    continue
                paths[next_node] = set()
                paths[next_node].update(paths[cur_node])
                paths[next_node].add((cur_node, next_node))
                costs[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))
        min_path = paths[end_node]
        #거의 최단경로 계산
        pq = []
        costs = [INF]*n
        costs[start_node] = 0
        heapq.heappush(pq, (0, start_node))
        
        while pq:
            cost, cur_node = heapq.heappop(pq)
            if costs[cur_node] < cost:
                continue

            for add_cost, next_node in links[cur_node]:
                if (cur_node, next_node) in min_path:
                    continue
                next_cost = add_cost + cost
                if costs[next_node] <= next_cost :
                    continue
                costs[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))
        if costs[end_node] == INF:
            print(-1)
        else:
            print(costs[end_node])
solve()