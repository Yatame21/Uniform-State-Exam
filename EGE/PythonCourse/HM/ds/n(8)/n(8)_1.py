from itertools import product

for i in product(sorted('ОМГД'),repeat=4):
    s=''.join(i)
    print(s)
