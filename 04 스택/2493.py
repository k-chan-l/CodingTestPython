'''
탑의 왼쪽으로 레이저를 날리고, 그 레이저를 수신하는 탑의 번호를 반환하는 문제
->시작값은 1부터 시작
------------------
처음 포인터를 인풋의 마지막 값으로 잡기
해당값을 스택으로 이동, 포인터를 앞으로 이동
스택의 탑이랑 해당 포인터를 비교, 포인터의 위치가 더 크면 스택을 팝 하고 해당 지점의 값에 현재 포인터의 위치로 채우기
아닐경우 다시 위로 반복
남아있는 스택의 값들을 전부 0으로 바꿈
'''
import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    st = []
    answer = [0]*(n)

    for i, x in enumerate(reversed(arr)):
        i = n-i-1 # 인덱스 역순으로 뒤집기 + 0부터 시작으로 변경
        while st:
            if st[-1][0] < x: # st의 top 값과, 지금 값을 비교 / 높이가 서로 다르기 때문에 가능
                value, idx = st.pop()
                answer[idx] = i+1 # 1부터 시작으로 기준 변경
            else :
                break
        st.append((x,i))
    while st:
        value, idx = st.pop()
        answer[idx] = 0
    print(' '.join(map(str, answer)))
solve()