from itertools import product
sp = list(map(''.join, product('ПАВСИКЙ', repeat=6)))
sp.sort()

ct = 0

for i,x in enumerate(sp, start= 1):
    if any(x[j] in 'АИ' and x[j+1] in 'АИ' for j in range(len(x)-1)):
        ct +=1
        if x == 'КАКААА':
            print(ct)
            break

