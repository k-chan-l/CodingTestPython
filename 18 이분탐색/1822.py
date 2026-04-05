'''
차집합

집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구해라
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n_a, n_b = map(int, input().rstrip().split())
    a = []
    b = []
    for x in map(int, input().rstrip().split()):
        a.append(x)
    for x in map(int, input().rstrip().split()):
        b.append(x)
    b.sort()
    in_a_not_b = []
    for i in a:
        x = bisect.bisect_left(b,i)
        if x >= n_b or b[x] != i:
            in_a_not_b.append(i)
    count = len(in_a_not_b)
    print(count)
    if count != 0:
        in_a_not_b.sort()
        print(' '.join(map(str, in_a_not_b)))
solve()