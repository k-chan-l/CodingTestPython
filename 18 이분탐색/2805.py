'''
나무 자르기

총 n개의 나무중, 나무 m미터가 필요 높이 x로 자를때, 위에서 잘린 부분의 합이 m이 되는 높이 x의 최대값을 구해라
'''
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().rstrip().split())
    trees = list(map(int, input().rstrip().split()))
    trees.sort()

    st = 0 #전부 자를 경우
    ed = trees[-1] # 가장 높은 나무 크기
    mid = (ed-st)//2

    while st <= ed:
        count = 0        
        for i in trees:
            count += i-mid if i>=mid else 0
        if count >= m:
            st = mid + 1
            mid = (ed-st)//2 + st
        else :
            ed = mid - 1
            mid = (ed-st)//2 + st
    print(mid)
solve()