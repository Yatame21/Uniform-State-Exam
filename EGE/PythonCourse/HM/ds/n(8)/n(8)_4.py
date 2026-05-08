from itertools import product
k=0
for i in product(sorted('ЯНДЕКС'),repeat=6):
    s=''.join(i)
    k+=1
    if s == 'ЯНДЕКС':
        print(k)
        break