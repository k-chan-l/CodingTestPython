import sys
input = sys.stdin.readline

def solve() :
    n, m = map(int, input().rstrip().split())
    maps = []
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(n) :
        maps.append(list(map(int, input().rstrip().split())))
    st = []
    count = 0
    maxSize = 0
    for i in range(n) :
        for j in range(m) :
            size = 0
            if maps[i][j] == 1 :
                st.append([i,j])
            while st :
                x,y = st.pop()
                if maps[x][y] != 1 :
                    continue
                else :
                    maps[x][y] = 2
                size += 1
                for k in move :
                    a,b = k
                    if x + a < 0 or x + a >= n or y + b < 0 or y + b >= m :
                        continue
                    if maps[x + a][y + b] != 1 :
                        continue
                    st.append([x+a,y+b])
            if size != 0 :
                count += 1
                maxSize = max(size, maxSize)
    print(count)
    print(maxSize)
solve()





'''
앞에서 부터 순환하면서 방문했거나, 길이 아닌곳은 스택에 삽입하지 않기

'''