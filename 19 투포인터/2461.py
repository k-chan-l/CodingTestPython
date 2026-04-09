'''
n개의 학급, m명
능력치의 최대값과, 최솟값의 차이가 최소가 되는 선수를 선발
각 학급당 한명씩 뽑고, 그 값의 차이가 최솟값이 경우를 선발
'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**10
def solve():
    n, m = map(int, input().rstrip().split())
    classes = []
    for _ in range(n):
        classes.append(sorted(list(map(int, input().rstrip().split()))))
    pt = [0]*n # 각 학급별 대표학생의 순번
    answer = INF
    max_pt = max(range(n), key=lambda i : classes[i][pt[i]]) # 교실의 대표학생들 중 최대값의 학생의 교실을 구함
    max_num = classes[max_pt][pt[max_pt]] # 교실의 위치로 학생의 최대값을 구함
    pq = []
    # 우선순위 큐로 최소값 관리,
    for i in range(n):
        heapq.heappush(pq, (classes[i][pt[i]], i)) # 최소값, 최소 위치
    while True:
        # 뭘 옮기는게 효율적일까? => 가장 작은값을 키우는게 차이를 좁히는 방법
        # min의 최소값과 위치를 찾고, 그 값을 계산한다. max의 최소값과 위치를 찾고 그 값을 계산한다. 0이 아니면 계속 수정한다.
        min_num, min_pt = heapq.heappop(pq)
        answer = min(answer, max_num-min_num) # 값의 차이를 계산
        if answer == 0: #0일경우 개선이 필요없으므로 반환
            print(0)
            return
        if pt[min_pt] == m-1:
            break
        # 최소값을 키운다
        pt[min_pt] += 1
        heapq.heappush(pq, (classes[min_pt][pt[min_pt]], min_pt))
        if classes[min_pt][pt[min_pt]] > max_num:
            max_pt = min_pt
            max_num = classes[max_pt][pt[max_pt]]
    print(answer)
solve()