'''
과자 나눠주기

긴과자를 나눠준다. 같은 길이의 과자를 나눠줘야 한다.
현재 n개 m개로 바꿔줘야 한다.
'''
import sys
import bisect
input = sys.stdin.readline

def is_possible(arr, m, size):
    count = 0
    for i in arr:
        count += i//size
    return count >= m

def solve():
    m, n = map(int, input().rstrip().split())
    snack = []
    for i in map(int, input().rstrip().split()):
        snack.append(i)
    snack.sort()

    st = 1
    ed = snack[-1]
    mid = (ed-st)//2 + st

    while st <= ed:
        if is_possible(snack, m, mid):
            st = mid + 1
            mid = (ed-st)//2 + st
        else:
            ed = mid - 1
            mid = (ed-st)//2 + st
    if mid != 0 and is_possible(snack, m, mid):
        print(mid)
    else:
        print(0)
solve()
    
