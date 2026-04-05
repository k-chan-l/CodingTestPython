'''
회전 초밥

1. 임의의 한 지점부터 k개의 접시를 연속해서 고르면 할인
2. 1번이 해당되면 초밥 추가 한종류 무료
이때, 손님이 먹을 수 있는 초밥의 종류의 최대값을 구해라

7 9 7 30 2 7 9 25

최대 n개의 접시중 한지점부터 연속해서 k개를 고르고, 이때의 가짓수의 최댓값을 고른다.

연속한 4개의 접시의 종류를 계산하는 방법? 번호 적어놓고, 빼면서 개수 계산 0이 되면 종류 -1 아니면 유지
'''
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, d, k, c = map(int,input().rstrip().split())
    kind = [0]*(d+1)
    sushi = deque()
    eat_sushi = deque()
    result = 0
    for _ in range(n):
        sushi.append(int(input()))

    for _ in range(k):
        x = sushi.popleft()
        kind[x] += 1
        if kind[x] == 1:
            result += 1
        eat_sushi.append(x)
    
    if kind[c] == 0:
        answer = result+1
    else:
        answer = result
    
    for _ in range(n):
        x = sushi.popleft()
        kind[x] += 1
        if kind[x] == 1:
            result += 1            
        eat_sushi.append(x)

        x = eat_sushi.popleft()
        kind[x] -= 1
        if kind[x] == 0:
            result -= 1
        sushi.append(x)

        if kind[c] == 0:
            answer = max(answer, result+1)
        else:
            answer = max(answer, result)
    print(answer)
solve()