import sys
from collections import deque
input = sys.stdin.readline
'''
키보드의 입력을 따라하는 프로그램 구현
커서의 위치를 구현하기 번거롭기때문에 커서는 고정하고, 커서 앞뒤를 덱으로 구현
<일경우 앞에서 하나를 pop해서 뒤에 push하고
>일경우 뒤에서 하나를 pop하고 앞에 push하고
-의 경우 앞을 pop한다
그 외 나머지의 경우 왼쪽에 push한다
'''
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