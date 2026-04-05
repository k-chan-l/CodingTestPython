'''
수찾기
이분탐색을 활용하여 구하는 문제
먼저 정렬을 한다.
st, mid, ed 포인터를 이용해서 정수의 위치를 특정한다.
mid = (ed-st)//2
mid의 값과 일치하면 1을 반환한다.
mid의 값보다 크면, st를 mid 다음칸으로 바꾼다
mid의 값보다 작으면, ed를 mid 전칸으로 바꾼다
st와 ed가 역전되면 0을 반환한다.

만약 st나 ed의 값이 영역을 넘어서면 바로 0을 반환한다 ->역전 검사에서 걸러지므로 당연히 될거라 문제는 없다.
'''
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted(list(map(int, input().rstrip().split())))
    m = int(input())
    x = list(map(int, input().rstrip().split()))
    
    for i in x:
        st = 0
        ed = n-1
        mid = ed//2
        find = False
        while st <= ed:            
            if arr[mid] == i:
                find = True
                break
            elif arr[mid] < i:
                st = mid + 1
            else:
                ed = mid -1
            mid = (ed-st)//2+st
        if find:
            print(1)
        else :
            print(0)
solve()