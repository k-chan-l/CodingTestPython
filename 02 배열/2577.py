import sys
input = sys.stdin.readline
'''
세 자연수의 곱에서 각각의 숫자가 몇번씩 쓰였는지 계산하는 문제
1. 세 수를 곱한다
2. 문자열로 변환 -> 10씩 나누며 자리수를 분리하는 반복문을 사용하는 것도 가능
3. 한 글자씩 배열에 담음 -> 배열 인덱스가 동일하기 때문에 간단
4. 출력
'''
def solve() :
    arr = [0] * 10
    a = int(input())
    b = int(input())
    c = int(input())
    mul = a * b * c
    for a in str(mul) :
        arr[int(a)] += 1
    for a in arr :
        print(a)
solve()