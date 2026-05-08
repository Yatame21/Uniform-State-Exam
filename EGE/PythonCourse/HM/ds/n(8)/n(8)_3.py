from itertools import product
k=0
for i in product(sorted('ЩДСЭР'),repeat=4):
    s=''.join(i)
    k += 1
    if s == 'ЩДЩД':
        print(k)
        break


