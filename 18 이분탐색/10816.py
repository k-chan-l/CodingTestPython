'''
숫자 카드 2
n개의 카드에서 m개의 숫자가 각각 몇개씩 있는지 확인하는 문제
1. 정렬한다.
2. 이분탐색을통해 양끝값을 구한다.
2-1. left값이 그 값이 아닐경우 0을 반환한다.
3. 둘의 차이를 반환한다.
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    cards = sorted(list(map(int, input().rstrip().split())))
    m = int(input())
    arr = map(int, input().rstrip().split())

    for x in arr:
        left = bisect.bisect_left(cards, x)
        right = bisect.bisect_right(cards, x)
        if left >=n or cards[left] != x:
            print(0, end=' ')
        else :
            print(right-left, end=' ')
solve()
