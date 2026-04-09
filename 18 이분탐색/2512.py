'''
예산

arr의 모든 숫자의 합이 기준값보다 작으면 모두선정
더 크면 상한액 x를 지정해서 그 값보다 클경우 해당 값으로 선정,
x의 최대값 -> arr의 최대값
x의 최소값 -> 기준값 //n
'''
import sys
input = sys.stdin.readline

def is_possible(mid, limit, arr):
    ans = 0
    for x in arr:
        if x < mid:
            ans += x
        else :
            ans += mid
    return ans <= limit

def solve():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    limit = int(input())

    st = limit//n
    ed = max(arr)
    mid = (ed-st)//2+st

    while st <= ed:
        if is_possible(mid, limit, arr):
            st = mid+1
            mid = (ed-st)//2+st
        else:
            ed = mid-1
            mid = (ed-st)//2+st
    print(ed)
solve()