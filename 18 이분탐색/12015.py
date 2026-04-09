'''
가장 긴 증가하는 부분수열 2

1. 가장 긴 수열이란? -> 왼쪽값보다 더큰 수만 포함하는 부분수열
2. 신경써야하는 부분 바로 다음 숫자를 올렸는데, 다음 숫자가 더 많을 경우.
3. 오른쪽으로 순회하다가.현재 값보다 더 작은수가 나오면 다시 비교
{10, 11, 20, 15, 16, 30, 50}
[12, 13, 8] -> 8 13이 되지만 개수는 일치하니까 문제는 없음
'''
import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    st = [] # 오름차순으로 정렬될 배열
    for x in a: # 입력배열에서 하나 꺼내기
        idx = bisect.bisect_left(st, x) # 이걸 저장할 배열에서 같은숫자 위치 찾기
        if idx == len(st): # 같은 숫자가 없으면
            st.append(x)  # [추가]
        else: # 같은 숫자가 있으면
            st[idx] = x   # [교체]

    print(len(st))
solve()
