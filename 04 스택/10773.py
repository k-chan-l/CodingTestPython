'''
스택 구조로 활용
0일경우 빼고, 아닐경우 넣는다.
마지막은 sum으로 한번에 합을 반환
'''
import sys
input = sys.stdin.readline

def solve():
    k = int(input())
    arr = []
    for a in range(k) :
        x = int(input())
        if x == 0 :
            arr.pop()
        else :
            arr.append(x)
    print(sum(arr))
solve()
