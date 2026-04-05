'''
숫자 카드
n개의 카드중에서 m개의 정수가 주어졌을때, 가지고 있는지 여부를 확인하는 프로그램
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    cards = list(map(int, input().rstrip().split()))
    m = int(input())
    nums = map(int, input().rstrip().split())
    cards.sort()
    for i in nums:
        x = bisect.bisect_left(cards, i)
        if x <n and i==cards[x]:
            print(1, end=' ')
        else :
            print(0, end=' ')
solve()