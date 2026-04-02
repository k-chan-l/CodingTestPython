'''
횡단보도
1번에서 N번까지 횡단보도를 건너게 되는데 최소 시간으로 건너야 한다.
이때 횡단보도는 초록불에만 건널수 있고, 건너가는데는 1분이 소요되며, 1분마다 신호가 바뀐다.
바뀌는 순서는 등록되는 순서고, 이를 주기로 반복해서 계산된다. %n을 통해서 현재 신호를 확인 할 수있다.
-----------------------------------------------------------------
즉 현재 신호에서 선택할수 있는 방법은 기다리기 or 건너가기가 된다.
해제 방법은 한주기를 건넜는데도 같은 신호일때, queue를 써도 상관은 없을듯, 전부 같은 시간을 소모하니
대기시간을 따로 저장해둔다. why? 최대 대기시간보다 낮으면, 이미 들어간 값으로 판단 queue를 사용하기때문에 역전될 일은 없다.
한번 최소시간이 정해지면 보통 그대로
------------틀린풀이----------------------------------------------
기다리기를 행동으로 계산하면 계산량이 늘어나 시간이 오래걸린다.
계산해서 가중치로 만든뒤 시간을 계산하면 우선순위 큐로 간단하게 풀 수 있다.

'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**16

def solve():
    n, m = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]
    costs = [INF] *(n+1)
    for i in range(m):
        a, b = map(int, input().rstrip().split())
        links[a].append((b, i)) # start, end, 0초 기준 대기시간
        links[b].append((a, i)) # end, start, 0초 기준 대기시간
    
    pq = []
    heapq.heappush(pq,(0, 1)) # 시간, 현재 위치
    costs[1] = 0
    while pq:
        t, cur_loc = heapq.heappop(pq)
        if costs[cur_loc] < t:
            continue
        
        for i in links[cur_loc]:
            next_node, wait = i
            next_t = ((m+wait)-(t%m))%m + 1 + t # 다음노드 도착시간 = ((한주기 + 0초 기준 대기시간) - (한주기 기준 현시간)) % 한주기 + 1
            if costs[next_node] <= next_t:
                continue
            costs[next_node] = next_t
            heapq.heappush(pq, (next_t, next_node))
    print(costs[n])
solve()