import sys
input = sys.stdin.readline

def solve() :
    max_num = 0
    turn = 0
    for a in range(1,10) :
        num = int(input())
        if num > max_num :
            max_num = num
            turn = a
    print(max_num)
    print(turn)
solve()