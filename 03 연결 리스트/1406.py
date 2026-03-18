import sys
from collections import deque
input = sys.stdin.readline

def solve() :
    before = deque(input().rstrip())
    after = deque()
    m = int(input())
    for a in range(m):
        t = input().rstrip().split()
        if len(t) == 2 :
            ex, c = t
        else :
            ex = t[0]
        if ex == 'P' :
            before.append(c)
        elif ex == 'L':
            if len(before) != 0 :
                after.appendleft(before.pop())
        elif ex == 'D' :
            if len(after) != 0 :
                before.append(after.popleft())
        else :
            if len(before) != 0 :
                before.pop()
    print(''.join(before)+''.join(after))
solve()
