# 절대값 힙
import sys
input = sys.stdin.readline

class AbsoluteHeap():
    def __init__(self):
        self.h = [0] * 100010
        self.sz = 0

    def push(self, x):
        self.sz += 1
        self.h[self.sz] = x

        cur = self.sz
        while cur > 1:
            next = cur // 2
            if abs(self.h[next]) < abs(self.h[cur]) :
                break
            if abs(self.h[cur]) == abs(self.h[next]) and self.h[next] <= self.h[cur]:
                break
            self.h[next], self.h[cur] = self.h[cur], self.h[next]
            cur = next

    def pop(self):
        if self.sz == 0:
            return 0
        cur = 1
        result = self.h[cur]
        self.h[cur], self.h[self.sz] = self.h[self.sz], self.h[cur]
        self.sz -= 1

        while cur*2 <= self.sz:
            left = cur*2
            right = left+1
            next = left
            if right <= self.sz and abs(self.h[right]) < abs(self.h[left]):
                next = right
            if right <= self.sz and abs(self.h[right]) == abs(self.h[left]) and self.h[right] < self.h[left]:
                next = right
            if abs(self.h[cur]) < abs(self.h[next]) :
                break
            if abs(self.h[cur]) == abs(self.h[next]) and self.h[cur] <= self.h[next]:
                break
            self.h[cur], self.h[next] = self.h[next], self.h[cur]
            cur = next

        return result

h = AbsoluteHeap()
n = int(input().rstrip())
for i in range(n) :
    x = int(input().rstrip())
    if x == 0:
        print(h.pop())
    else :
        h.push(x)