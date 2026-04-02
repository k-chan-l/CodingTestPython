'''
면접보는 승범이네

면접자는 n명
도로는 단방향 k개의 면접장에서 가장 가까운 구역으로 면접자는이동, 이때 가장 먼거리를 이동하는사람을 구해라
가장 가까운 면접장을 구하는 문제 => 전부 순회 필요
가장 가까운 면접자를 찾는 문제 => k개 만큼만 순회하면 가능
즉 면접장에서 다익스트라를 써서 모든 값을 구하고, 각 도시별 최소 값을 모아서 하나로 만들고, 그중 가장 먼사람을 골라서 반환
--------------------------------------------------------------------
메모리 초과로 방법 변경
k개 순회해서 최저값을 구하나, 한번에 k개 순회하는거나 별차이가 없고, 각 케이스별 값들을 남길 이유가 없어서 한번에 멀티소스 다익스트라로 돌리면 된다

'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**11

def dijkstra(links, dists, start_nodes):
    pq = []
    for i in start_nodes:
        dists[i] = 0
        heapq.heappush(pq, (0, i))

    while pq:
        dist, cur_node = heapq.heappop(pq)
        if dist > dists[cur_node]:
            continue

        for i in links[cur_node]:
            next_node, add_dist = i
            next_dist = dist + add_dist
            if next_dist >= dists[next_node]:
                continue
            dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
    return dists

def solve():
    n, m, k = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]
    dists = [INF]*(n+1)
    for i in range(m):
        start_node, end_node, dist = map(int, input().rstrip().split())
        links[end_node].append((start_node, dist)) # 도착한 기준이기 때문에 역순으로 정렬
    l = list(map(int, input().rstrip().split()))

    dists = dijkstra(links, dists, l)
    
    max_dist = 0
    for i in range(1,n+1):
        if dists[i] > max_dist:
            max_dist = dists[i]
            cur = i
    print(cur)
    print(max_dist)
solve()