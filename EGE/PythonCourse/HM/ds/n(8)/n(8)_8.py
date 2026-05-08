from itertools import product
k=0
e=0
for i in product(sorted('ВОСТРГ'),repeat=6):
    s=''.join(i)
    k+=1
    if s == 'СГОВОР':
        e+=1
    if e == 1 and s !='СГОВОР' :
        for i in "ВСТРГ":
            s=s.replace(i,'x')
        if 'xx' not in s:
            print(k)
