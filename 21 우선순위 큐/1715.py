import sys
import heapq
input = sys.stdin.readline

'''
작은 숫자 순서대로 꺼내서 계산 덧셈 연산
1. 전부 우선순위 큐에 때려박기
2. 앞에서 부터 2개 꺼내고, 다시 넣기 -> 1개 남을때까지
3. 더한값을 결과에 넣기
4. 더한값 리턴
'''

def solve():
    result = 0
    pq = []
    n = int(input().rstrip())
    for i in range(n):
        heapq.heappush(pq, int(input().rstrip()))
    while 2 <= len(pq):
        x = heapq.heappop(pq) + heapq.heappop(pq)
        result += x
        heapq.heappush(pq, x)

    return result
print(solve())