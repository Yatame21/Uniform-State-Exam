from itertools import product
k=0
for i in product(sorted('АВОРТ'), repeat=6):
    s=''.join(i)
    k+=1
    if s == 'ВОРОТА':
        print(k)
        break