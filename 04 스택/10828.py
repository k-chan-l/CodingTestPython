import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    arr = []
    for i in range(n) :
        t = input().rstrip().split()
        instruction = t[0]
        num = 0
        if len(t) == 2 :
            num = int(t[1])
        if instruction == 'push' :
            arr.append(num)
        elif instruction == 'pop':
            if len(arr) == 0 :
                print(-1)
            else :                
                print(arr.pop())
        elif instruction == 'size':
            print(len(arr))
        elif instruction == 'empty':
            print(1 if len(arr) == 0 else 0)
        else :
            if len(arr) == 0 :
                print(-1)
            else :                
                print(arr[len(arr)-1])
            
solve()