from itertools import product
k=0
for i in product(sorted('АВЛОС'),repeat=4):
    s=''.join(i)
    k+=1
    if s[0] == 'Л':
        print(k)
        break

