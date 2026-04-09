'''
세 용액

세가지 용액의 합이 0에 가까운 용액
1. 정렬한다.
2. 앞에서부터 순회한다.
3. 두개의 용액을 더한 용액을 만든다. 그 용액을 순회하면서 나머지 용액과 더해서 0이 되면 없앤다.
'''
import sys
input = sys.stdin.readline
INF = 10**10
def solve():
    n = int(input())
    liquid = sorted(list(map(int, input().rstrip().split())))
    answer = (INF,[])
    for i in range(n-2):
        st = i+1
        ed = n-1
        while ed > st:
            x = liquid[i] + liquid[st] + liquid[ed]
            if answer[0] > abs(x):
                answer = (abs(x), [liquid[i], liquid[st],liquid[ed]])
            if x > 0:
                ed-=1            
            elif x == 0:
                print(liquid[i], liquid[st],liquid[ed])
                return
            else :
                st+=1
    print(' '.join(map(str,answer[1])))
solve()