import sys
from collections import deque
input = sys.stdin.readline

def solve() :
    answer = []
    count = 1
    n, k = map(int, input().split())
    dq = deque(range(1,n+1))    
    while len(dq) != 0 :
        if count % k == 0 :
            count += 1
            answer.append(dq.popleft())
        else :
            count += 1
            dq.append(dq.popleft())
    print('<' + ', '.join(map(str, answer)) + '>')
solve()