import sys
input = sys.stdin.readline

def solve() :
    n = int(input())
    for i in range(n) :
        before, after = input().rstrip().split(' ')
        befores = [0] * 26; afters = [0] * 26
        for a in before:
            befores[ord(a) - ord('a')] += 1
        for a in after:
            afters[ord(a) - ord('a')] += 1
        flag = True
        for a in range(26) :
            if befores[a] != afters[a] :
                print('Impossible')
                flag = False
                break
        if flag :
            print('Possible')
solve()