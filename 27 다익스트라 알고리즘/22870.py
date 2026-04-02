'''
산책(large)

도착지점을 반환하여 다시 원점으로 돌아오는 최소경로 찾기
뼈대 로직-----------------------------------------------
이때 중복 방문은 안된다. 다행인점은 S->E로 갈때 당시의 최솟값만 포함되기 때문에 다익스트라에서 먼저 가는 길을 구하고
해당 노드를 제외한 후, 다시 역순으로 다익스트라를 돌린다.

어떻게 하는게 좋을까? -> S->E의 최소 힙/ (비용, 노드번호, 이전노드 번호)을 기준으로 다익스트라
다음 경로 중 베스트를 찾는 방법?
모든 경로를 더해서 넘긴다-> 가능은 하다. 하지만 오래 걸렸다.
기본 다익스트라 기준 -> 최적경로는 거리기준으로 탐색 -> 더 짧은 거리가 있으면 갱신(같은 경로는 중복으로 판단하여 배제) | 인데
개선안 -> 거리기준 탐색 -> 큰거리는 배제 -> 같은거리일 경우 사전순 앞이면 갱신 이다.

기준은 개수가 아니라 거리 기준이기 때문에
1 -(1)-> 2 -(1)-> 3 -(1)-> 4 -(1)-> 5 -(1)-> 7 => 5
1 -(5)-> 7 => 5 여도 전자가 더 좋은 경로가 된다 즉 바로 직전경로의 숫자가 더 앞일경우 최적화를 해서 미룰 수 있다.
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**20

def solve():
    n, m = map(int, input().rstrip().split())
    links = [[] for _ in range(n+1)]
    for _ in range(m):
        s_node, e_node, dist = map(int, input().rstrip().split())
        links[s_node].append((dist, e_node))
        links[e_node].append((dist, s_node))
    start, end = map(int, input().rstrip().split())

    dists = [(INF, []) for _ in range(n+1)] # 비용, 방문한노드들
    pq = []

    heapq.heappush(pq, (0, end, str(end))) # 거리, 현재노드, 직전노드
    dists[end] = (0, str(end)) # 거리, 직전방문노드

    while pq:
        cur_dist, cur_node, cur_path = heapq.heappop(pq)
        if dists[cur_node][0] != cur_dist:
            continue
        if dists[cur_node][1] != cur_path:
            continue

        for add_dist, next_node in links[cur_node]:
            next_dist = add_dist + cur_dist
            next_path = str(cur_node)
            if dists[next_node][0] < next_dist:
                continue
            elif dists[next_node][0] == next_dist:
                if dists[next_node][1] <= next_path:
                    continue
            dists[next_node] = (next_dist, next_path)
            heapq.heappush(pq, (next_dist, next_node, next_path))
    visited = [False]*(n+1)
    cur_node = int(dists[start][1])
    while cur_node != end:
        visited[cur_node] = True
        cur_node = int(dists[cur_node][1])
    forward = dists[start][0]

    dists = [INF for _ in range(n+1)] # 비용, 방문한노드들
    pq = []

    heapq.heappush(pq, (0, end)) # 거리, 현재노드, 방문한 노드들
    dists[end] = 0

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if dists[cur_node] != cur_dist:
            continue
        
        for add_dist, next_node in links[cur_node]:
            next_dist = cur_dist + add_dist

            if visited[next_node]:
                continue
            if dists[next_node] <= next_dist:
                continue
            dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
    backward = dists[start]
    print(forward + backward)
solve()