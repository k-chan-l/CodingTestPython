import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = []
    st = []
    answer = 0
    for i in range(n) :
        arr.append(int(input()))
    for x in arr :
        if not(st) or st[-1] > x: #st이 비어있거나, 현재 값보다 클 경우
            st.append(x) #st에 값 추가
        else :#아니면
            #st 비우기
            while st and st[-1] <= x :
                st.pop()
                answer += len(st)
            st.append(x)
    while st :
        st.pop()
        answer += len(st)
    print(answer)
solve()