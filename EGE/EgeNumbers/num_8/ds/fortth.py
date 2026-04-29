from itertools import product
k=0
for i in product(sorted('КАБИНЕТ'),repeat=7):
    s=''.join(i)
    if len(set(s)) == len(s) and s[6] not in 'АИЕ':
        k+=1
print(k)



'''
a = '887790'
print(set(a))
if len(set(a))==len(a):
    print('yes')
'''