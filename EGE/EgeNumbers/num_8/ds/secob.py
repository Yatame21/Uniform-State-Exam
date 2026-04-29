from itertools import product
k=0
for i in product(sorted("012345678"), repeat=6):
    s = ''.join(i)
    if s[0] !='0' and s.count('4') <=2 :
        k+=1
print(k)