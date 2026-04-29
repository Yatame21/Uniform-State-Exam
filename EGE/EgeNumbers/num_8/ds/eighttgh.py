from itertools import product
k=0
for i in product(sorted('ГИРЛЯНДА'),repeat=9):
    s=''.join(i)
    if s.count('А') == 1 :
        for i in 'ГРЛНД':
            s=s.replace(i,'а')
        if 'аА' not in s and 'Аа' not in s:
            k+=1

print(k)