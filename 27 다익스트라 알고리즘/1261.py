'''
알고스팟
NxM사이즈의 미로 탈출
이동은 상하좌우만 가능
1,1 N,M의 위치로 이동하려면 몇개의 벽을 부숴야 하나?

우선순위 큐를 사용하는 BFS
1. 부순벽의 개수를 확인할 지도가 필요
2. 부순벽의 개수가 지도에 있는 최소값보다 크면 패스
3. 우선순위 큐를 사용했기때문에 벽 파괴의 최소 값이 보장
4. 즉. N, M에 처음 도달한 값이 최소값
'''
import sys
import heapq
input = sys.stdin.readline
move = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 이동 옵션
INF = 10**6
def solve():
    m, n = map(int, input().rstrip().split())
    maze = []
    least_move = [[INF]*m for i in range(n)]
    for i in range(n):
        maze.append(list(map(int, list(input().rstrip()))))
    
    pq = []
    least_move[0][0] = 0
    heapq.heappush(pq, (0, 0, 0)) # 벽을 부순횟수, x(세로), y(가로)

    while pq:
        count, x, y = heapq.heappop(pq)
        if count > least_move[x][y]:
            continue
        if x == n-1 and y == m-1 :
            break
        for i in move:
            a, b = i
            if x+a<0 or x+a>=n or y+b<0 or y+b>=m:
                continue
            next_count = count
            if maze[x+a][y+b]:
                next_count+=1
            if next_count >= least_move[x+a][y+b]:
                continue
            least_move[x+a][y+b] = next_count
            heapq.heappush(pq,(next_count, x+a, y+b))
    print(least_move[n-1][m-1])
solve()
