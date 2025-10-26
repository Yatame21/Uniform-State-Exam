sp = [int(x) for x in open('17data/17_23376.txt')]

m = max(x for x in sp if 10000 <= abs(x) <= 99999 and x % 100 == 37)

res = []

for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    n1 = 10000 <= abs(x) <= 99999
    n2 = 10000 <= abs(y) <= 99999
    if (n1 and not n2) or (not n1 and n2):
        if (x + y) ** 2 > m ** 2:
            res.append(x + y)

print(len(res), max(res))