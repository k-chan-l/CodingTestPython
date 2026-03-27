'''
N번째 큰수
n*n 사이즈의 배열이 있고, 모든 수는 자신의 한칸 '위'의 수보다 크다. 이때 n번째 큰 수를 구해라.
그냥 전부 우선순위 큐에 짱박아 넣고, N개 빼면 되는거 아닌가?
-> 최적화 기준 큰수 부터 넣어야 하는데 어떻게 하냐? 최대 힙을 이용한다? O(n)
but 맨 아래에 있는거 한줄 쫙 -> 우선순위 큐에 짱 박아 두고, 최대값을 빼고, 그값 다음값을 넣는다.
1. 배열의 마지막 줄을 순회해서 우선순위 큐에 넣음
2. 우선순위 큐를 활용시 해시와, 우선순위 큐를 활용해 -> 서로 다른 수이기를 이기 때문에 가능
3. n번째 나온수를 반환
-----------------------------------------------------------------------------
메모리 초과로 인해 시간은 좀더 걸리더라도 메모리가 안드는 방식을 활용
1. 최소힙을 써서, n개 까지 남기고, n+1개가 넘어가면 가장 작은거 빼기
'''
import sys
import heapq
input = sys.stdin.readline

def solve():
    pq = []
    n = int(input().rstrip())
    for a in range(n):
        for i in map(int,input().rstrip().split()):
            heapq.heappush(pq, i)
            if len(pq) > n :
                heapq.heappop(pq)
    num = heapq.heappop(pq)
    return num

# def solve():
#     pq = []
#     n = int(input().rstrip())
#     nums = []
#     for a in range(n):
#         nums.append(list(map(int,input().rstrip().split())))
#     for i, x in enumerate(nums[n-1]):
#         heapq.heappush(pq, (-x, n-1, i))
#     for i in range(n):
#         num, x, y = heapq.heappop(pq)
#         heapq.heappush(pq, (-nums[x-1][y], x-1, y))
#     num *= -1
    
#     return num
print(solve())