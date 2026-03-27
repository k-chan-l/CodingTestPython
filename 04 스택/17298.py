import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    st = []
    answer = []
    for a in arr :
        while st and st[-1] <= a:
            st.pop()
        top = -1
        if st :
            top = st[-1]
        answer.append(top)
        st.append(a)
    answer.reverse()
    print(' '.join(map(str, answer)))
solve()