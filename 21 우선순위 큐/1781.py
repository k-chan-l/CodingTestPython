'''
컵라면

데드라인에 맞춰서 문제를 풀면 해결되는 문제
최대 한으로 얻을수있는 컵라면 갯수에 맞춰서 풀면 된다.

모든 문제의 풀이시간이 1로 동일하기때문에 기준 1은 데드라인, 기준 2는 개수로 정렬하면된다.
이때 데드라인은 최소힙, 개수는 최대힙으로 정렬한 후, 현재시간보다, 클경우 해당 값을 버린다.
최소 힙?
컵라면이 작은순서대로 배치?
데드라인	1	1	3	3	2	2	6
컵라면 수	6	7	2	1	4	5	1
데드라인, 컵라면수(작은것부터) => 우선순위 큐에 삽입
why? 그래야 기존것에서 작은거를 빼고 삭제하는게 가능하기 때문
'''
import sys
import heapq
input = sys.stdin.readline

def solve():
    pq = []
    result = []
    n = int(input().rstrip())
    for i in range(n):
        dead, cup = map(int, input().rstrip().split())
        heapq.heappush(pq, (dead, cup)) # 작은것부터
    
    while pq:
        dead, cup = heapq.heappop(pq)
        if len(result) < dead:
            heapq.heappush(result, cup)
        else :
            heapq.heappop(result)
            heapq.heappush(result, cup)
    print(sum(result))
solve()