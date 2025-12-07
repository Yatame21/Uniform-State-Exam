from itertools import product

sp = sorted(map(''.join, product('ФОКУС', repeat=5)))

res = 0
for i, x in enumerate(sp, 1):
    if 'Ф' not in x and x.count('У') == 2:
        res = i

print(res)