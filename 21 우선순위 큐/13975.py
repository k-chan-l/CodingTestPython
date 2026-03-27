'''
파일 합치기3
40 30 30 50
그냥 작은 순서대로 -> 30 + 30 => 60,
40 50 60, 40 + 50 => 90,
60 90 => 150
300
우선순위 큐를 이용해서 파일 합치기
'''
import sys
import heapq
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    for x in range(n):
        input()
        pq = []
        result = 0
        nums = map(int, input().rstrip().split())
        for y in nums:
            heapq.heappush(pq, y)
        while len(pq) > 1:
            a, b = heapq.heappop(pq), heapq.heappop(pq)
            new_file = a+b
            result += new_file
            heapq.heappush(pq, new_file)
        print(result)
solve()
    
