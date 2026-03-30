'''
최단경로
방향그래프를 바탕으로 주어진 시작점에서 다른 모든 정점으로의 최단경로를 구하는 방법
우선순위 큐를 활용해 현재기준 거리가 가깝다면, 먼저 연산해 중복연산을 최소화
1. links로 노드별 연결 부여
2. dists로 각 노드별 이동 최소 경로 지정 -> 기본값 INF
3. 우선순위 큐에 거리와, 현재지점을 등록
4. 다익스트라 알고리즘을 이용해 우선순위큐에서 거리가 가까운 순서대로 뽑아내기
5. 연산 과정중에 바뀌었을 수도 있으니, 확인후 큐에 추가 거리부분 더하기
'''
import sys
import heapq
input = sys.stdin.readline

def solve():
    v, e = map(int, input().rstrip().split())
    start_node = int(input().rstrip())
    dists = ['INF'] * (v+1)
    links = [[] for i in range(v+1)]
    pq = []
    for i in range(e):
        a, b, w = map(int, input().rstrip().split())
        links[a].append((b,w))
    heapq.heappush(pq, (0, start_node))
    while pq:
        dist, node = heapq.heappop(pq)
        if dists[node] != 'INF' and dists[node] <= dist:
            continue
        dists[node] = dist
        for x in links[node]:
            next_node, add_dist = x
            if dists[next_node] != 'INF' and dists[next_node] <= add_dist + dist:
                continue
            heapq.heappush(pq, (add_dist + dist, next_node))
    for i in range(1, v+1):
        print(dists[i])
solve()