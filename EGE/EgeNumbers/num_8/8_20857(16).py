from itertools import product
sp = list(map(''.join,product('012345678', repeat=6)))
sp.sort()
sp = sp[sp.index('100000'):]


for i,x in enumerate(sp, start=1):
    if i % 10 == 5 and all(not(int(x[j]) % 2 and int(x[j+1]) % 2) for j in range(5)):
        res = x

print(res)

