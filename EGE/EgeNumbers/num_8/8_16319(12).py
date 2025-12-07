from itertools import product

sp = sorted(map(''.join, product('ПАРУС', repeat=5)))

result = 0
for i, x in enumerate(sp, 1):
    if x.count('У') <= 1 and 'АА' not in x:
        result = i

print(result)