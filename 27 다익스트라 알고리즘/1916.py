'''
최소 비용구하기

단순 단방향 다익스트라 문제
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def solve():
    n = int(input().rstrip())
    m = int(input().rstrip())
    links = [[] for i in range(n+1)]
    dists = [INF]*(n+1)

    for i in range(m):
        s_node, e_node, dist = map(int, input().rstrip().split())
        links[s_node].append((e_node, dist))

    start, end = map(int, input().rstrip().split())

    pq = []
    dists[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, s_node = heapq.heappop(pq)
        if dist > dists[s_node]:
            continue

        for i in links[s_node]:
            next_node, add_dist = i
            next_dist = dist + add_dist
            if next_dist >= dists[next_node]:
                continue
            dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
    print(dists[end])
solve()