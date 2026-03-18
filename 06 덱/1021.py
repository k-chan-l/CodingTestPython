import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().rstrip().split())
    dq = deque(range(1,n+1))
    arr = list(map(int, input().rstrip().split()))
    answer = 0
    for a in arr :
        dq_left = dq.copy(); dq_right = dq.copy()
        answer_left = answer_right = answer
        while dq_left and dq_left[0] != a :
            dq_left.append(dq_left.popleft())
            answer_left += 1
        while dq_right and dq_right[0] != a :
            dq_right.appendleft(dq_right.pop())
            answer_right += 1
        if answer_left > answer_right :
            answer = answer_right
            dq_right.popleft()
            dq = dq_right
        else :
            answer = answer_left
            dq_left.popleft()
            dq = dq_left
    print(answer)
solve()

