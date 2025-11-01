for x in range(1, 3001):
    n = 9  ** 150 + 9 ** 30 - x
    r = 0
    while n > 0:
        if n %  9 == 0:
            r += 1
        n//=9
    if r == 122:
        print(x)
        break