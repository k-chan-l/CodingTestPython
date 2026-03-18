import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    answer = 0
    for a in range(n) :
        s = input().rstrip()
        st = []
        for c in s :
            if c == 'A' :
                if st and st[-1] == 'A' :
                    st.pop()
                else :
                    st.append(c)
            else :
                if st and st[-1] == 'B' :
                    st.pop()
                else :
                    st.append(c)
        if len(st) == 0 :
            answer += 1
    print(answer)
solve()