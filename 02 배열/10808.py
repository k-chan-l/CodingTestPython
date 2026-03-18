import sys
input = sys.stdin.readline
'''
알파벳이 몇개가 포함되어 있는지 구하는 프로그램
1. 알파벳 개수는 고정 -> 알파벳을 기록할 딕셔너리를 만드는것이 간단
2. 문자열을 순회 : O(n)
3, 단어 개수를 출력 : O(26)
'''
def solve() :
    words = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0,
            'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0,'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0,
            'y' : 0, 'z' : 0,  }
    s = input().rstrip()
    for a in s:
        words[a] += 1
    for a in list(words.values()) :
        print(a, end=' ')
solve()