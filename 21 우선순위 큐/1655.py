'''
가운대로 말해요
n개의 숫자를 받는다. n개가 홀수면 가운데값, n개가 짝수면 가운데 2개중 작은값을 출력

중간값을 구하는방법
작은 숫자만 넣는->최대힙[]
큰 숫자만 넣는->최소힙[]
이러면 중간 값이 우선순위가 가장 좋게 나온다.

두 힙에서 값을 하나씩 뺀다. 그 값이랑 현재 값을 비교해서 큰값은 큰숫자만 넣는 힙에, 작은값은 작은숫자만 넣는 힙에 넣는다.
개수가 홀수 일경우 크기를 맞춰주고, 짝수일 경우 큰 값에 우선적으로 넣는다.
짝수일 경우 남은 값을 출력하고,
홀수의 경우 도 남은값을 출력한다.
'''
import sys
import heapq
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    large_num = [] # 큰값이 들어갈 최소힙
    small_num = [] # 작은값이 들어갈 최대힙
    count = 0 # 반복 횟수
    for i in range(n):
        x = int(input().rstrip())
        next = large_num # 다음에 들어갈 힙 설정
        val = 1 # 최소 힙일 경우 반전없이 삽입
        if count % 2 == 1: # 개수가 홀수일 경우
            next = small_num # 작은 값에 추가적으로 삽입, why? 이렇게 구성되어 있어야 값이 같을경우 작은값에서 뺀 값이 정답이 되기 때문
            val *= -1 # 최대 힙일 경우 값을 반전해서 삽입
        large = heapq.heappop(large_num) if large_num else None # 큰값을 힙에서 빼기
        small = -heapq.heappop(small_num) if small_num else None # 작은값을 현재 힙에서 빼기|최대힙이기 때문에 반전해서 빼기

        if large != None and large < x: # None이 아니고, x보다 작으면
            large, x = x, large # x가 최대값이 됌
        elif small != None and small > x: # None이 아니면서, x보다 크면
            small, x = x, small # x가 최소값이 됌
        print(x) # x가 가운데의 값이 됌

        if large != None: # None이 아닐경우
            heapq.heappush(large_num, large)
        if small != None: # None이 아닐경우
            heapq.heappush(small_num, -small)
        heapq.heappush(next, x * val)
        count += 1

solve()