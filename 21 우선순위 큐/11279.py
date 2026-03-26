import sys
input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.h = [0] * 100005
        self.sz = 0

    def push(self, x):
        '''
        1. x를 맨 뒤에 붙인다
        2. 맨 뒤에서부터 앞까지 정렬한다
        
        '''
        self.sz += 1
        self.h[self.sz] = x
        cur = self.sz

        while cur > 1 :
            '''
            cur 시점에서의 값과, 이걸 반으로 나눈값을 비교해서 cur시점의 값이 작으면 스탑 아니면 계속 가게 만든다.
            '''
            next = cur//2
            if self.h[cur] <= self.h[next]:
                break
            self.h[cur], self.h[next] = self.h[next], self.h[cur]
            cur = next
            
    def pop(self):
        '''
        0. sz가 0일때, 호출하면 0반환
        1. 맨뒤의 값과 맨 앞의 값을 바꾼다.
        2. 해당값을 임시저장한다.
        3. sz를 내리고, 다시 앞에서부터 정렬한다.
        4. 임시저장한 값을 반환한다.
        '''
        if self.sz == 0:
            return 0

        cur = 1
        result = self.h[cur]
        self.h[self.sz], self.h[cur] = self.h[cur], self.h[self.sz]
        self.sz -= 1

        while cur*2 <= self.sz:
            left = cur*2
            right = cur*2 + 1

            next = left
            if right <= self.sz and self.h[right] > self.h[left] : # 10 5
                next = right
            if self.h[cur] > self.h[next]:
                break
            self.h[cur], self.h[next] = self.h[next], self.h[cur]
            cur = next

        return result
h = Heap()
n = int(input().rstrip())
for i in range(n):
    x = int(input().rstrip())
    if x == 0:
        print(h.pop())
    else :
        h.push(x)
