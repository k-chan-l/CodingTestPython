'''
파티

N개의 마을에서 X로 이동한다. -> i번 길을 지나는데 Ti의 시간을 소비
즉 최단시간기준 가장 오래걸리는 학생이 누군지? 모든길은 연결되어있음

다익스트라 알고리즘 사용 해서 X기준 가장 먼 곳 구한뒤 반환
오는길 가는길이 전부 다르고, 왔다갔다 하는 거리 기준으로 계산 필요

시간은 1초 다익스트라 1번만 가능

Ti의 최대값은 100
1. 거리를 저장하는 리스트
2. 연결을 저장하는 리스트 2차원
3. 우선순위 큐 설정
-------------------------------------------------------------
개선사항 2차원으로 만들 필요는 없다. 시간이 오래걸림
-> 뒤집어진 경로를 다시 만들면 된다.
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**6 # N * 100 => 이론상 나올수 있는 최대값보다 큰값 1000 * 100 * 2

def solve():
    n, m, start = map(int, input().rstrip().split())
    dists = [INF]*(n+1) # 최소거리 저장
    rev_dists = [INF]*(n+1) # 역순
    links = [[] for i in range(n+1)] # 연결 저장
    rev_links = [[] for i in range(n+1)] # 역순 연결
    pq = []

    for i in range(m):
        s_node, e_node, dist = map(int, input().rstrip().split())
        links[s_node].append((e_node, dist)) # 정방향 거리 등록
        rev_links[e_node].append((s_node, dist)) # 역방향 거리 등록
    
    dists[start] = 0
    heapq.heappush(pq, (0, start)) # (거리, 시작노드)

    while pq:
        dist, s_node = heapq.heappop(pq)

        if dist > dists[s_node]:
            continue
        for x in links[s_node]:
            next_node, add_dist = x
            next_dist = dist + add_dist
            if next_dist >= dists[next_node]:
                continue

            dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))

    rev_dists[start] = 0
    heapq.heappush(pq, (0, start)) # (거리, 시작노드)

    while pq:
        dist, s_node = heapq.heappop(pq)

        if dist > rev_dists[s_node]:
            continue
        for x in rev_links[s_node]:
            next_node, add_dist = x
            next_dist = dist + add_dist
            if next_dist >= rev_dists[next_node]:
                continue

            rev_dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
    
    distance = [dists[i] + rev_dists[i] for i in range(1, n+1)]
    return max(distance)
print(solve())