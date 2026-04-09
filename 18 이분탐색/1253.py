'''
좋다

n개의 수중에서 어떤수가 다른 두개의 수 의 합으로 나타낼수 있으면 좋은수다.
수의 위치가 다르면 값이 같아도 다른수이다.
음수 때문에 다른방법 필요
1. a + b = c인 숫자를 구하는건데,
2. 첫번째 a를 고정하고, b를 고른뒤, 그 둘을 제외한 나머지 값 c를 찾는 방법 이때 좋은 수의 개수 이므로, 해당 숫자를 중복없이 표현할 필요가 있음
3. bool 배열로 체크한 경우를 표시, True인경우 체크 안함, 음수의 존재때문에 전체 범위를 나눠서 찾을 필요가 있음
4.이분탐색을 이용해서 개수를 세고, false일 경우만 true로 바꾸고 개수 증가
- - 면 첫번째보다 앞부분에서 찾기
- + 면 둘사이에서 찾기
+ + 면 둘 이후에서 찾기
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    if n < 3:
        print(0)
        return
    arr.sort()
    is_good = [False]*n
    answer = 0
    for i in range(n-1):
        for j in range(i+1,n):
            a = arr[i]
            b = arr[j]
            c = a+b
            if c <= a: # a의 왼쪽에서 찾기 
                k = bisect.bisect_right(arr,c, hi=i) #i 오른쪽 값을 반환할 필요가 있음
                k -=1 # arr[k]는 c가 아님
                while 0 <= k and arr[k] == c: #값이 들어갈 위치이기때문에 더 큰수여도 무방
                    if not is_good[k]:
                        answer += 1
                        is_good[k] = True
                    else : # 이미 순회 했으면 탈출
                        break
                    k-=1
            if b <= c: # b의 오른쪽에서 찾기
                k = bisect.bisect_left(arr,c, lo=j+1) #j 이후로 탐색 1 2 2 3 3 4 5
                while k < n and arr[k] == c:
                    if not is_good[k]:
                        answer += 1
                        is_good[k] = True
                    else:
                        break
                    k+=1
            if a <= c and c <= b: # a와 b 사이에서 찾기
                k = bisect.bisect_right(arr,c, lo=i+1, hi=j) #j 전까지 탐색 끝이 움직이기 때문
                k -= 1
                while k > i and arr[k] == c:
                    if not is_good[k]:
                        answer += 1
                        is_good[k] = True
                    else:
                        break
                    k-=1
    print(answer)
solve()