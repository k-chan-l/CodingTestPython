'''
List of Unique Numbers

길이가 n인 수열에서 연속한 1개 이상의 수를 뽑았을때, 같은수가 여러번 등장하지 않는 경우의 수를 구해라
연속된 수 -> 슬라이딩 도어 -> 투 포인터
같은수가 나오기 전까지 계속 슬라이딩을 확장
같은 수가 나왔다면, 1에서부터 지금까지의 딕셔너리의 개수만큼의 합을 구한다.
그 후 st를 옆으로 움직여 지금 ed의 값과 같은값이 나올때까지 딕셔너리에서 뺀다.
이 과정을 계속 반복한다.
'''
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    uni = [0]*(100001)

    ed = 0
    answer = 0
    count = 0
    for st in range(n+1):
        while ed < n and uni[arr[ed]] < 1:
            count += 1
            uni[arr[ed]] += 1
            ed += 1
            answer += count
        if ed == n:
            break
        uni[arr[st]] -= 1
        count -= 1
    print(answer)
solve()