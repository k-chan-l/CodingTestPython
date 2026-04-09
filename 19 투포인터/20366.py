'''
각 h의 지름을 가진 n개의 눈덩이가 있다. 눈사람의 키는 2개의 눈덩이의 합과 같다
n개중 4개를 골라서 눈사람 2개를 만들때, 두 눈사람의 키의 차이가 최소가 될때의 값을 구해라

두 눈사람의 키의 차이기 때문에 머리와 몸통의 크기는 상관 없다.
-> 만들수 있는 모든 눈사람의 경우의 수를 센다. => n^2 중복이 포함되기 때문에 문제가 있다. 중복을 제거하면 경우의 수가 제한된다.
전체 눈사람을 다 만들고, 거기서 2개씩 골라서 투포인터 => 중복 제거는 어떻게? 첫번째 for문에서 이것보다 뒤의 경우를 배제,
하나의 기준을 가진 3포인터?
'''
import sys
input = sys.stdin.readline
INF = 10**10
def solve():
    min_dif = INF
    n = int(input())
    snows = list(map(int, input().rstrip().split()))
    snows.sort()
    snowmans = []
    for i in range(n-1):
        for j in range(i+1,n):
            snowmans.append((snows[i]+snows[j],i,j))
    snowmans.sort()
    ed = 1
    min_dif = INF
    for st in range(len(snowmans)):
        f_s, a, b = snowmans[st]
        for ed in range(st+1, len(snowmans)):
            s_s, c, d = snowmans[ed]
            if a == c or a == d or b == c or b == d:
                continue
            dif = s_s - f_s
            min_dif = min(min_dif, abs(dif))
            if dif > 0:
                break
            if dif == 0:
                print(0)
                return
    print(min_dif)
solve()