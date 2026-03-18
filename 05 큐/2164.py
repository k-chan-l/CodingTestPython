import sys
from collections import deque
input = sys.stdin.readline

def solve() :
    n = int(input())
    q = deque(range(n,0,-1))

    flag = True
    while len(q) > 1:
        if flag :
            q.pop()
        else :
            q.appendleft(q.pop())
        flag = not flag
    print(q[0])
solve()