from itertools import product

sp = list(map(''.join, product('ЯНВАРЬ', repeat=5)))
sp.sort()

for i, x in enumerate(sp, start=1):
    if x[0] != 'Я' and x.count('Ь') <= 1 and 'ЯЯ' not in x:
        res = i

print(res)