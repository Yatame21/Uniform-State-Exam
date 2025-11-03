for x in range(2005, 0, -1):
    n = 43**56 + 113**841 - x
    r = 0
    while n > 0:
        if n % 4 % 2 == 0:
            r += 1
        if n % 4 == 2:
            r += 1
        n //= 4
        #if
    print(x)    