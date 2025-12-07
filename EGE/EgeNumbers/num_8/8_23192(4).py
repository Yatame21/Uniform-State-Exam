from itertools import product

sp = sorted(map(''.join, product('ТЕОРИЯ', repeat=6)))

res = 0
for i, x in enumerate(sp, 1):
    if i % 2 == 1 and x[0] not in 'РТЯ' and x.count('И') >= 2:
        res = i

print(res)