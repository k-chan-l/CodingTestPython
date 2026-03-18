import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    for i in range(n) :
        st = []
        s = input().rstrip()
        is_VPS = True
        for c in s :
            if c == ')' :
                if st and st[-1] == '(' :
                    st.pop()
                else :
                    is_VPS = False
                    break
            else :
                st.append(c)
        if len(st) != 0 :
            is_VPS = False
        if is_VPS :
            print('YES')
        else :
            print('NO')
solve()