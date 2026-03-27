import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    st = []
    answer = [0] * n
    top = 0
    # 0 1 2 3 4 이렇게 만들고 할때마다 원본 자료로 가서 확인하는 방식으로 ㄱㄱ
    for a in range(n-1,-1,-1):#역순으로 db에 접근
        x = arr[a]
        # 스택이 있을 경우
        if len(st) != 0:
            top = arr[st[len(st)-1]] #stack의 최고값

        # top이 없거나 현재 값보다 클 경우
        if top == 0 or top > x:
            st.append(a)

        # 현재 값보다 작을 경우
        else :
            while top < x: #모든 탑이 현재 값보다 작을때까지
                answer[st.pop()] = a + 1
                if len(st) != 0:
                    top = arr[st[len(st)-1]]
                else :
                    top = 0
                    break
            st.append(a)
    for a in answer:
        print(a, end=' ')
solve()