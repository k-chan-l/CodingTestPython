for a in range(3):
    yut = list(map(int, input().split()))
    if yut.count(0) == 0 :
        print('E')
    elif yut.count(0) == 1 :
        print('A')
    elif yut.count(0) == 2 :
        print('B')
    elif yut.count(0) == 3 :
        print('C')
    else :
        print('D')