'''
세 수의 합

임의의 점 3개를 골라야하고 그값의 합이 배열에 있는지를 찾아야하는문제
n^3*logn 으로 보이지만
n^2만 하고 3개의 합에서 ln을 뺀 값이 n^2를 저장한 배열에 있는지 확인하는 방법을 통해 시간을 줄일 수 있다.
x =(2 3 5 10 18)
5 7 12 20 8 13 21 15 28 정렬
y = (5 7 8 12 13 15 20 21 28)
이렇게 되는데 이 값은 x-y 값이 x에 있는지 찾는 경우라 n^2*logn이 된다.
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    nums.sort()
    sums = []
    for i in range(n):
        for j in range(n):
            sums.append(nums[i]+nums[j])
    sums = sorted(list(set(sums)))
    for i in reversed(nums): # 3개의 합
        for j in sums: # 2수의 합
            x = i-j #나머지 값 하나
            bn = bisect.bisect_left(nums, x)
            if bn < n and nums[bn] == x:
                print(i)
                return
solve()
