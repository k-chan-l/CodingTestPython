'''
최소비용 구하기2
A -> B까지의 최소 비용과 경로를 출력 하는문제 양방향 연결
A에서 시작하는 다익스트라다 알고리즘과, 경로를 저장한다.
1. 노드 만들기
2. 경로 저장할 배열 만들기
3. 비용을 저장할 배열 만들기
4. 다익스트라다 알고리즘 수행
5. 도착점을 기준으로 역산해서 경로 담기
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def solve():
    n = int(input().rstrip())
    m = int(input().rstrip())

    costs = [INF]*(n+1)
    path = [-1]*(n+1)
    links = [[] for i in range(n+1)]
    pq = []

    for i in range(m):
        start_node, end_node, cost = map(int, input().rstrip().split())
        links[start_node].append((end_node, cost))

    start, goal = map(int, input().rstrip().split())

    costs[start] = 0
    path[start] = start
    heapq.heappush(pq, (0, start)) #거리, 시작지

    while pq:
        cost, start_node = heapq.heappop(pq)
        if cost > costs[start_node]:
            continue

        for x in links[start_node]:
            end_node, add_cost = x
            new_cost = cost + add_cost
            if new_cost >= costs[end_node]:
                continue
            costs[end_node] = new_cost
            path[end_node] = start_node
            heapq.heappush(pq, (new_cost, end_node))
    print(costs[goal])
    cur = goal
    move = [cur]
    while cur != start:
        cur = path[cur]
        move.append(cur)
    print(len(move))
    print(' '.join(map(str, reversed(move))))
solve()
