'''
세금
통행료의 합이 가장 적은 경로로 이동, 양방향, 세금이 A만큼 오르면 모든 도로의 통행료가 A만큼 오름
----------------------------
즉, 다익스트라를 2번 돌린다.
첫번째에서구한 최대 노드수를 기준으로 이것보다 작은값들만 순회시킨다.
그러면 제한조건을 찾아 가능하다. 하지만 이때 이전구간에서는 아닌줄 알았던 값이, 다음구간에서 최적값을 가능성이 있나? 이걸 생각해봐야한다.
최적값이 되려면, 이전 그 값에서 최적값이 되어야 가능하기 때문에 그럴리가 없다. 그다음 경로를 어떻게 하느냐의 문제지 이전값은 반드시 최적값이여야 하기에 가능하다.

이 최대 간선수를 기준으로 다음값을 2차원 다익스트라를 돌린다. 현재 간선수를 기준으로 구할 수 있는 최소값을 구한뒤, 이걸 바탕으로 최종값을 구한다.
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**8

def solve():
    n, m, k = map(int, input().rstrip().split())
    start, end = map(int, input().rstrip().split())
    links = [[] for i in range(n+1)]

    for i in range(m):
        s_node, e_node, cost = map(int, input().rstrip().split())
        links[s_node].append((cost, e_node))
        links[e_node].append((cost, s_node))
    
    # 요금 추가
    add_fees = [0]
    for i in range(k):
        add_fees.append(int(input()))

    # 최소 요금 다익스트라 -> 최대 간선의 개수 상한선 지정
    min_costs_lines = [(INF, 0) for i in range(n+1)] # 최소값과, 그때의 간선수
    pq = []
    heapq.heappush(pq, (0, start, 0)) # 비용, 노드, 그때의 간선수
    min_costs_lines[start] = (0, 0)

    while pq:
        cur_cost, cur_node, cur_line = heapq.heappop(pq)
        if min_costs_lines[cur_node][0] != cur_cost:
            continue
        for add_cost, next_node in links[cur_node]:
            next_cost = cur_cost + add_cost
            next_line = cur_line + 1
            if min_costs_lines[next_node][0] <= next_cost:
                continue
            min_costs_lines[next_node] = (next_cost, next_line)
            heapq.heappush(pq,(next_cost, next_node, next_line))

    # 각 노드의 간선 별 최소 요금 다익스트라
    costs_lines = [[INF]*(min_costs_lines[i][1]+1) for i in range(n+1)]
    pq = []
    heapq.heappush(pq, (0, 0, start)) # 비용, 간선수, 노드
    costs_lines[start][0] = 0 # 라인별비용[시작 노드][간선수] = 비용

    while pq:
        cur_cost, cur_line, cur_node = heapq.heappop(pq)
        if costs_lines[cur_node][cur_line] != cur_cost:
            continue

        for add_cost, next_node in links[cur_node]:
            next_cost = cur_cost + add_cost
            next_line = cur_line + 1
            # 각 노드별 간선 최대값보다 다음 간선수가 크면 패스
            if min_costs_lines[next_node][1] < next_line:
                continue
            if costs_lines[next_node][next_line] <= next_cost:
                continue
            costs_lines[next_node][next_line] = next_cost
            heapq.heappush(pq, (next_cost, next_line, next_node))

    fee = 0
    for add_fee in add_fees:
        fee += add_fee
        min_fee = INF
        for line, cost in enumerate(costs_lines[end]):
            min_fee = min(min_fee, (line*fee)+cost)
        print(min_fee)
solve()