import sys
input = sys.stdin.readline

def solve():
    while True:
        x = list(map(int, input().rstrip().split()))
        n = x[0]
        if n == 0:
            break
        h = x[1:]
        st = []
        max_sq = 0
        for a in h :
            count = 0
            while st and st[-1][0] >= a :
                i = st.pop()
                count = i[1] + count                
                max_sq = max_sq if max_sq > count * i[0] else count * i[0] #최대값 갱신
            st.append([a, count + 1])
        count = 0
        while st :
            i = st.pop()
            count = i[1] + count
            max_sq = max_sq if max_sq > count * i[0] else count * i[0] #최대값 갱신
        print(max_sq)
solve()

'''
st은 오름차순으로 정렬
저장되는 값은 높이, 개수
다음값이 더 낮으면 현재값을 빼서 다음값으로 바꾼 후 값을 더하기
빼는 과정에서 max_sq 갱신
최종적으로 모든값을 빼면서 다시 갱신
'''



