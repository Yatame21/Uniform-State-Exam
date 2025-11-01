res = []
for x in range(1,3001):
    n = 4 ** 210 + 4 ** 110 - x
    r = 0
    while n > 0:
        if n % 4 == 0:
            r +=1
        n//=4
    res.append([r,x])
res.sort()
print(res)