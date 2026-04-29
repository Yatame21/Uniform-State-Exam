from itertools import product
k=0
for i in product('0123456',repeat=6):
    s=''.join(i)
    if s[0]!='0' and s[0] in '246' and s.count('5') == 2:
        k+=1
print(k)