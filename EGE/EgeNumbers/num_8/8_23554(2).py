from itertools import product
sp=list(map(''.join,product('АЛГОРИТМ', repeat=5)))
sp.sort()

for i,x in enumerate(sp,start=1):
    if i%2==0 and x[0] not in 'АГ' and x.count('Р')>=2:
        res = i
        break
print(res)