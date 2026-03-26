import sys
from collections import deque
input = sys.stdin.readline
'''
원모양에서 사람들이 제거되도록 구현하는 문제 제거된 사람은 정답 리스트에 담기
덱을 이용해서 원형 큐처럼 구현하여 계산
1 ~ N까지의 수열을 넣은 덱 작성
while문으로 덱이 빌때까지 계속해서 반복하여 삭제, 혹은 넘기기 실행
'''
def solve() :
    answer = []
    count = 1
    n, k = map(int, input().split())
    dq = deque(range(1,n+1))    
    while len(dq) != 0 :
        if count % k == 0 :
            count += 1
            answer.append(dq.popleft())
        else :
            count += 1
            dq.append(dq.popleft())
    print('<' + ', '.join(map(str, answer)) + '>')
solve()