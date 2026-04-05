'''
용액 합성하기

n개의 리스트의 값들을 합쳐서 0에 가장 가까운 값을 만들어내는 문제
먼저 하나를 고르고, 그값을 뺀값이 0인지 아닌지 확인하는 문제
'''
import sys
import bisect
input = sys.stdin.readline
INF = 10**9
def solve():
    n = int(input())
    liquids = list(map(int, input().rstrip().split()))

    answer = INF
    for idx, liquid in enumerate(liquids[:-1]):
        x = bisect.bisect_left(liquids, -liquid, idx+1)
        if x >= n:
            x=n-1
            answer = answer if abs(answer) < abs(liquids[x]+liquid) else liquids[x]+liquid
        elif liquids[x] == -liquid:
            print(0)
            return
        elif x-1!=idx and abs(liquids[x-1] + liquid) < abs(liquids[x] + liquid):
            answer = answer if abs(answer) < abs(liquids[x-1]+liquid) else liquids[x-1]+liquid
        else:
            answer = answer if abs(answer) < abs(liquids[x]+liquid) else liquids[x]+liquid
    print(answer)
solve()