def solve() :
    arr = []
    for a in range(9) :
        arr.append(int(input()))
    arr.sort()
    x = sum(arr) - 100
    for i in range(9):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == x :
                for k in range(9) :
                    if k == i or k == j :
                        continue
                    print(arr[k])
                return
solve()
