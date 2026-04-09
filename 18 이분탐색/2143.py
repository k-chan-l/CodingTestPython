'''
배열 a와 b의 a[i]~a[j]까지의 합과, b[k]~b[l]의 합이 T가되는 부 배열의 쌍의 개수를 구해라
[1 3 1 2]
[1 3 2] 숫자의 값은 음수~양수
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    t = int(input())
    a_n = int(input())
    a = list(map(int, input().rstrip().split()))
    b_n = int(input())
    b = list(map(int, input().rstrip().split()))

    a_sum = []
    b_sum = []

    for i in range(a_n):
        sum = 0
        for j in range(i, a_n):
            sum += a[j]
            a_sum.append(sum)
    for i in range(b_n):
        sum = 0
        for j in range(i, b_n):
            sum += b[j]
            b_sum.append(sum)
    a_sum.sort()
    b_sum.sort()
    answer = 0
    for i in a_sum:
        l = bisect.bisect_left(b_sum,t-i)
        r = bisect.bisect_right(b_sum,t-i)
        answer += r-l
    print(answer)

solve()