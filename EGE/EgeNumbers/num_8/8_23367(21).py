from itertools import product
sp = list(map(''.join, product('0123456', repeat=5)))

ct =0

for x in sp:
    if x[0]!='0' and x.count('6') == 1 and all(x[i] != x[i+1] for i in range(len(x)-1)):
            ct +=1

print(ct)