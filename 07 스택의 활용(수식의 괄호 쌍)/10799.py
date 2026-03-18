import sys
input = sys.stdin.readline

def solve() :
    s = input().rstrip()
    st = []
    last = ''
    answer = 0
    for c in s :
        if c == ')' :
            st.pop()
            if last == '(' :
                answer += len(st)
            else :
                answer += 1
        else :
            st.append('(')
        last = c
    print(answer)
solve()

