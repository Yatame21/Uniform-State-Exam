from itertools import product
kb=[]
k=0
shal =set('ЮЕИ')
SHALAVAAAAAAAAAAAAAA = set('БДЖТНК')
for i in product(sorted('БЮДЖЕТНИК'), repeat=6):
    s=''.join(i)
    k+=1
    if s == 'БЮДЖЕТ' :
        break

    ex = True
    for j in range(5):
        if (s[j] in shal) == (s[j+1] in shal):
            ex = False
            break
    for j in range(5):
        if (s[j] in SHALAVAAAAAAAAAAAAAA) == (s[j+1] in SHALAVAAAAAAAAAAAAAA):
            ex = False
            break
    if ex:
        kb.append(k)

print(sum(kb))

'''
from itertools import product
k=0
count = 0
for i in product(sorted('БЮДЖЕТНИК'),repeat=6):
    s=''.join(i)
    k+=1
    if s!='БЮДЖЕТ':
        for i in 'ЮЕИ':
            s=s.replace(i,'a')
        for i in 'БДЖТНК':
            s=s.replace(i,'b')
        if 'aa' not in s and 'bb' not in s:
            count+=k
    if s=='БЮДЖЕТ':
        break
print(count)'''