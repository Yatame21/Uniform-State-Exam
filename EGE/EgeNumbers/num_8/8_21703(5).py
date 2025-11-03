from itertools import product
sp = list(map(''.join,product('ПОБЕДА', repeat=6)))
sp.sort()

for i,x in enumerate(sp,start=1):
    if i%2==0 and x[0] == 'О' and len(set(x)) == 6:
        res = i

print(res)