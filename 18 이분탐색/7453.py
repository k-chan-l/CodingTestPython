'''
합이 0인 네 정수
숫자가 n개 들어있는 배열 a,b,c,d에서 각각 하나씩 뽑아서 합이 0이되는 개수를 구하라
1. a와 b, c와 d의 합을 배열로 정리 2 *n2
2. 1번 배열을 순회하며 2번 배열에서 0이 되는 개수 이분탐색
3. 압축을 한다면? 숫자의 합을 압축해서 하나로 만듬
'''
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = []
    b = []
    c = []
    d = []
    for _ in range(n):
        i, j, k, l = map(int, input().rstrip().split())
        a.append(i)
        b.append(j)
        c.append(k)
        d.append(l)
    
    dic = {}
    for i in a:
        for j in b:
            dic[i+j] = dic.get(i+j, 0)+1
    answer = 0
    for i in c:
        for j in d:
            answer += dic.get(-i-j, 0)
    print(answer)
solve()