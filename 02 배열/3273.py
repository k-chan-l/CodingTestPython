import sys
input = sys.stdin.readline
'''
수열의 두 수의 합이 주어진 입력과 같은 쌍의 숫자를 구하는 문제
1. 수열을 오름차순으로 정렬 -> 계산의 간단함을 위해
2. n-1번째 까지 순회
3. 현재 고른 반복문의 수와 같은 값을 맨 뒤에서 부터 검색 -> 중복 탐색되는 범위를 줄이게 됌
이 방법을 사용하면 이중 반복문에서도 O(n)으로 탐색 가능
4. 같은 쌍의 개수를 반환
'''
def solve() :
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    count = 0
    end = n-1
    arr.sort()
    for i in range(n-1):
        num = x - arr[i]
        for j in range(end,0,-1):
            if i >= j :
                break
            if num == arr[j] :
                count += 1
                end = j - 1
                break
            elif num > arr[j] :
                end = j
                break

    print(count)
solve()