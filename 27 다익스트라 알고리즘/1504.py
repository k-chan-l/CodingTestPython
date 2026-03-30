'''
특정한 최단 경로
1번노드에서 N번 노드로 이동하는데 지정된 2개의 지점을 통과해야함
한번 이동했던 경로를 다시 이동하는것도 가능하다, 단 무조건 최단거리여야한다.
1-> x -> y -> N의 구조로 가는게 정석
1번에서의 거리, N에서의 거리를 구한뒤
x->y까지의 거리의 최소값을 구한다.
그 상황에서 1 -> x + n -> y과 1->y + n->x 중 가장 작은값을 구해서 x->y까지의 거리를 구하고 반환하면된다.
하지만 이러면 3번해야 하니 비효율 생각을 바꿔서 y, x에서 수행하면 2번해서 모든 경우를 구하는게 가능하다.
즉 x-> 1 + y->n or x->n + y->1이다.
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**8

def dijkstra(links, dists, s_node):
    pq = []

    dists[s_node] = 0
    heapq.heappush(pq, (0, s_node))

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > dists[node]:
            continue
        
        for i in links[node]:
            next_node, add_dist = i
            next_dist = add_dist + dist
            if next_dist >= dists[next_node]:
                continue

            dists[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))
    return dists



def solve():
    n, e = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]
    dists_x = [INF] * (n+1)
    dists_y = [INF] * (n+1)
    
    for i in range(e):
        s_node, e_node, dist = map(int, input().rstrip().split())
        links[s_node].append((e_node, dist)) #정방향 추가
        links[e_node].append((s_node, dist)) #역방향 추가
    x, y = map(int, input().rstrip().split())
    dists_x = dijkstra(links, dists_x, x)
    dists_y = dijkstra(links, dists_y, y)

    result = dists_x[1] + dists_y[n] + dists_x[y] if dists_x[1] + dists_y[n] < dists_x[n] + dists_y[1] else dists_x[n] + dists_y[1] + dists_x[y]
    if result >= INF :
        result = -1
    return result
print(solve())

'''
1 -> n -> x -> y
n -> 1 -> x -> y
'''