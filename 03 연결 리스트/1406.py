import sys
from collections import deque
input = sys.stdin.readline
'''
커서를 통해 텍스트를 입력하는 에디터 구현
커서의 위치를 구현하기 번거롭기때문에 커서는 고정하고, 커서 앞뒤를 덱으로 구현
L일경우 앞에서 하나를 pop해서 뒤에 push하고
D일경우 뒤에서 하나를 pop하고 앞에 push하고
B의 경우 왼쪽을 pop하고
P $의 경우 $를 왼쪽에 push하여 구현
'''
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
