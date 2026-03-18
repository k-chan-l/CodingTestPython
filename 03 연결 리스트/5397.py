import sys
from collections import deque
input = sys.stdin.readline

def solve() :
    n = int(input())
    for a in range(n) :
        left = deque()
        right = deque()
        s = input().rstrip('\n')
        for b in s :
            if b == '<' :
                if len(left) != 0 :
                    right.appendleft(left.pop())
            elif b == '>' :
                if len(right) != 0 :
                    left.append(right.popleft())
            elif b == '-' :
                if len(left) != 0 :
                    left.pop()
            else :
                left.append(b)
        print(''.join(left) + ''.join(right))
solve()