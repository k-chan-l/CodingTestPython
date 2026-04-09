'''
공유기 설치
n개의 집에서 공유기 c개를 설치한다고 할때
집에는 공유기를 한개면 설치 가능 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
 ㅂ      ㅂ          ㅂ
 ㅁ ㅁ x ㅁ x x x ㅁ ㅁ
공유기 사이의 최대 거리를 최대로 하려면 1 4 9에 위치해서 사이의 거리가 3이된면다.
어떻게 계산? 가장 인접한 거리의 공유기 사이의 거리가 최대가 되려면 (최대 좌표-최소 좌표/c)
1. 임의의 최소 거리를 지정한다.
2. 맨 앞에있는 좌표에 공유기를 설치한다.
3. 그다음 공유기의 위치를 오른쪽으로 순회하면서 찾는다. 최소 거리보다 같거나 큰경우만 지정
4. 해당 거리를 현재 거리의 최소 값으로 지정,
5. 3-4를 반복하면서 최소 값을 갱신
6-1. 모든 공유기를 설치했을 경우 기록된 최소값을 현재 최대값과 비교하여 갱신, 갱신에 성공했으면 True를 반환하고, 아니면 False를 반환
6-2. 모든 공유기를 설치못했을 경우 False를 반환
7-1. True를 반환했을 경우. 임의의 최소거리보다 더 큰 숫자를 사용
7-2. False를 반환했을 경우. 임의의 최소거리보다 더 작은 숫자를 사용
'''
import sys
input = sys.stdin.readline

def is_possible(dist, houses, c):
    house = houses[0]
    c-=1
    for next_house in houses:
        if next_house - house >= dist: # 거리를 넘겼을때만 가능
            house = next_house # 현재 집 갱신
            c -= 1
            if c == 0:
                return True
    return False
        

def solve():
    n, c = map(int, input().rstrip().split())
    houses = []
    for _ in range(n):
        house = int(input())
        houses.append(house)
    houses.sort()
    st = 1
    ed = houses[-1] - houses[0]
    mid = (ed-st)//2+st
    while st <= ed:
        if is_possible(mid, houses, c): # 해당 최소 거리로 모든 공유기를 배치 가능
            st = mid+1
            mid = (ed-st)//2+st
        else: # 해당 최소 거리로 모든 공유기를 배치할수 없음, 기준값을 하향
            ed = mid-1
            mid = (ed-st)//2+st
    print(ed)
solve()