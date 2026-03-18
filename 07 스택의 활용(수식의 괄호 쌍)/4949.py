import sys
input = sys.stdin.readline

def solve():
    while True:
        st = []
        s = input().rstrip()
        if s == '.' :
            break
        isBalanced = True
        for a in s :
            if a == '[' :
                st.append(a)
            elif a == ']' :
                if st and st[-1] == '[' :
                    st.pop()
                else :
                    isBalanced = False
                    break
            if a == '(' :
                st.append(a)
            elif a == ')' :
                if st and st[-1] == '(' :
                    st.pop()
                else :
                    isBalanced = False
                    break
        if len(st) != 0 :
            isBalanced = False
        if isBalanced :
            print('yes')
        else :
            print('no')
solve()