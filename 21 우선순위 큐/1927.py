import sys
input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.heap = [0] * 100010 # 빈 힙
        self.sz = 0 # 힙의 개수

    def push(self, num):
        self.sz += 1 # 개수 증가
        self.heap[self.sz] = num # 맨 뒤에 값을 부여
        pos = self.sz # 현재 위치를 맨 뒤로 지정

        while pos > 1: # 뒤에서 부터 앞으로 순회
            par = pos//2 # 부모 인덱스 지정
            if self.heap[par] <= self.heap[pos]: # 부모가 자식보다 작거나 같으면(정상이면)
                break # 끝내라
            self.heap[par], self.heap[pos] = self.heap[pos], self.heap[par] # 아니면 서로 바꾸고
            pos = par # 다음으로가서 다시 검사

    def pop(self):
        if self.sz == 0: # 비어있으면
            return 0 # 0 반환
        pos = 1 # 현 위치를 맨 앞으로 지정
        num = self.heap[pos] # 반환할 값 임시저장
        self.heap[pos] = self.heap[self.sz] # 다시 트리를 정렬하기 위해 맨뒤의 값이랑 스왑 이 과정에서 반환할값은 힙에서 삭제
        self.sz -= 1 # 개수 감수
        
        while pos*2 <= self.sz: # 현위치의 자식이 하나 이상일 경우
            lc, rc = pos*2, pos*2+1 # 자식들의 위치를 지정
            min_child = lc # 일단 최소값은 left로 설정
            if rc <= self.sz and self.heap[rc] < self.heap[lc]: # right가 존재하고 더 작으면
                min_child = rc # 최소값을 right로 변경
            if self.heap[pos] <= self.heap[min_child]: # 현재값이 자식보다 더 작으면(정상이면)
                break # 끝내라
            self.heap[pos], self.heap[min_child] = self.heap[min_child], self.heap[pos] # 아닐경우 스왑
            pos = min_child # 아래로 내려가서 다시검사

        return num

h = Heap()
n = int(input().rstrip())
for i in range(n):
    a = int(input().rstrip())
    if a == 0:
        print(h.pop())
    else:
        h.push(a)
