'''
n개의 정수로 이루어진 수열
두수를 골랐을때 차이가 M이상이면서 제일 작은 경우를 구하는 프로그램

양 끝값을 지정
st, ed
ed - st -> 차이가 m보다 크면 m값을 저장, 

'''
import sys
input = sys.stdin.readline
INF = 10**10

def solve():
    n, m = map(int, input().rstrip().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    st = 0
    ed = 0
    arr.sort()
    answer = INF
    while st <= ed and ed < n:
        sub = arr[ed] - arr[st]
        if sub < m:
            ed += 1
        elif sub > m:
            if answer > sub:
                answer = sub
            st+=1
        else:
            print(sub)
            return
    print(answer)
solve()