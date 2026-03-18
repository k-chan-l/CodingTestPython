import sys
from collections import deque
input = sys.stdin.readline

def solve() :
    T = int(input())
    for a in range(T) :
        instructions = list(input().rstrip())
        n = int(input())
        if n != 0 :
            dq = deque(map(int, input().rstrip().strip('[]').split(',')))
        else :
            input()
            dq = deque()
        flag = True
        reversedFlag = False
        for i in instructions :
            if i == 'R' :
                reversedFlag = not reversedFlag
            elif i == 'D' :
                if dq :
                    if reversedFlag :
                        dq.pop()
                    else :
                        dq.popleft()
                else :
                    flag = False
                    break
        if flag :
            if reversedFlag :
                dq.reverse()
            print('[' + ','.join(map(str,list(dq))) + ']')
        else :
            print('error')
solve()