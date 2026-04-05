'''
가장 긴 짝수 연속한 부분 수열 (large)

수열 S에서 k번만큼 임의의 숫자를 지워 가장 긴 길이의 짝수 부분수열을 만들어라
-> 임의의숫자 뭘지우지? 가장긴 짝수 부분수열을 만들려면 긴 짝수 부분수열 끼리 합치는게 중요
-> 부분수열을 압축 짝수는 짝수, 홀수는 홀수 끼리 합침 짝 홀 짝 홀 짝 홀 짝 순서로 될텐데
홀의 숫자 만큼 빼서 가장 큰 숫자가 나오는 수열을 구한다. 슬라이딩 도어 윗 작업은 필요 없음?

짝수가 나올때 까지 st이동/ 그다음 ed이동, 홀수의 개수가 k를 넘기 전까지, 그때 길이 - k를 answer로 변경
그다음 다시 홀수가 나오고, 짝수가 나올때 까지 st이동 어떻게? 홀수 짝수 변하는 횟수를 둘까? 2가 될때까지?
'''
import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().rstrip().split())
    s = list(map(int, input().rstrip().split()))

    st = 0
    ed = 0
    count = 0
    answer = 0

    for st in range(n):
        while ed < n and count <= k:
            if s[ed] % 2 == 1:
                count += 1
            ed += 1
        answer = max(answer, ed-st-count)
        if s[st] % 2 == 1:
            count -= 1
    print(answer)
solve()