import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(range(n, 0, -1))
    prev = []
    answer = []
    for a in range(n) :
        x = int(input())

        while True:
            top = 0
            if len(prev) != 0 :
                top = prev[len(prev)-1]
            if top == 0 or top < x:
                prev.append(arr.pop())
                answer.append('+')
            elif top == x :
                prev.pop()
                answer.append('-')
                break
            else :
                print("NO")
                return
    for a in answer :
        print(a)
solve()

        