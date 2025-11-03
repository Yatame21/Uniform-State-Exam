from itertools import product
sp=list(map(''.join,product('СТРОКА', repeat=5)))
sp.sort()

for i,x in enumerate(sp,start=1):
    if i%2==0 and x[0] not in 'АСТ' and x.count('О')==2:
        rez=i
        # break
print(rez)

# 5058