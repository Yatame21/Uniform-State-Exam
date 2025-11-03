from itertools import product
sp = list(map(''.join,product('ПРЕСТОЛ',repeat=5)))
sp.sort()

ct = 0

for i,x in enumerate(sp,start=1):
    if i%2==1 and x[-1] in 'ЕО' and sum(1 for n in x if n in 'ПРСТЛ') <= 3:
        ct+=1
print(ct)