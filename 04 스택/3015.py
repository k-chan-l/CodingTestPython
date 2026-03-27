'''
3015의 Docstring

n명
앞에서 부터 순서대로 주어짐
a와 b사이에 둘보다 큰사람이 없어야 함 둘중 작은 수보다 큰 사람이 없어야 함
-> 가장 큰값만 남기고 서로 비교? 스택

현재 값이 더 작으면?

2 4 1 2 2 5 1

1. 앞에서부터시작
2. 새로들어온 값이 더 크면 스택 꺼내면서 작아질때까지 반복 +1
3. 작으면 +1
3. 스택에 집어넣기

4 3 2 1
4 3 2
'''
import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    answer = 0
    st = [] # [값, 개수]
    for i in range(n) :
        a = int(input())
        count = 0
        while st and st[-1][0] < a :
            answer += st.pop()[1]
        if st and st[-1][0] == a:
            count = st.pop()[1]
            answer += count
            if st :
                answer += 1
        elif st and st[-1][0] > a:
            answer += 1
        st.append([a, count+1])
    print(answer)
solve()

            