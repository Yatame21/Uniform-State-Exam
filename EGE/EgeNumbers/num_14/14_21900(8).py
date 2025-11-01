for x in range(1,2301):
    n = 7 ** 350 + 7 ** 150 - x
    r = 0
    while n > 0:
        if n % 7 ==0:
            r+=1
        n//=7
    if r == 200:
        print(x)
        break
