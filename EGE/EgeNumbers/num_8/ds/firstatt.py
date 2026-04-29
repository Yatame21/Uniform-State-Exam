from itertools import product
k=0
for i in product(sorted('ДСР'), repeat=3):
    s = ''.join(i)
    if s[0]=='С':
        k+=1
print(k)

