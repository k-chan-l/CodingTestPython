'''
랜선 자르기
parametric search를 이용해서 문제 해결
k개 중 몇개를 잘라서 n개로 만들어야 하는데 ->이때 모든 랜선의 길이는 x로 같아야한다.
4개를 11개로 만들어야 한다.
457 539 743 802 순으로 정렬
x의 길이를 이분탐색으로 줄여가면서 11이 나오는 가장 큰 값을 구한다.
end는 가장 작은 값으로 지정,
st는 1로 지정
mid는 중간 값으로 지정
이때의 x를 반환
'''
import sys
input = sys.stdin.readline

def is_possible(n, mid, arr):
    sums = 0
    for i in arr:
        sums += i//mid
    return sums >= n

def solve():
    k, n = map(int,input().rstrip().split())
    arr = []
    for i in range(k):
        arr.append(int(input()))
    arr.sort()
    ed = arr[-1]
    st = 1
    mid = (ed-st)//2+st
    while st <= ed:
        if is_possible(n, mid, arr):
            st = mid + 1
            mid = (ed-st)//2 + st
        else :
            ed = mid - 1
            mid = (ed-st)//2 + st
    print(mid)
solve()
    