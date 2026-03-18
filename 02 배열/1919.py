import sys
input = sys.stdin.readline

def solve() :
    first = input().rstrip(); second = input().rstrip()
    firsts = [0] * 26; seconds = [0] * 26
    count = 0
    for a in first :
        firsts[ord(a) - ord('a')] += 1
    for a in second :
        seconds[ord(a) - ord('a')] += 1
    for i in range(26) :
        gap = firsts[i] - seconds[i]
        if gap < 0 :
            gap *= -1
        count += gap
    print(count)
solve()