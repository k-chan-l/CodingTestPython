'''
소수의 연속합

자연수가 주어졌을때 이 자연수를 연속된 소수의 합으로 나타낼수 있는 경우의 수를 구하는 프로그램을 구해라

1. 소수구하기 2부터 시작하는 반복문으로  지정
2. 합계산은 투포인터로 지정
'''
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    prime = [x for x in range(n+1) if is_prime[x]]
    ed = 0
    sum = 0
    answer = 0
    for st in range(len(prime)):
        while ed < len(prime) and sum < n:
            sum += prime[ed]
            ed += 1
        if sum == n:
            answer += 1
        sum -= prime[st]
    print(answer)
solve()