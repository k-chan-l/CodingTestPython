'''
같은 값 처리가 핵심
같은값이 있으면 옥상을 볼수 없기 때문에 없앤다.
1. 빌딩을 앞에서부터 순회
2. st이 비어있으면 (높이, 개수)로 스택에 삽입
3. st이 비어있지 않으면, 현재 top과 비교
3-1. 현재 탑보다 작을경우, 그대로 st에 삽입
3-2. 현재 탑보다 크거나 같을경우, 현재 탑을 pop() 여기서 나온 지금 스택에 있는 탑의 개수 만큼 정답에 더함 : 이 작업을 현재 값보다 커지거나, 빌때 까지 반복
'''
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = []
    st = []
    answer = 0    
    for i in range(n) :
        arr.append(int(input()))
    for x in arr:
        while st:
            if st[-1] > x:
                break
            st.pop()
            answer += len(st)
        st.append(x)
    # 남아있는 스택 정리
    while st:
        st.pop()
        answer += len(st)
    print(answer)
solve()