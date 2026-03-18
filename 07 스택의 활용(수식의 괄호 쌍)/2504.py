'''
(()[[]])([])
괄호가 완성되면 stack에 숫자 넣기
0. while을 통해 괄호가 완성될때까지 스택 비우기
0.5. 스택에 숫자가 있으면 현재값에 더하기
1. 스택이 비어있으면 현재값을 정답에 더하기 
2. 괄호가 불량하면 즉시 종료

'''
import sys
input = sys.stdin.readline

def solve() :
    s = input().rstrip()
    st = []
    answer = 0

    for c in s :
        cur = 0
        if c == ')' :
            while st and st[-1] != '(' :
                x = st.pop()
                if type(x) == int :
                    cur += x
                else :
                    st.append(x)
                    break
            if st and st[-1] == '(' :
                st.pop()
                if cur == 0 :
                    cur = 2
                else :
                    cur *= 2
                if st :
                    st.append(cur)
                else :
                    answer += cur
            else :
                st.append(c)
                break
        elif c == ']' :
            while st and st[-1] != '[' :
                x = st.pop()
                if type(x) == int :
                    cur += x
                else :
                    st.append(x)
                    break
            if st and st[-1] == '[' :
                st.pop()
                if cur == 0 :
                    cur = 3
                else :
                    cur *= 3
                if st :
                    st.append(cur)
                else :
                    answer += cur
            else :
                st.append(c)
                break
        else :
            st.append(c)
    if len(st) != 0 :
        answer = 0
    print(answer)

solve()