def solve() :
    count = int(input())
    arr = list(map(int, input().split()))
    young, minn = 0, 0
    for i in range(count) :
        young += (arr[i] // 30 + 1) * 10
        minn += (arr[i] // 60 + 1) * 15
    if young > minn :
        print('M', minn)
    elif young == minn :
        print('Y M', young)
    else :
        print('Y', young)
solve()