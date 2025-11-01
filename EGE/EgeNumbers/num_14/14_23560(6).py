for x in range(1,2401):
    n = 7 * 9 ** 210 + 6 * 9 **110 - x
    r = 0
    while n > 0:
        if n % 9 ==0:
            r +=1
        n//=9
    if r == 100:
        print(x)