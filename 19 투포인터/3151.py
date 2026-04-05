'''
합이 0

들어오는 리스트 중에서 3을 골라서 그 값이 0이 되는지 확인
0. 정렬
투포인터로 st부터 ed까지의 합을 구하기

3개의 합이 0이 된다? 두개의 합을 구했을때, 그 합의 역수가 그 다음범위에 존재하는가?
n^2으로 가능
2중for문으로 처음 기준을 정하고, 그 안에서 투포인터로 합이 0이 되는 두개의 값을 구한다.
'''
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    students = sorted(list(map(int, input().rstrip().split())))
    answer = 0
    if n < 3 :
        print(0)
        return
    for idx in range(n-2):# 0 ~ n-3
        v = -students[idx] # 두 수의 합이 0에서 나머지 한 값을 뺀 값이 나와야 세 수 의 합이 0이 됌
        ed = n-1 # 최대 탐색 가능 범위 
        st = idx + 1 # 1 ~ n-2
        while st < ed and st < n-1:
            while st < ed and students[st] + students[ed] > v: #ed를 줄임 -> 합을 줄임
                ed -=1
            if st != ed and students[st] + students[ed] == v:
                cur_st = st
                cur_ed = ed
                if students[cur_st] == students[cur_ed]:
                    sub = ed - st
                    answer += (sub+1)*(sub)//2
                    break
                while st <= ed and students[cur_st] == students[st]:
                    st += 1
                while st <= ed and students[cur_ed] == students[ed]:
                    ed -= 1
                answer += (st-cur_st)*(cur_ed-ed)
            else:
                st += 1
    print(answer)
solve()